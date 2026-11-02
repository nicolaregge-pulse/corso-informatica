# Mastermind bello (client per la 3INF)

Versione 1.0 - 02/11/2026 - Lazarus / Free Pascal. Lezione prevista: giovedì 05/11.

**Questa è l'UNICA versione del client da dare ai ragazzi.** I client precedenti (`classe-3/mastermind-2/client-unico` e i file `client_unit.pas` e `unit1_client.pas`) sono SUPERATI: restano nel repository solo come storico, non vanno distribuiti.

Un solo progetto Lazarus, tutto nella stessa cartella: `MastermindBello.lpi`, `MastermindBello.lpr`, `unit1.pas` e `unit1.lfm`. Una finestra e una unit, nello stile dei progetti che fate di solito. Nessuna immagine esterna: la tavola di legno, i buchi, i pioli e i piolini si disegnano nel programma. Funziona da solo («Gioca da solo») o collegato al server del prof («Connetti»), senza cambiare programma.

## Come si apre (per il prof, da provare in aula)

1. Copia l'intera cartella `mastermind-3-bello` in `Documenti\Lazarus\`.
2. Apri `MastermindBello.lpi` con Lazarus e premi F9.
3. **Non provato con la vera Lazarus:** i file `.lpi` e `.lpr` sono scritti a mano (copiati dalla struttura del modello Lazarus) e vanno controllati alla prima apertura.

## Come cambiare l'IP del server

L'IP del server è nella casella «IP del server», in alto a sinistra nella finestra: si scrive lì, senza toccare il codice. Il valore di partenza (`192.168.38.70`, il PC del prof) è nel file `unit1.lfm`, alla riga `Text = '192.168.38.70'` dentro `EdIp`. La porta è la 5050 e non si cambia.

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
