// 3INF 02/11/2026: controllo automatico del file unit1.pas (Mastermind ora 1 e 2, Slideshow ora 3).
// Dice con parole semplici se nel file ci sono i pezzi giusti. NON blocca MAI la consegna: è solo un aiuto.
// Lo stesso controllo, in Python, lo fa il cruscotto (riservato: generatori/cruscotto_3inf_mastermind.py). Uso: ControllaPas(testo, ora) -> {ok, voci:[{ok, it}], ora_trovata}
(function (g) {
  function pulisci(t) { return String(t || '').replace(/\{[^}]*\}/g, ' ').replace(/\(\*[\s\S]*?\*\)/g, ' ').replace(/\/\/[^\n]*/g, ' '); }
  function senzaScritte(t) { return t.replace(/'[^'\n]*'/g, "''"); }
  function voce(ok, it, solo_avviso) { return { ok: !!ok, avviso: !!solo_avviso, it: it }; }
  function oraTrovata(c) {
    if (/\bTTimer\b|\bTimer1Timer\b/i.test(c)) return 3;
    if (/\bTPageControl\b|\bspostate\b/i.test(c)) return 2;
    if (/\bRandomize\b|\bRandom\s*\(/i.test(c)) return 1;
    return 0;
  }
  var FACILE = {   // la riga del percorso facilitato di ogni ora; stesse regole in cruscotto_3inf_mastermind.py
    1: /\bLabel1\s*\.\s*Caption\s*:=[^;]*\bRandom\s*\(/i,          // Label1.Caption := IntToStr(Random(6) + 1);
    2: /\bMemo1\s*\.\s*Clear\b/i,                                    // Memo1.Clear; nel bottone Nuova partita
    3: /\bPanel1\s*\.\s*Caption\s*:=/i                               // Panel1.Caption := 'Seconda diapositiva';
  };
  function conta(re, t) { return (t.match(re) || []).length; }
  function ControllaPas(testo, ora) {
    var grezzo = String(testo || ''), c0 = pulisci(grezzo), c = senzaScritte(c0), V = [];
    var unita = /\bunit\s+\w+\s*;/i.test(c) && /\bimplementation\b/i.test(c) && /\bend\s*\.\s*$/i.test(c.trim());
    V.push(voce(unita, 'È un file di Lazarus (una unit in Pascal).'));
    if (!unita) {
      V.push(voce(false, 'Hai scelto il file giusto? Deve essere unit1.pas, nella cartella del progetto.'));
      return { ok: false, voci: V, ora_trovata: 0 };
    }
    var clic = /procedure\s+TForm1\s*\.\s*Button1Click\s*\(/i.test(c);
    V.push(voce(clic, 'C\'è il clic del bottone: Button1Click.'));
    if (ora === 1) {
      V.push(voce(/\bRandomize\b/i.test(c), 'C\'è Randomize: il computer mescola i numeri a caso.'));
      V.push(voce(/\bRandom\s*\(\s*\d+\s*\)/i.test(c), 'C\'è Random( … ): il codice segreto si sceglie a caso.'));
      V.push(voce(/\bMemo1\s*\.\s*Lines\s*\.\s*Add\s*\(/i.test(c), 'I tentativi vanno nel Memo: Memo1.Lines.Add( … ).'));
      V.push(voce(/\bEdit1\s*\.\s*Text\b/i.test(c), 'Il programma legge la casella: Edit1.Text.'));
      V.push(voce(/\bLabel1\s*\.\s*Caption\s*:=/i.test(c), 'Il risultato va nella scritta: Label1.Caption := …'));
    } else if (ora === 2) {
      V.push(voce(/\bPageControl1\s*:\s*TPageControl\b/i.test(c) && /\bTabSheet3\s*:\s*TTabSheet\b/i.test(c), 'Ci sono le 3 schede: PageControl1 con TabSheet1, 2 e 3.'));
      V.push(voce(/procedure\s+TForm1\s*\.\s*Button2Click\s*\(/i.test(c), 'C\'è il bottone Nuova partita: Button2Click.'));
      V.push(voce(/\besatte\b/i.test(c) && /\bspostate\b/i.test(c), 'Il programma conta le esatte e le spostate.'));
      V.push(voce(conta(/\bfor\s+\w+\s*:=\s*1\s+to\s+4\s+do/gi, c) >= 3, 'Ci sono almeno 3 cicli for … to 4 (azzera, esatte, spostate).'));
      V.push(voce(/\bMemo1\s*\.\s*Clear\b/i.test(c), 'La partita nuova svuota il Memo: Memo1.Clear.'));
      V.push(voce(/\bRandom\s*\(\s*\d+\s*\)/i.test(c), 'C\'è Random( … ): il codice segreto è a caso.', true));
    } else if (ora === 3) {
      V.push(voce(/\bTimer1\s*:\s*TTimer\b/i.test(c) && /procedure\s+TForm1\s*\.\s*Timer1Timer\s*\(/i.test(c), 'C\'è il timer: Timer1 e Timer1Timer.'));
      V.push(voce(/procedure\s+TForm1\s*\.\s*Button2Click\s*\(/i.test(c), 'C\'è il bottone Avanti: Button2Click.'));
      V.push(voce(/\bPanel1\s*\.\s*Caption\s*:=/i.test(c), 'La diapositiva cambia scritta: Panel1.Caption := …'));
      V.push(voce(/\bPanel1\s*\.\s*Color\s*:=/i.test(c), 'La diapositiva cambia colore: Panel1.Color := …', true));
      V.push(voce(/\bN\s*:=\s*N\s*[+-]\s*1\b/i.test(c), 'Il programma conta le diapositive: N := N + 1.'));
    }
    var errori = V.filter(function (v) { return !v.ok && !v.avviso; }).length, fac = false;
    if (errori > 0 && clic && FACILE[ora] && FACILE[ora].test(c)) {
      fac = true; V.forEach(function (v) { if (!v.ok) v.avviso = true; });
      V.push(voce(true, 'Percorso facilitato: il codice è giusto. Bravo! Le righe gialle sono per chi fa il percorso completo.'));
      errori = 0;
    }
    return { ok: errori === 0, facile: fac, voci: V, ora_trovata: oraTrovata(c) };
  }
  g.ControllaPas = ControllaPas;
  if (typeof module !== 'undefined') module.exports = ControllaPas;
})(typeof window !== 'undefined' ? window : globalThis);
