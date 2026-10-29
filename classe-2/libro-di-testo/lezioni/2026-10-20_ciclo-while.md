# Il ciclo WHILE: lancia il dado finché…

**Versione 1.0** — 29/10/2026
*Libro parziale della 2INF: la lezione del 20/10/2026. Fa parte del libro di testo della classe (libro-classe2). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 20/10/2026, 2 ore, Laboratorio.
2. **Argomenti:** Ciclo WHILE in Lazarus («ripeti finché»): teoria, ripasso, gioco del dado (lancia finché esce il numero magico e conta i tiri), ciclo infinito e come fermarlo; verifica.

### La teoria e l'esercitazione

### Le schede della lezione

#### 1. Dal FOR al WHILE: quando non sai quante volte

<div class="scheda">Con il <b>for</b> sai prima quanti giri fai: <code>for x := 1 to 10 do</code> fa 10 giri, sempre.<br>Ma se lanci un dado finché esce il 6, <b>quante volte lo lanci?</b> Non lo sa nessuno: magari 1, magari 15.<br>Per questo c'è il <b>while</b>: «<b>finché</b> la condizione è vera, ripeti». Si ferma quando la condizione diventa falsa.<br>Nella vita: <i>finché</i> ho fame, mangio; <i>finché</i> il semaforo è rosso, aspetto.</div>

#### 2. Come si scrive

<div class="scheda"><pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">while condizione do begin   istruzioni da ripetere; end;</pre>Si legge: <b>finché</b> la condizione è vera, <b>fai</b> quello che c'è tra begin ed end.<br>La condizione si controlla <b>prima</b> di ogni giro. Se è falsa già all'inizio, il while non fa <b>nessun</b> giro.<br>Le condizioni sono quelle dell'IF: <code>=</code> uguale, <code>&lt;&gt;</code> diverso, <code>&lt;</code> minore, <code>&gt;</code> maggiore, <code>&lt;=</code>, <code>&gt;=</code>.<br>Esempio: conta da 1 a 5 con il while:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">x := 1; while x &lt;= 5 do begin   Memo1.Lines.Add(IntToStr(x));   x := x + 1; end;</pre>Nel for il contatore aumenta da solo; nel while <b>lo fai aumentare tu</b> (<code>x := x + 1</code>).</div>

#### 3. Il pericolo: il ciclo infinito

<div class="scheda">Se dentro il while niente cambia la condizione, il ciclo <b>non finisce mai</b>:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">x := 1; while x &lt;= 5 do begin   Memo1.Lines.Add(IntToStr(x)); end;</pre>Qui manca <code>x := x + 1</code>: x resta 1 per sempre e il programma si <b>blocca</b>.<br>Se ti succede: in Lazarus menu <b>Esegui → Ferma</b> (oppure <b>Ctrl+F2</b>). Succede a tutti i programmatori, anche ai pro: si ferma e si corregge.<br>Regola: dentro il while deve sempre esserci qualcosa che <b>prima o poi</b> rende falsa la condizione.</div>

#### 4. Il dado: Random

<div class="scheda">Per tirare un dado il computer usa i <b>numeri a caso</b>:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">Randomize; dado := Random(6) + 1;</pre><b>Randomize</b> «mescola» i numeri: si scrive una volta all'inizio, altrimenti esce sempre la stessa sequenza.<br><b>Random(6)</b> dà un numero da <b>0 a 5</b>; con <b>+ 1</b> diventa da <b>1 a 6</b>, come un dado vero.<br>Per una moneta: <code>Random(2)</code> dà 0 o 1 (testa o croce).</div>

#### 5. Il programma: lancia finché esce il numero magico

<div class="scheda">L'interfaccia: in alto <b>Numero magico (1-6)</b> [ 6 ], al centro un Memo grande, in basso un bottone <b>Lancia!</b>. Il codice del bottone, con i rientri giusti:<pre style="background:#f3f5f8;color:#111;border-radius:8px;padding:10px 12px;font-size:16px;line-height:1.5;white-space:pre;overflow-x:auto">var dado, magico, tiri: integer; begin   Randomize;   magico := StrToInt(Edit1.Text);   Memo1.Clear;   tiri := 0;   dado := 0;   while dado &lt;&gt; magico do   begin     dado := Random(6) + 1;     tiri := tiri + 1;     Memo1.Lines.Add('Tiro ' + IntToStr(tiri) + ': ' + IntToStr(dado));   end;   Memo1.Lines.Add('Uscito il ' + IntToStr(magico) + ' dopo ' + IntToStr(tiri) + ' tiri!'); end;</pre>Leggilo: prendo il numero magico dalla casella; tiri parte da 0; <b>finché</b> il dado è <b>diverso</b> dal numero magico, tiro il dado, conto il tiro e lo scrivo nel Memo. Quando esce, scrivo dopo quanti tiri.<br>Perché <code>dado := 0</code> prima del while? Perché all'inizio il dado non è ancora uscito: 0 è diverso da qualsiasi numero magico, quindi il primo giro si fa sempre.</div>

#### 6. LA PRATICA, passi 1-5: il form

<div class="scheda">Un passo alla volta.<br>1) Apri Lazarus: <b>Progetto → Nuovo progetto → Applicazione → Ok</b>.<br>2) Metti un <b>TLabel</b> con Caption <b>Numero magico (1-6)</b>.<br>3) Accanto un <b>TEdit</b> (Edit1): nella proprietà <b>Text</b> scrivi <b>6</b>.<br>4) Al centro un <b>TMemo</b> grande con <b>ScrollBars = ssBoth</b>; cancella le righe di <b>Lines</b>.<br>5) In basso un <b>TButton</b> con Caption <b>Lancia!</b>.</div>

#### 7. LA PRATICA, passi 6-9: il codice e la prova

<div class="scheda">6) <b>Doppio clic</b> sul bottone: si apre <code>procedure TForm1.Button1Click</code>.<br>7) Scrivi il codice della scheda 5, riga per riga, con i rientri di 2 spazi. La riga <code>var dado, magico, tiri: integer;</code> va <b>sopra</b> il begin.<br>8) Premi <b>F9</b>.<br>9) Premi <b>Lancia!</b> più volte: ogni volta i tiri sono diversi. <b>FATTO!</b><br>Prova: scrivi <b>9</b> nella casella e premi Lancia!. Che cosa succede? (Scheda 3: Esegui → Ferma.)</div>

#### 8. Fallo tuo, gli errori e la sfida

<div class="scheda"><b>Fallo tuo</b>: cambia le frasi nel Memo (per esempio <code>'Ce l''hai fatta in '</code>), il titolo della finestra (Caption del form) e il colore del form.<br><b>Tieni pronto il codice per la verifica</b>: seleziona dalla riga <code>var</code> all'ultimo <code>end;</code>, <b>Ctrl+C</b>; nella verifica c'è una domanda dove lo incolli.<br><b>Errori tipici</b>: manca <code>Randomize</code> (escono sempre gli stessi tiri); manca <code>tiri := tiri + 1</code> (dice sempre 0 tiri); <code>while dado = magico</code> invece di <code>&lt;&gt;</code> (non fa nessun giro); numero magico 9 (ciclo infinito).<br><b>Sfida</b>: due dadi, finché escono <b>due 6</b> insieme (<code>while (d1 &lt;&gt; 6) or (d2 &lt;&gt; 6) do</code>). Quanti tiri servono?</div>


## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
