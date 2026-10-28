# Schemi da ricopiare sul quaderno: uguali in tutte e tre le lingue (presi da _build/lazarus.js, 28/10/2026).
SCHEMA1 = """+--------------------------------------------------+
| MENU:  File  Progetto  Esegui ...                |
| PALETTE: [Standard]  [OK] [abc] [A] ...          |
+------------+-------------------------------------+
| ISPETTORE  |                                     |
| OGGETTI    |   FORM1  (la mia finestra)          |
|            |    +-----------------+              |
| Proprieta  |    | Edit1           |  <- TEdit    |
|  Caption   |    +-----------------+              |
|  Text      |       [ Saluta ]       <- TButton   |
| Eventi     |                                     |
|  OnClick   |   (F12 = vado al codice)            |
+------------+-------------------------------------+
| MESSAGGI: errori e avvisi                        |
+--------------------------------------------------+"""
SCHEMA2 = """ciao\\                       <- UNA cartella = UN progetto
 |- ciao.lpi    progetto (+ opzioni)      TENERE
 |- ciao.lpr    programma principale      TENERE
 |- unit1.pas   il mio codice             TENERE
 |- unit1.lfm   com'e' fatta la finestra  TENERE
 |- ciao.lps    sessione                  si rifa'
 |- ciao.res    risorse (icona)           si rifa'
 |- ciao.ico    icona                     si rifa'
 |- ciao.exe    programma finito (F9)     si rifa'
 |- lib\\x86_64-win64\\
 |     .o .ppu .compiled .or (compilatore) si rifa'
 |- backup\\     copie di sicurezza        si butta"""
SCHEMA3 = """scrivo MARIO -> clic su [Saluta] -> OnClick -> Button1Click
   -> ShowMessage('Ciao ' + Edit1.Text) -> | Ciao MARIO  [OK] |"""
PROC = """procedure TForm1.Button1Click(Sender: TObject);
begin
  // qui scrivi la tua riga
end;"""
RIGA = "ShowMessage('Ciao ' + Edit1.Text);"
FOTO = 'immagini/20261028_lavagna-lazarus-ciao.jpg'
FOTO_FIN = 'immagini/20261028_lavagna-finestre-lazarus.jpg'
FOTO_FILE = 'immagini/20261028_lavagna-file-progetto.jpg'
