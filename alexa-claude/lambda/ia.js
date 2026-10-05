// ia.js — manda la domanda al modello scelto (Claude o Gemini) e restituisce
// il testo della risposta, già pronto da far leggere ad Alexa.
//
// Usa il modulo "https" incluso in Node.js (niente librerie esterne), perché le
// skill ospitate da Alexa possono girare su versioni di Node.js vecchie (16),
// dove l'SDK ufficiale di Anthropic e "fetch" non sono disponibili.

const https = require('https');
const config = require('./config');

// Istruzioni fisse per il modello: risposte brevi, parlate, in italiano.
const ISTRUZIONI =
  "Sei un assistente vocale che risponde tramite un altoparlante Alexa, in italiano. " +
  "La risposta verrà letta ad alta voce: niente elenchi puntati, niente markdown, " +
  "niente emoji, niente link. Rispondi in modo naturale e breve: al massimo tre o " +
  "quattro frasi, salvo che l'utente chieda esplicitamente di più. " +
  "Latency-sensitive; begin your visible answer immediately.";

// Alexa aspetta circa 8 secondi in tutto (avvio della skill compreso):
// ci fermiamo molto prima, così Alexa riesce sempre a dire qualcosa.
const TEMPO_MASSIMO_MS = 5500;

// Fa una richiesta POST con corpo JSON e restituisce la risposta JSON.
function postJSON(url, intestazioni, corpo) {
  return new Promise((risolvi, rifiuta) => {
    const dati = JSON.stringify(corpo);
    const richiesta = https.request(
      url,
      {
        method: 'POST',
        headers: Object.assign(
          { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(dati) },
          intestazioni
        ),
        timeout: TEMPO_MASSIMO_MS,
      },
      (risposta) => {
        let testo = '';
        risposta.setEncoding('utf8');
        risposta.on('data', (pezzo) => (testo += pezzo));
        risposta.on('end', () => {
          if (risposta.statusCode < 200 || risposta.statusCode >= 300) {
            return rifiuta(new Error('Errore ' + risposta.statusCode + ' da ' + url + ': ' + testo));
          }
          try {
            risolvi(JSON.parse(testo));
          } catch (e) {
            rifiuta(e);
          }
        });
      }
    );
    richiesta.on('timeout', () => {
      const errore = new Error('timeout');
      errore.name = 'TimeoutError';
      richiesta.destroy(errore);
    });
    richiesta.on('error', rifiuta);
    richiesta.write(dati);
    richiesta.end();
  });
}

async function chiediAClaude(storia) {
  // Haiku è il modello più veloce, ma non accetta "effort" né i "fallbacks".
  const veloce = config.CLAUDE_MODEL.indexOf('haiku') !== -1;

  const intestazioni = {
    'x-api-key': config.CLAUDE_API_KEY,
    'anthropic-version': '2023-06-01',
  };
  const corpo = {
    model: config.CLAUDE_MODEL,
    max_tokens: veloce ? 500 : 2000,
    system: ISTRUZIONI,
    messages: storia,
  };
  if (!veloce) {
    corpo.output_config = { effort: 'low' }; // risposte veloci, adatte alla voce
    // Se il modello rifiuta una richiesta, l'API riprova da sola con un altro modello.
    intestazioni['anthropic-beta'] = 'server-side-fallback-2026-07-01';
    corpo.fallbacks = 'default';
  }

  const risposta = await postJSON('https://api.anthropic.com/v1/messages', intestazioni, corpo);

  if (risposta.stop_reason === 'refusal') {
    return 'Mi dispiace, a questa domanda non posso rispondere.';
  }

  return (risposta.content || [])
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

  const dati = await postJSON(
    url,
    { 'x-goog-api-key': config.GEMINI_API_KEY },
    {
      systemInstruction: { parts: [{ text: ISTRUZIONI }] },
      // Gemini chiama "model" quello che Claude chiama "assistant".
      contents: storia.map((m) => ({
        role: m.role === 'assistant' ? 'model' : 'user',
        parts: [{ text: m.content }],
      })),
      generationConfig: { maxOutputTokens: 1000 },
    }
  );

  const candidato = (dati.candidates || [])[0];
  const parti = (candidato && candidato.content && candidato.content.parts) || [];
  return parti.map((p) => p.text || '').join(' ').trim();
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
