// Classe 2 — "Cosa scrive il programma?": if / then / else e if annidati in Lazarus.
// Ogni domanda è una funzione: i numeri cambiano per ogni allievo (generatore personale r).
function tra(r, a, b) { return a + Math.floor(r() * (b - a + 1)); }
function opz(giusta, altre) {             // la giusta in posizione 0, poi le altre senza doppioni
  var o = [giusta]; altre.forEach(function (x) { if (o.indexOf(x) < 0) o.push(x); }); return { o: o, a: 0 };
}
function D(codice, giusta, altre, domanda) {
  var x = opz(giusta, altre);
  return { q: domanda || "Cosa scrive il programma in <b>Label1</b>?", codice: codice, o: x.o, a: x.a };
}
window.BANCA = {
  titolo: "Cosa scrive il programma? (if)",
  sotto: "Classe 2 · Lazarus · ognuno ha i suoi numeri · ripasso: <a href='../2inf-if/'>dispensa if annidati</a>",
  regola: "Leggi il codice <b>come il computer</b>: guarda il valore della variabile, controlla la condizione dell'<b>if</b>: "
        + "se è <b>vera</b> esegui il blocco dopo <b>then</b>, se è <b>falsa</b> quello dopo <b>else</b>. Negli if annidati entra nel blocco giusto e ripeti. "
        + "Fai i conti sul foglio.",
  quante: 10,
  domande: [
    function (r) { var n = tra(r, 10, 99);
      return D("numero := " + n + ";\nif numero mod 2 = 0 then\n  begin\n    Label1.Caption := 'PARI';\n  end\nelse\n  begin\n    Label1.Caption := 'DISPARI';\n  end;",
        n % 2 == 0 ? "PARI" : "DISPARI", ["PARI", "DISPARI", "niente: errore"]); },
    function (r) { var n = [tra(r, 1, 50), -tra(r, 1, 50), 0][tra(r, 0, 2)];
      return D("numero := " + n + ";\nif numero > 0 then\n  begin\n    Label1.Caption := 'POSITIVO';\n  end\nelse\n  begin\n    if numero < 0 then\n      begin\n        Label1.Caption := 'NEGATIVO';\n      end\n    else\n      begin\n        Label1.Caption := 'ZERO';\n      end;\n  end;",
        n > 0 ? "POSITIVO" : (n < 0 ? "NEGATIVO" : "ZERO"), ["POSITIVO", "NEGATIVO", "ZERO"]); },
    function (r) { var v = tra(r, 3, 10);
      return D("voto := " + v + ";\nif voto < 6 then\n  begin\n    Label1.Caption := 'Insufficiente';\n  end\nelse\n  begin\n    if voto < 8 then\n      begin\n        Label1.Caption := 'Sufficiente';\n      end\n    else\n      begin\n        Label1.Caption := 'Ottimo!';\n      end;\n  end;",
        v < 6 ? "Insufficiente" : (v < 8 ? "Sufficiente" : "Ottimo!"), ["Insufficiente", "Sufficiente", "Ottimo!"]); },
    function (r) { var e = tra(r, 8, 25);
      return D("eta := " + e + ";\nif eta < 14 then\n  begin\n    Label1.Caption := 'Bambino';\n  end\nelse\n  begin\n    if eta < 18 then\n      begin\n        Label1.Caption := 'Ragazzo';\n      end\n    else\n      begin\n        Label1.Caption := 'Maggiorenne';\n      end;\n  end;",
        e < 14 ? "Bambino" : (e < 18 ? "Ragazzo" : "Maggiorenne"), ["Bambino", "Ragazzo", "Maggiorenne"]); },
    function (r) { var s = tra(r, 20, 80), n = [s, s - tra(r, 1, 15), s + tra(r, 1, 15)][tra(r, 0, 2)];
      return D("segreto := " + s + ";\nnumero := " + n + ";\nif numero = segreto then\n  begin\n    Label1.Caption := 'Indovinato!';\n  end\nelse\n  begin\n    if numero < segreto then\n      begin\n        Label1.Caption := 'Troppo BASSO';\n      end\n    else\n      begin\n        Label1.Caption := 'Troppo ALTO';\n      end;\n  end;",
        n == s ? "Indovinato!" : (n < s ? "Troppo BASSO" : "Troppo ALTO"), ["Indovinato!", "Troppo BASSO", "Troppo ALTO"]); },
    function (r) { var a = tra(r, 1, 20), b = tra(r, 1, 20);
      return D("a := " + a + ";\nb := " + b + ";\nif a > b then\n  begin\n    Label1.Caption := IntToStr(a);\n  end\nelse\n  begin\n    Label1.Caption := IntToStr(b);\n  end;",
        String(Math.max(a, b)), [String(a), String(b), String(a + b)], "Cosa scrive il programma? (scrive il numero più grande)"); },
    function (r) { var t = tra(r, 1, 9);
      return D("tentativi := " + t + ";\nif tentativi > 7 then\n  begin\n    Label1.Caption := 'Hai perso!';\n  end\nelse\n  begin\n    Label1.Caption := 'Riprova';\n  end;",
        t > 7 ? "Hai perso!" : "Riprova", ["Hai perso!", "Riprova"]); },
    function (r) { var n = tra(r, -20, 120);
      var g = (n < 1 || n > 100) ? "Solo numeri da 1 a 100!" : "OK";
      return D("numero := " + n + ";\nif (numero < 1) or (numero > 100) then\n  begin\n    Label1.Caption := 'Solo numeri da 1 a 100!';\n  end\nelse\n  begin\n    Label1.Caption := 'OK';\n  end;",
        g, ["Solo numeri da 1 a 100!", "OK"], "Cosa scrive il programma? (<b>or</b> = basta che UNA condizione sia vera)"); },
    function (r) { var t = tra(r, 10, 40);
      return D("temperatura := " + t + ";\nif temperatura >= 30 then\n  begin\n    Label1.Caption := 'Caldo';\n  end\nelse\n  begin\n    if temperatura >= 18 then\n      begin\n        Label1.Caption := 'Bello';\n      end\n    else\n      begin\n        Label1.Caption := 'Fresco';\n      end;\n  end;",
        t >= 30 ? "Caldo" : (t >= 18 ? "Bello" : "Fresco"), ["Caldo", "Bello", "Fresco"]); },
    function (r) { var e = tra(r, 3, 70);
      var g = e < 6 ? "Gratis" : (e < 65 ? "8 euro" : "5 euro");
      return D("eta := " + e + ";\nif eta < 6 then\n  begin\n    Label1.Caption := 'Gratis';\n  end\nelse\n  begin\n    if eta < 65 then\n      begin\n        Label1.Caption := '8 euro';\n      end\n    else\n      begin\n        Label1.Caption := '5 euro';\n      end;\n  end;",
        g, ["Gratis", "8 euro", "5 euro"], "Il cinema: quanto costa il biglietto?"); },
    function () {
      return { q: "Dove va il punto e virgola? Quale versione è <b>giusta</b>?", fisse: false,
        o: ["  end\nelse — l'end prima di else SENZA ;", "  end;\nelse — l'end prima di else CON ;", "else;  — il ; dopo else", "nessun ; in tutto l'if"], a: 0 }; },
    function () {
      return { q: "Regola dei rientri del corso: quale frase è <b>giusta</b>?",
        o: ["if ed else allineati; begin ed end allineati; il resto più a destra", "tutto attaccato a sinistra", "else più a destra dell'if", "end più a destra del suo begin"], a: 0 }; }
  ]
};
