# Mastermind bello (client per la 3INF)

Versione 1.0 - 02/11/2026 - Lazarus / Free Pascal. Lezione prevista: giovedì 05/11.

Un solo file di codice (`unit1.pas`) e il suo `unit1.lfm`, come il client di oggi. Nessuna immagine esterna: la tavola di legno, i buchi, i pioli e i piolini si disegnano nel programma.

## Come si gioca

1. Clicca i colori della colonna a destra: si riempiono i 4 buchi della riga illuminata. I colori possono ripetersi.
2. Premi **Prova**. Con **Togli l'ultimo** correggi.
3. Piolino piccolo **nero** = colore giusto al posto giusto. **Bianco** = colore giusto al posto sbagliato.

## Due modi

| Bottone | Che cosa fa |
|---|---|
| Gioca da solo | il programma pensa il codice, non serve la rete |
| Connetti | ti colleghi al PC del prof (stessa porta 5050 e stesso protocollo del Mastermind di oggi: i neri sono le «esatte», i bianchi le «spostate») |

Il server del prof non cambia: `classe-3/mastermind-2/server-unico` funziona con questo client.

## Prove fatte (nel container, senza Lazarus)

`bash test/prova_bello.sh` compila il vero `unit1.pas` con finte unità LCL (`test/stub_lcl`) e prova il conteggio neri/bianchi (anche colori ripetuti, tutte le 1296 x 1296 coppie), la partita da soli con il controllo dei piolini disegnati e la rete contro il server vero. Non è la vera LCL: la finestra con la vera LCL va compilata in aula con Lazarus (F9).
