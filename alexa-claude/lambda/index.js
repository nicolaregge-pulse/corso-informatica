// index.js — il "cervello" della skill Alexa.
// Alexa ci manda la frase detta; noi la giriamo all'IA e facciamo leggere la risposta.

const Alexa = require('ask-sdk-core');
const { chiedi } = require('./ia');

// Quanti scambi (domanda + risposta) ricordare durante una conversazione.
const MAX_SCAMBI_RICORDATI = 6;
const RIPROPOSTA = 'Hai altre domande?';

// Alexa legge il testo come SSML: alcuni simboli vanno "neutralizzati".
function perSSML(testo) {
  return testo.replace(/&/g, ' e ').replace(/</g, ' minore di ').replace(/>/g, ' maggiore di ');
}

// "Alexa, apri il mio assistente"
const AvvioHandler = {
  canHandle(input) {
    return Alexa.getRequestType(input.requestEnvelope) === 'LaunchRequest';
  },
  handle(input) {
    return input.responseBuilder
      .speak('Ciao! Sono pronto. Fammi una domanda, per esempio: dimmi perché il cielo è blu.')
      .reprompt('Dimmi pure la tua domanda.')
      .getResponse();
  },
};

// "dimmi ...", "chiedi ...", "spiegami ..." — la domanda vera e propria.
const DomandaHandler = {
  canHandle(input) {
    return (
      Alexa.getRequestType(input.requestEnvelope) === 'IntentRequest' &&
      Alexa.getIntentName(input.requestEnvelope) === 'DomandaIntent'
    );
  },
  async handle(input) {
    const domanda = Alexa.getSlotValue(input.requestEnvelope, 'domanda');
    if (!domanda) {
      return input.responseBuilder
        .speak('Non ho capito la domanda. Puoi ripeterla?')
        .reprompt('Dimmi pure la tua domanda.')
        .getResponse();
    }

    // La "storia" della conversazione vive solo finché la sessione Alexa resta aperta.
    const attributi = input.attributesManager.getSessionAttributes();
    const storia = attributi.storia || [];
    storia.push({ role: 'user', content: domanda });

    let risposta;
    try {
      risposta = await chiedi(storia);
    } catch (errore) {
      console.error('Errore IA:', errore);
      storia.pop(); // la domanda senza risposta non va ricordata
      attributi.storia = storia;
      input.attributesManager.setSessionAttributes(attributi);
      const lento = errore.name === 'TimeoutError' || /timed? ?out/i.test(String(errore.message));
      const frase = lento
        ? 'Ci sto mettendo troppo a pensare. Prova con una domanda più breve.'
        : 'Scusa, in questo momento non riesco a collegarmi. Riprova tra poco.';
      return input.responseBuilder.speak(frase).reprompt(RIPROPOSTA).getResponse();
    }

    storia.push({ role: 'assistant', content: risposta });
    attributi.storia = storia.slice(-MAX_SCAMBI_RICORDATI * 2);
    input.attributesManager.setSessionAttributes(attributi);

    return input.responseBuilder.speak(perSSML(risposta)).reprompt(RIPROPOSTA).getResponse();
  },
};

const AiutoHandler = {
  canHandle(input) {
    return (
      Alexa.getRequestType(input.requestEnvelope) === 'IntentRequest' &&
      Alexa.getIntentName(input.requestEnvelope) === 'AMAZON.HelpIntent'
    );
  },
  handle(input) {
    return input.responseBuilder
      .speak(
        'Puoi farmi qualsiasi domanda iniziando con dimmi, spiegami o chiedi. ' +
          'Per esempio: spiegami come funziona un arcobaleno. Per uscire di\' stop.'
      )
      .reprompt('Dimmi pure la tua domanda.')
      .getResponse();
  },
};

const StopHandler = {
  canHandle(input) {
    if (Alexa.getRequestType(input.requestEnvelope) !== 'IntentRequest') return false;
    const nome = Alexa.getIntentName(input.requestEnvelope);
    return nome === 'AMAZON.StopIntent' || nome === 'AMAZON.CancelIntent' || nome === 'AMAZON.NoIntent';
  },
  handle(input) {
    return input.responseBuilder.speak('Va bene, a presto! Buonanotte.').withShouldEndSession(true).getResponse();
  },
};

// Quando Alexa non riconosce la frase come domanda.
const FallbackHandler = {
  canHandle(input) {
    return (
      Alexa.getRequestType(input.requestEnvelope) === 'IntentRequest' &&
      Alexa.getIntentName(input.requestEnvelope) === 'AMAZON.FallbackIntent'
    );
  },
  handle(input) {
    return input.responseBuilder
      .speak('Non ho capito. Prova a iniziare la domanda con dimmi, oppure spiegami.')
      .reprompt('Dimmi pure la tua domanda.')
      .getResponse();
  },
};

const FineSessioneHandler = {
  canHandle(input) {
    return Alexa.getRequestType(input.requestEnvelope) === 'SessionEndedRequest';
  },
  handle(input) {
    return input.responseBuilder.getResponse();
  },
};

const ErroreHandler = {
  canHandle() {
    return true;
  },
  handle(input, errore) {
    console.error('Errore skill:', errore);
    return input.responseBuilder
      .speak('Scusa, qualcosa è andato storto. Riprova.')
      .reprompt(RIPROPOSTA)
      .getResponse();
  },
};

exports.handler = Alexa.SkillBuilders.custom()
  .addRequestHandlers(
    AvvioHandler,
    DomandaHandler,
    AiutoHandler,
    StopHandler,
    FallbackHandler,
    FineSessioneHandler
  )
  .addErrorHandlers(ErroreHandler)
  .lambda();
