// config.example.js — MODELLO DI CONFIGURAZIONE (senza chiavi vere).
// Nella console Alexa: crea un file "config.js" accanto a index.js,
// incolla questo contenuto e metti le tue chiavi al posto dei puntini.
// Il file config.js NON va mai messo su GitHub (è già escluso da .gitignore).

module.exports = {
  // Quale IA usare: 'gemini' (chiave gratuita) oppure 'claude' (chiave di Guido).
  MODELLO: 'gemini',

  // Chiave Gemini: da aistudio.google.com, voce "Get API key".
  GEMINI_API_KEY: '...',
  GEMINI_MODEL: 'gemini-flash-lite-latest',

  // Chiave Claude: da console.anthropic.com (serve credito sull'organizzazione).
  CLAUDE_API_KEY: '...',
  CLAUDE_MODEL: 'claude-opus-5-5',
};
