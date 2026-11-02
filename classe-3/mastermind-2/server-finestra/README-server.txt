MASTERMIND 2.0 - SERVER CON LA FINESTRA (per il prof) - README
Tutto con il mouse. Nessuna riga di comando.

Questa cartella contiene il server in versione "a finestra": sostituisce il vecchio
server nero a console (server_mastermind.pas), che non serve piu'.

FILE DI QUESTA CARTELLA
  unit1_server.pas   il codice della finestra (si incolla in Unit1)
  unit1_server.lfm   il disegno della finestra (si incolla con "Visualizza form come testo")
  mm_logica.pas      il cervello del gioco (identico a quello dei ragazzi)
  mm_file.pas        il modo "file" (identico)
  mm_tcp_poll.pas    la rete SENZA thread + il calcolo dell'IP (nuovo)
  (la cartella "test" serve solo a chi vuole rifare le prove: non serve per giocare.
   Il file mm_tcp.pas NON serve al server a finestra.)

PASSO 1 - Crea il progetto (una volta, sul tuo PC)
 1. Apri Lazarus. Menu File > Nuovo... > Progetto > Applicazione > OK.
 2. Menu File > Salva tutto. Scegli una cartella nuova (es. Mastermind-server) e
    salva con i nomi proposti: project1 e unit1.
 3. Apri Esplora file. Copia dentro QUELLA cartella i 3 file: mm_logica.pas,
    mm_file.pas, mm_tcp_poll.pas. (Non c'e' bisogno di aggiungerli al progetto:
    Lazarus li trova da solo perche' sono nella stessa cartella.)

PASSO 2 - Incolla il codice (.pas)
 1. Apri unit1_server.pas col Blocco note (clic destro > Apri con > Blocco note):
    Ctrl+A poi Ctrl+C.
 2. In Lazarus clicca sulla scheda "Unit1" (il testo del codice).
    Ctrl+A poi Ctrl+V.

PASSO 3 - Incolla la finestra (.lfm)
 1. Apri unit1_server.lfm col Blocco note: Ctrl+A poi Ctrl+C.
 2. In Lazarus premi F12 per vedere la finestra grigia (Form1). Clicca sulla
    finestra con il tasto DESTRO e scegli "Visualizza form come testo"
    (se la voce e' diversa, cerca "come testo"/"as text").
    Ctrl+A poi Ctrl+V.
 3. Clic destro > "Visualizza come form": compare la finestra del server, con
    la porta, i bottoni, la classifica e il registro.
 4. Menu File > Salva tutto.

PASSO 4 - Avvia
 1. Premi F9. Si apre la finestra "Mastermind 2.0 - SERVER del prof".
 2. Se Windows chiede "Consenti accesso" (firewall), clicca "Consenti accesso".
 3. Clicca "Avvia server". Il registro scrive "Server acceso sulla porta 5050".
    La combinazione segreta e' gia' scelta (nascosta). Se vuoi vederla, clicca la
    scritta "Combinazione segreta" (un altro clic la nasconde).
 4. Guarda la casella "Da dire ai ragazzi": c'e' scritto IP:5050. I ragazzi lo
    scrivono nella prima casella del loro programma. Per copiarlo: clicca nella
    casella, Ctrl+A, Ctrl+C.
 5. Quando i ragazzi compaiono nella classifica ("collegato, non ha ancora provato"),
    clicca "Via!". Da quel momento i tentativi contano.
 6. Per ricominciare: "Nuova combinazione" (chiede conferma se la partita e' in corso),
    poi di nuovo "Via!".

COSA SI VEDE NELLA FINESTRA
  Registro: ogni collegamento e ogni tentativo, con l'ora; le vittorie con ***.
  Classifica: posto, nome, tentativi, stato (HA VINTO / sta provando / collegato).
  A pari tentativi e pari secondi il posto e' lo stesso (pari merito).
  "Giocatori collegati": chi si e' fatto sentire negli ultimi 20 secondi.

COME VEDERE L'IP SENZA RIGA DI COMANDO (se la finestra non lo ricava)
  Windows 10/11: Impostazioni > Rete e Internet > (Wi-Fi o Ethernet) > clicca sulla
  rete collegata > in fondo "Indirizzo IPv4". E' un numero tipo 192.168.10.5.
  Poi scrivi tu nella casella dei ragazzi: IP:5050 (i due punti e la porta).
  Se il PC ha piu' schede di rete (Wi-Fi + cavo, VPN) l'IP mostrato potrebbe essere
  quello sbagliato: confrontalo con quello di Impostazioni.

PERCHE' NIENTE THREAD
  Il vecchio server usava un thread (un "secondo cuoco") per la rete. Qui non serve:
  il Timer1 della finestra chiama la rete ogni 50 millisecondi, il server risponde a
  chi sta bussando (fino a 12 richieste per giro) e restituisce subito la finestra.
  Ogni richiesta dura pochi millisecondi, quindi 22 ragazzi che chiedono ogni 3 secondi
  non si accorgono di niente. Se un PC "muto" si collega e non dice niente, la finestra
  aspetta al massimo mezzo secondo e va avanti.
  Se la porta 5050 e' occupata (un altro server gia' acceso) il programma lo dice:
  cambia la porta (es. 5051) e riprova; ai ragazzi dai IP:5051.

MODO FILE
  Resta attivo in parallelo: il server rilegge ogni 2 secondi la cartella "partita"
  accanto al programma e riscrive partita.txt e ranking.txt (utile se la rete e'
  bloccata). Nessuna impostazione da fare.

COSA E' STATO VERIFICATO E COSA NO (onesta')
  Verificato con fpc 3.2.2 su Linux: unit1_server.pas compila contro FINTE unita'
  LCL (cartella test/stub_lcl_server) e, pilotata da un programma che fa le veci di
  Lazarus, risponde a 22 e a 30 client veri (script Python, rete localhost):
  tutti vincono sulla stessa combinazione, nessun errore, risposta max 0,2 s.
  Porta occupata: messaggio corretto. La sintassi del .lfm e' controllata con
  ObjectTextToBinary di FPC.
  NON verificato: apertura in Lazarus vero (nessun Lazarus qui), il disegno reale
  della finestra, TStringGrid/TMemo/TTimer della vera LCL, il comportamento su
  Windows (firewall, calcolo IP su Windows). Se Lazarus segnala una proprieta'
  sconosciuta nel .lfm, clicca "Ignora": in genere la finestra si apre lo stesso e
  la proprieta' si sistema dall'Ispettore oggetti.
  Per rifare le prove: bash test/prova_finestra.sh 22   (serve fpc e python3).
