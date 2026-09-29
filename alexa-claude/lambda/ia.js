// ia.js — manda la domanda al modello scelto (Claude o Gemini) e restituisce
// il testo della risposta, già pronto da far leggere ad Alexa.

const Anthropic = require('@anthropic-ai/sdk');
const config = require('./config');

// Istruzioni fisse per il modello: risposte brevi, parlate, in italiano.
const ISTRUZIONI =
  "Sei un assistente vocale che risponde tramite un altoparlante Alexa, in italiano. " +
  "La risposta verrà letta ad alta voce: niente elenchi puntati, niente markdown, " +
  "niente emoji, niente link. Rispondi in modo naturale e breve: al massimo tre o " +
  "quattro frasi, salvo che l'utente chieda esplicitamente di più. " +
  "Latency-sensitive; begin your visible answer immediately.";

// Alexa aspetta circa 8 secondi: ci fermiamo prima per poter dire qualcosa.
const TEMPO_MASSIMO_MS = 7000;

let clientClaude = null;

async function chiediAClaude(storia) {
  if (!clientClaude) {
    clientClaude = new Anthropic({
      apiKey: config.CLAUDE_API_KEY,
      timeout: TEMPO_MASSIMO_MS,
      maxRetries: 0, // niente tentativi ripetuti: il tempo di Alexa è poco
    });
  }

  const risposta = await clientClaude.beta.messages.create({
    model: config.CLAUDE_MODEL,
    max_tokens: 2000,
    output_config: { effort: 'low' }, // risposte veloci, adatte alla voce
    system: ISTRUZIONI,
    messages: storia,
    // Se il modello rifiuta una richiesta, l'API riprova da sola con un altro modello.
    betas: ['server-side-fallback-2026-07-01'],
    fallbacks: 'default',
  });

  if (risposta.stop_reason === 'refusal') {
    return 'Mi dispiace, a questa domanda non posso rispondere.';
  }

  return risposta.content
    .filter((blocco) => blocco.type === 'text')
    .map((blocco) => blocco.text)
    .join(' ')
    .trim();
}

async function chiediAGemini(storia) {
  const url =
    'https://generativelanguage.googleapis.com/v1beta/models/' +
    encodeURIComponent(config.GEMINI_MODEL) +
    ':generateContent';

  const corpo = {
    systemInstruction: { parts: [{ text: ISTRUZIONI }] },
    // Gemini chiama "model" quello che Claude chiama "assistant".
    contents: storia.map((m) => ({
      role: m.role === 'assistant' ? 'model' : 'user',
      parts: [{ text: m.content }],
    })),
    generationConfig: { maxOutputTokens: 1000 },
  };

  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-goog-api-key': config.GEMINI_API_KEY,
    },
    body: JSON.stringify(corpo),
    signal: AbortSignal.timeout(TEMPO_MASSIMO_MS),
  });

  if (!res.ok) {
    throw new Error('Gemini ha risposto con errore ' + res.status + ': ' + (await res.text()));
  }

  const dati = await res.json();
  const parti = dati.candidates?.[0]?.content?.parts ?? [];
  return parti.map((p) => p.text ?? '').join(' ').trim();
}

// Toglie i simboli che Alexa leggerebbe male (asterischi, cancelletti, ecc.).
function pulisciPerLaVoce(testo) {
  return testo
    .replace(/[*#_`>]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

async function chiedi(storia) {
  const testo =
    config.MODELLO === 'claude' ? await chiediAClaude(storia) : await chiediAGemini(storia);
  return pulisciPerLaVoce(testo) || 'Non ho trovato una risposta, prova a chiedermelo in un altro modo.';
}

module.exports = { chiedi };
