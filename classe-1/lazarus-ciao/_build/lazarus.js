// 28/10/2026 1INF, Laboratorio (Nicola: «iniziamo a far vedere Lazarus: una Edit e un bottone, scrive il nome, preme e compare Ciao e il suo nome»).
// Teoria in schede IT/AR/ZH + esercitazione + consegna (Documento su Classroom con il codice e lo screenshot).
// Uso: node lazarus.js  →  docs/verifica/banche/1inf-lazarus-ciao.js (+ stato). Le foto della lavagna del prof vanno in FOTO (percorsi da docs/verifica/).
const fs = require('fs'), path = require('path'); const DOCS = path.join(__dirname, '../../../docs/');
const FOTO = JSON.parse(fs.existsSync(path.join(__dirname, 'foto.json')) ? fs.readFileSync(path.join(__dirname, 'foto.json'), 'utf8') : '{}');
const ar = t => '<p lang="ar" dir="rtl" style="color:#5b6573">' + t + '</p>', zh = t => '<p lang="zh" style="color:#5b6573">' + t + '</p>';
const k = t => '<code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">' + t + '</code>';
const box = t => '<pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">' + t + '</pre>';
const tab = (h, r) => '<div style="overflow-x:auto;max-width:100%"><table style="border-collapse:collapse;width:100%;margin:8px 0"><tr>' + h.map(x => '<th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">' + x + '</th>').join('') + '</tr>' +
  r.map(rr => '<tr>' + rr.map(x => '<td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">' + x + '</td>').join('') + '</tr>').join('') + '</table></div>';
const foto = n => (FOTO[n] || []).map(x => { const f = typeof x === 'string' ? x : x.f, d = typeof x === 'string' ? '' : (x.d || '');
  return '<p><img src="' + f + '" alt="foto della lavagna" style="max-width:100%;border-radius:10px;border:1px solid #d5dbe3"></p>' + (d ? '<p style="margin-top:-4px;font-style:italic">' + d + '</p>' : ''); }).join('');
const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const quaderno = t => '<p><b>Da ricopiare sul quaderno</b></p>' + box(esc(t));
const SCHEMA1 = "+--------------------------------------------------+\n| MENU:  File  Progetto  Esegui ...                |\n| PALETTE: [Standard]  [OK] [abc] [A] ...          |\n+------------+-------------------------------------+\n| ISPETTORE  |                                     |\n| OGGETTI    |   FORM1  (la mia finestra)          |\n|            |    +-----------------+              |\n| Proprieta  |    | Edit1           |  <- TEdit    |\n|  Caption   |    +-----------------+              |\n|  Text      |       [ Saluta ]       <- TButton   |\n| Eventi     |                                     |\n|  OnClick   |   (F12 = vado al codice)            |\n+------------+-------------------------------------+\n| MESSAGGI: errori e avvisi                        |\n+--------------------------------------------------+", SCHEMA2 = "ciao\\                       <- UNA cartella = UN progetto\n |- ciao.lpi    progetto (+ opzioni)      TENERE\n |- ciao.lpr    programma principale      TENERE\n |- unit1.pas   il mio codice             TENERE\n |- unit1.lfm   com'e' fatta la finestra  TENERE\n |- ciao.lps    sessione                  si rifa'\n |- ciao.res    risorse (icona)           si rifa'\n |- ciao.ico    icona                     si rifa'\n |- ciao.exe    programma finito (F9)     si rifa'\n |- lib\\x86_64-win64\\\n |     .o .ppu .compiled .or (compilatore) si rifa'\n |- backup\\     copie di sicurezza        si butta", SCHEMA3 = "scrivo MARIO -> clic su [Saluta] -> OnClick -> Button1Click\n   -> ShowMessage('Ciao ' + Edit1.Text) -> | Ciao MARIO  [OK] |";
const S = [];
S.push({ titolo: '1. Che cos\'è Lazarus · ١. ما هو Lazarus · 1. Lazarus 是什么',
  testo: '<div style="background:#fff4c2;border:2px solid #d4a017;border-radius:10px;padding:10px 12px;margin:0 0 12px"><p style="margin:0 0 6px"><b>Questa pagina cambia durante la lezione: ogni tanto premi F5 per vedere la versione nuova.</b></p>' + ar('<b>هذه الصفحة تتغيّر أثناء الدرس: اضغط F5 من وقت لآخر لترى النسخة الجديدة.</b>') + zh('<b>这个页面在上课时会变化：时不时按 F5，看最新的版本。</b>') + '</div>' +
    '<p><b>Lazarus</b> è un programma che serve a <b>creare altri programmi</b>, con le finestre e i bottoni, come quelli che usi ogni giorno. Funziona come i <b>mattoncini</b>: prendi un pezzo già pronto (un bottone, una casella), lo metti nella finestra e poi scrivi <b>che cosa deve fare</b>. Il linguaggio si chiama <b>Pascal</b>.</p>' +
    '<p>Oggi facciamo il primo programma di tutti i programmatori: il <b>«Ciao»</b>. Scrivi il tuo nome in una casella, premi un bottone e il programma ti saluta: <b>Ciao Ahmed</b>.</p>' +
    '<p>Per aprire Lazarus: doppio clic sull\'icona di Lazarus (il prof vi mostra dove si trova). Poi vai alla scheda 2: lì prepari il progetto nuovo e la tua cartella.</p>' + foto(1) +
    ar('Lazarus برنامج نصنع به برامج أخرى بنوافذ وأزرار. نأخذ قطعة جاهزة (زر، خانة) ونضعها في النافذة، ثم نكتب ماذا تفعل. اللغة اسمها Pascal. اليوم نصنع برنامج «Ciao» (مرحبًا): تكتب اسمك، تضغط الزر، فيقول لك البرنامج مرحبًا.') +
    zh('Lazarus 是用来做其他程序的软件，可以做有窗口和按钮的程序。像搭积木一样：拿一个现成的零件（按钮、输入框），放进窗口，再写它要做什么。语言叫 Pascal。今天做第一个程序「Ciao」（你好）：写名字，按按钮，程序就跟你打招呼。') });
S.push({ titolo: '2. Partenza pulita: nuovo progetto e cartella nuova · ٢. بداية نظيفة: مشروع جديد ومجلد جديد · 2. 干净的开始：新项目和新文件夹',
  testo: '<p>Prima di mettere i pezzi nella finestra prepariamo il posto giusto. <b>Un progetto = una cartella sola</b>: tutti i file del tuo programma stanno insieme, nella tua cartella. Così nessun file si perde e nessun file si mescola con quelli di un altro.</p>' +
    '<p>Fai un passo alla volta. Dopo ogni passo guarda lo schermo.</p>' +
    '<p><b>1.</b> In alto a sinistra in Lazarus clicca il menu <b>File</b>.</p>' +
    '<p><b>2.</b> Nel menu clicca <b>Chiudi tutto</b>. Così si chiudono i file rimasti aperti.</p>' +
    '<p><b>3.</b> Se Lazarus chiede di salvare un progetto vecchio, clicca <b>No</b>.</p>' +
    '<p><b>4.</b> In alto clicca il menu <b>Progetto</b>.</p>' +
    '<p><b>5.</b> Nel menu clicca <b>Chiudi progetto</b>. Se la voce è grigia, non si può cliccare: va bene così, vai al passo 6.</p>' +
    '<p><b>6.</b> Ora fai il progetto nuovo. In alto clicca il menu <b>Progetto</b>.</p>' +
    '<p><b>7.</b> Nel menu clicca <b>Nuovo progetto…</b>. Si apre una finestra con un elenco.</p>' +
    '<p><b>8.</b> Nell\'elenco a sinistra clicca <b>Applicazione</b>.</p>' +
    '<p><b>9.</b> In basso nella finestra clicca <b>OK</b>. Al centro compare la finestra vuota <b>Form1</b>.</p>' +
    '<p><b>10.</b> SUBITO si salva. In alto clicca il menu <b>Progetto</b>.</p>' +
    '<p><b>11.</b> Nel menu clicca <b>Salva progetto con nome…</b>. Si apre la finestra per salvare.</p>' +
    '<p><b>12.</b> In alto nella finestra clicca il bottone <b>Nuova cartella</b>. (Non lo vedi? Clic con il tasto destro su un punto vuoto della finestra → <b>Nuovo</b> → <b>Cartella</b>.)</p>' +
    '<p><b>13.</b> Scrivi il nome della cartella e premi ' + k('Invio') + ':</p>' + box('ciao') +
    '<p><b>14.</b> Fai <b>doppio clic</b> sulla cartella ' + k('ciao') + ' per entrarci. In alto ora c\'è scritto ' + k('ciao') + '.</p>' +
    '<p><b>15.</b> In basso, nella casella <b>Nome file</b>, scrivi il nome del progetto:</p>' + box('ciao.lpi') +
    '<p><b>16.</b> In basso a destra clicca <b>Salva</b>.</p>' +
    '<p><b>17.</b> Lazarus apre una seconda finestra: chiede il nome della <b>unit</b> (il file del codice). Nella casella <b>Nome file</b> lascia o scrivi:</p>' + box('unit1.pas') +
    '<p><b>18.</b> In basso a destra clicca <b>Salva</b>.</p>' +
    '<p><b>19.</b> Controlla: guarda in alto, nella barra del titolo di Lazarus. C\'è scritto ' + k('ciao') + '. FATTO: il tuo progetto ha la sua cartella!</p>' + foto(2) +
    ar('قبل أن نبدأ نجهّز المكان الصحيح: مشروع واحد = مجلد واحد، فلا يضيع أي ملف ولا يختلط بملفات زملائك. ١) قائمة «File» ثم «Chiudi tutto» (إغلاق الكل)؛ إذا سأل عن حفظ مشروع قديم اضغط «No». ٢) قائمة «Progetto» ثم «Chiudi progetto» إذا كان الأمر متاحًا. ٣) قائمة «Progetto» ثم «Nuovo progetto» ثم «Applicazione» ثم OK. ٤) فورًا: قائمة «Progetto» ثم «Salva progetto con nome»، اضغط زر «Nuova cartella» (مجلد جديد) وسمّه ciao، ادخل إليه بنقرتين، واحفظ المشروع باسم ciao.lpi، ثم الوحدة باسم unit1.pas واضغط «Salva». ٥) تحقّق: في أعلى نافذة Lazarus يظهر الاسم ciao.') +
    zh('开始之前先准备好地方：一个项目 = 一个文件夹，这样文件不会丢，也不会和同学的文件混在一起。1）菜单 File →「Chiudi tutto」（全部关闭）；如果问要不要保存旧项目，点「No」。2）菜单 Progetto →「Chiudi progetto」（如果能点）。3）菜单 Progetto →「Nuovo progetto」→「Applicazione」→ OK。4）马上保存：菜单 Progetto →「Salva progetto con nome」，点「Nuova cartella」（新建文件夹）按钮，取名 ciao，双击进去，项目存为 ciao.lpi，然后单元存为 unit1.pas，点「Salva」。5）检查：Lazarus 最上面的标题栏里出现 ciao。') });
S.push({ titolo: '3. Le finestre di Lazarus · ٣. نوافذ Lazarus · 3. Lazarus 的窗口',
  testo: '<p>Quando apri un progetto nuovo vedi più finestre. Ognuna ha un lavoro:</p>' +
    tab(['Dove', 'Si chiama', 'A che cosa serve'], [
      ['in alto', '<b>menu</b> e <b>palette dei componenti</b>', 'i comandi (File, Progetto, Esegui…) e, sotto, i pezzi da mettere nella finestra, divisi in linguette'],
      ['a sinistra', '<b>Ispettore oggetti</b>', 'le <b>proprietà</b> del pezzo selezionato (il testo, il nome, il colore) e i suoi <b>eventi</b> (che cosa succede quando lo clicchi)'],
      ['al centro', '<b>Form1</b>, con i puntini', 'la <b>finestra del tuo programma</b>: qui metti i pezzi'],
      ['dietro la Form', '<b>Editor del codice</b> (unit1.pas)', 'qui scrivi <b>che cosa fa</b> il programma'],
      ['in basso', '<b>Messaggi</b>', 'Lazarus ti dice se è andato tutto bene o dove c\'è un errore']]) +
    '<p>Per passare dalla Form al codice e ritorno: tasto ' + k('F12') + '.</p>' + quaderno(SCHEMA1) + foto(3) +
    ar('في الأعلى: القوائم ولوحة المكوّنات. على اليسار: «مفتش الكائنات» (الخصائص والأحداث). في الوسط: Form1 وهي نافذة برنامجك. خلفها: محرر الكود. في الأسفل: الرسائل والأخطاء. للتنقل بين النافذة والكود: F12.') +
    zh('上面：菜单和组件面板。左边：对象检查器（属性和事件）。中间：Form1，就是你的程序窗口。后面：代码编辑器。下面：消息（错误会写在这里）。窗口和代码之间切换：按 F12。') });
S.push({ titolo: '4. La palette: come scegliere il pezzo giusto · ٤. لوحة المكوّنات: كيف نختار القطعة · 4. 组件面板：怎么选零件',
  testo: '<p>La <b>palette dei componenti</b> è la fila di icone in alto, sotto il menu. I pezzi di oggi sono nella linguetta <b>Standard</b>. Per scegliere, chiediti: <b>che cosa deve fare chi usa il programma?</b></p>' +
    tab(['Deve…', 'Pezzo (componente)', 'Icona nella palette', 'Proprietà che conta'], [
      ['<b>scrivere</b> qualcosa', '<b>TEdit</b> (casella di testo)', 'una casella bianca con «abc» o «ab|»', k('Text') + ' = quello che c\'è scritto dentro'],
      ['<b>premere</b> per far succedere una cosa', '<b>TButton</b> (bottone)', 'un bottone con «OK»', k('Caption') + ' = la scritta sul bottone'],
      ['<b>leggere</b> un testo (solo guardare)', '<b>TLabel</b> (etichetta)', 'una «A»', k('Caption') + ' = il testo che si vede']]) +
    '<p>Per metterlo nella finestra: <b>un clic</b> sull\'icona nella palette, poi <b>un clic</b> sulla Form1, nel punto dove lo vuoi. Lazarus gli dà un nome da solo: ' + k('Edit1') + ', ' + k('Button1') + '. Il <b>nome</b> (' + k('Name') + ') è quello che userai nel codice.</p>' + foto(4) +
    ar('لوحة المكوّنات هي صف الأيقونات في الأعلى، اللسان «Standard». اسأل نفسك: ماذا يفعل المستخدم؟ يكتب ← TEdit (خانة نص، الخاصية Text). يضغط ← TButton (زر، الخاصية Caption). يقرأ فقط ← TLabel. نقرة على الأيقونة ثم نقرة على Form1.') +
    zh('组件面板是上面一排图标，在 Standard 标签里。问自己：用户要做什么？要写字 → TEdit（输入框，属性 Text）。要按 → TButton（按钮，属性 Caption）。只看文字 → TLabel。点一下图标，再点一下 Form1。') });
S.push({ titolo: '5. Esercitazione: il mio «Ciao» · ٥. التمرين: برنامج «Ciao» · 5. 练习：我的「Ciao」',
  testo: '<p>Un passo alla volta. Dopo ogni passo guarda lo schermo: deve essere uguale.</p>' +
    '<p><b>1.</b> Nella palette, linguetta <b>Standard</b>, clicca <b>TEdit</b>, poi clicca nella Form1, in alto a sinistra. Compare una casella con scritto ' + k('Edit1') + '.</p>' +
    '<p><b>2.</b> Con la casella selezionata, nell\'Ispettore oggetti trova la proprietà ' + k('Text') + ' e cancella la scritta «Edit1»: la casella resta vuota.</p>' +
    '<p><b>3.</b> Nella palette clicca <b>TButton</b>, poi clicca nella Form1 sotto la casella. Compare ' + k('Button1') + '.</p>' +
    '<p><b>4.</b> Con il bottone selezionato, nell\'Ispettore oggetti cambia ' + k('Caption') + ' in ' + k('Saluta') + '. FATTO: la finestra è pronta!</p>' +
    '<p><b>5.</b> Fai <b>doppio clic sul bottone</b>. Si apre il codice, con il cursore qui:</p>' +
    box('procedure TForm1.Button1Click(Sender: TObject);\nbegin\n  <span style="color:#7ee787">// qui scrivi la tua riga</span>\nend;') +
    '<p><b>6.</b> Tra ' + k('begin') + ' e ' + k('end;') + ' scrivi questa riga:</p>' + box("ShowMessage('Ciao ' + Edit1.Text);") +
    '<p>Che cosa vuol dire, pezzo per pezzo:</p>' +
    tab(['Pezzo', 'Vuol dire'], [
      [k('ShowMessage( … )'), 'apre una <b>finestrella</b> con un messaggio e il bottone <b>OK</b>. Quello che c\'è tra le parentesi è il messaggio'],
      [k('Edit1.Text'), 'il testo scritto dentro la casella Edit1 (il nome)'],
      [k("'Ciao '"), 'una scritta fissa. Va tra apici. Lo <b>spazio</b> dopo Ciao serve per non avere «CiaoAhmed»'],
      [k('+'), 'attacca due scritte una dopo l\'altra'],
      [k(';'), 'fine dell\'istruzione (come il punto alla fine di una frase)']]) +
    '<p>Tutto insieme: <b>«apri una finestrella con scritto Ciao e il nome che c\'è nella casella»</b>. Come alla lavagna: scrivi MARIO, premi Saluta, compare <b>Ciao MARIO</b> con il bottone OK. È la funzione che risponde al <b>clic</b> del bottone: si chiama ' + k('Button1Click') + '.</p>' + quaderno(SCHEMA3) + foto(5) +
    ar('١) ضع TEdit في النافذة وامسح نص «Edit1» من الخاصية Text. ٢) ضع TButton واجعل Caption = Saluta. ٣) انقر مرتين على الزر، يُفتح الكود. ٤) بين begin و end اكتب: ShowMessage(\'Ciao \' + Edit1.Text); المعنى: تفتح نافذة صغيرة فيها «Ciao» + الاسم وزر OK.') +
    zh('1）放一个 TEdit，在 Text 属性里删掉「Edit1」。2）放一个 TButton，Caption 改成 Saluta。3）双击按钮，打开代码。4）在 begin 和 end 中间写：ShowMessage(\'Ciao \' + Edit1.Text); 意思：打开一个小窗口，写着「Ciao」加上名字，还有 OK 按钮。') });
S.push({ titolo: '6. Salva e fai partire · ٦. احفظ وشغّل · 6. 保存并运行',
  testo: '<p>La cartella ' + k('ciao') + ' l\'hai già fatta nella scheda 2. Adesso basta poco.</p>' +
    '<p><b>1.</b> Premi ' + k('Ctrl') + ' + ' + k('S') + ': Lazarus salva tutto nella tua cartella.</p>' +
    '<p><b>2.</b> Premi ' + k('F9') + ' (oppure la freccia verde ▶ in alto). Lazarus prepara il programma e lo fa partire: si apre la TUA finestra.</p>' +
    '<p><b>3.</b> Clicca nella casella e scrivi il tuo nome.</p>' +
    '<p><b>4.</b> Clicca il bottone <b>Saluta</b>. Si apre una finestrella con <b>Ciao</b> e il tuo nome.</p>' +
    '<p><b>5.</b> Clicca <b>OK</b>. Ce l\'hai fatta: hai scritto il tuo primo programma!</p>' +
    '<p><b>Errore? È normale, succede a tutti i programmatori.</b> Guarda la finestra Messaggi in basso: dice la riga. I più comuni: manca il ' + k(';') + '; hai scritto ' + k('=') + ' invece di ' + k(':=') + '; manca un apice ' + k("'") + '; la riga è fuori da begin … end.</p>' + foto(6) +
    ar('١) اضغط Ctrl+S للحفظ. ٢) اضغط F9 للتشغيل: تفتح نافذتك. ٣) اكتب اسمك. ٤) اضغط الزر «Saluta». ٥) اضغط OK. خطأ؟ هذا طبيعي: انظر إلى «Messaggi» في الأسفل، فهي تذكر رقم السطر (ينقص ; أو ينقص \' ).') +
    zh('1）按 Ctrl+S 保存。2）按 F9 运行：你的窗口就打开了。3）写你的名字。4）点「Saluta」按钮。5）点 OK。出错了？很正常：看下面的 Messaggi，它会告诉你是哪一行（少了 ; 或者少了 \' ）。') });
S.push({ titolo: '7. I file del progetto, uno per uno · ٧. ملفات المشروع · 7. 项目的文件',
  testo: '<p>Dopo ' + k('F9') + ' apri la cartella ' + k('ciao') + ' con Esplora file. Lazarus ha creato tanti file. L\'<b>estensione</b> sono le lettere dopo il punto nel nome del file: dice <b>che tipo di file è</b>. Non vedi le estensioni? In Esplora file, in alto: <b>Visualizza</b> → <b>Mostra</b> → <b>Estensioni nomi file</b>.</p>' +
    '<p><b>Gruppo 1. Il progetto</b></p>' +
    tab(['File', 'Che cos\'è', 'Che cosa c\'è dentro', 'Si può cancellare?'], [
      [k('ciao.lpi'), 'informazioni del progetto (<b>L</b>azarus <b>P</b>roject <b>I</b>nformation)<br><i>Come: la scheda del progetto, con l\'elenco dei pezzi e le istruzioni per montarli</i>', 'un testo in formato <b>XML</b> (testo con le etichette tra &lt; e &gt;): quali file fanno parte del progetto e le <b>opzioni</b> del progetto e del compilatore, quelle che si cambiano dal menu <b>Progetto</b> → <b>Opzioni progetto…</b>. Con doppio clic su questo file riapri il progetto', '<b>NO</b>'],
      [k('ciao.lpr'), 'programma principale (<b>L</b>azarus <b>PR</b>ogram)<br><i>Come: il fischio di inizio della partita: fa partire tutto</i>', 'le poche righe in Pascal che fanno partire tutto e aprono Form1. Non si tocca', '<b>NO</b>'],
      [k('ciao.lps'), 'sessione (<b>L</b>azarus <b>P</b>roject <b>S</b>ession)<br><i>Come: un <b>segnalibro</b>: la memoria di dove eri rimasto</i>', 'quali file erano aperti nell\'editor, in che ordine erano le linguette, dov\'era il cursore. <b>Non contiene il programma</b>: se la cancelli, il tuo lavoro c\'è ancora tutto', 'sì: Lazarus la rifà'],
      [k('ciao.res'), 'risorse (<b>RES</b>ource)<br><i>Come: lo zaino con le cose da portare dentro l\'exe: icona e versione</i>', 'l\'icona e la versione del programma, pronte da mettere dentro l\'exe', 'sì: Lazarus la rifà'],
      [k('ciao.ico'), 'icona (<b>ICO</b>n)<br><i>Come: la foto profilo del programma</i>', 'il disegnino del programma, quello che vedi sulla barra di Windows', 'sì: Lazarus la rifà']]) +
    '<p><b>Gruppo 2. La finestra e il codice</b></p>' +
    tab(['File', 'Che cos\'è', 'Che cosa c\'è dentro', 'Si può cancellare?'], [
      [k('unit1.lfm'), 'la form (<b>L</b>azarus <b>F</b>or<b>M</b>)<br><i>Come: la piantina di una stanza: dove stanno i mobili</i>', '<b>com\'è fatta la finestra</b>: quali pezzi ci sono, dove stanno, quanto sono grandi, Caption e Text', '<b>NO</b>'],
      [k('unit1.pas'), 'la unit (un file di codice in <b>Pas</b>cal)<br><i>Come: la ricetta: le istruzioni che hai scritto tu</i>', 'il <b>TUO codice</b>: la procedura ' + k('Button1Click') + ' con la riga del Ciao. Una unit può avere anche l\'estensione ' + k('.pp'), '<b>NO</b>']]) +
    '<p><b>Gruppo 3. Il programma finito</b></p>' +
    tab(['File', 'Che cos\'è', 'Che cosa c\'è dentro', 'Si può cancellare?'], [
      [k('ciao.exe'), 'eseguibile (<b>EXE</b>cutable), nella cartella del progetto<br><i>Come: la torta già cotta: si mangia anche senza la ricetta</i>', 'il <b>programma finito</b>, creato con F9. Si apre anche senza Lazarus', 'sì: si rifà con F9']]) +
    '<p><b>Gruppo 4. File di lavoro del compilatore</b> (il <b>compilatore</b> è il programma che trasforma il Pascal in un programma che il computer sa eseguire)</p>' +
    tab(['File', 'Che cos\'è', 'Che cosa c\'è dentro', 'Si può cancellare?'], [
      [k('lib\\x86_64-win64\\'), 'cartella<br><i>Come: il tavolo della cucina dove si preparano i pezzi</i>', 'i pezzi intermedi che servono per fare l\'exe (qui sotto)', 'sì: Lazarus la rifà'],
      [k('.o'), 'file oggetto (<b>O</b>bject)<br><i>Come: un ingrediente già cotto, uno solo</i>', 'il codice macchina di <b>una sola</b> unit, per esempio ' + k('unit1.o'), 'sì'],
      [k('.ppu'), 'unit compilata di Free Pascal (<b>P</b>ascal <b>P</b>recompiled <b>U</b>nit)<br><i>Come: un pezzo già montato, con l\'etichetta che dice che cosa sa fare</i>', 'le informazioni sulla unit già tradotta, per esempio ' + k('unit1.ppu'), 'sì'],
      [k('.compiled'), 'promemoria della compilazione<br><i>Come: lo scontrino: ricorda com\'è andata l\'ultima volta</i>', 'come è stato compilato il progetto l\'ultima volta: così Lazarus sa se deve rifare tutto', 'sì'],
      [k('.or'), 'risorse compilate<br><i>Come: lo zaino del .res già chiuso, pronto da caricare</i>', 'il file ' + k('.res') + ' già pronto da attaccare all\'exe', 'sì'],
      [k('backup\\'), 'cartella delle copie di sicurezza<br><i>Come: la fotocopia del compito prima di correggerlo</i>', 'quando salvi un file che esisteva già, Lazarus mette qui la versione di prima. Le copie dei file del progetto hanno <b>lo stesso nome</b> dell\'originale (' + k('unit1.pas') + ', ' + k('unit1.lfm') + ', ' + k('ciao.lpi') + '…); un file che non fa parte del progetto prende in più ' + k('.bak') + ' (per esempio ' + k('prova.pas.bak') + '). La cartella compare dal secondo salvataggio', 'sì']]) +
    '<p>Con le impostazioni normali di Lazarus 4, fuori dalla cartella ' + k('backup') + ' non trovi copie con ' + k('~') + ' o ' + k('.bak') + '. Se le vedi, qualcuno ha cambiato le impostazioni delle copie (menu <b>Strumenti</b> → <b>Opzioni…</b>, pagina <b>Backup</b>).</p>' +
    '<p>Regola da ricordare: i <b>4 file da tenere</b>, da consegnare e da mettere su GitHub sono ' + k('.lpi') + ' ' + k('.lpr') + ' ' + k('.pas') + ' ' + k('.lfm') + '. Tutto il resto Lazarus lo rifà da solo.</p>' + quaderno(SCHEMA2) + foto(7) +
    ar('الامتداد هو الحروف بعد النقطة في اسم الملف، ويقول نوع الملف (لإظهاره في مستكشف الملفات: Visualizza ثم Mostra ثم Estensioni nomi file). المجموعة ١، المشروع: .lpi (معلومات المشروع وخياراته بصيغة XML، مثل بطاقة المشروع؛ ننقر عليه مرتين لنكمل العمل)، .lpr (البرنامج الرئيسي)، .lps (الجلسة: مثل علامة الكتاب، تتذكر أين توقفت: الملفات المفتوحة في المحرر وترتيبها ومكان المؤشر؛ لا تحتوي البرنامج، يمكن حذفها وLazarus يصنعها من جديد)، .res (الموارد)، .ico (الأيقونة). المجموعة ٢، النافذة والكود: .lfm (شكل النافذة، مثل مخطط الغرفة)، .pas (كودك، مثل الوصفة؛ وقد يكون امتداده أيضًا .pp). المجموعة ٣، البرنامج الجاهز: .exe (مثل الكعكة الجاهزة، تعمل بدون Lazarus). المجموعة ٤، ملفات عمل المترجم: المجلد lib\\x86_64-win64 فيه .o (كود الآلة لوحدة واحدة) و.ppu (وحدة مترجمة) و.compiled (تذكير بطريقة الترجمة) و.or (موارد مترجمة)؛ والمجلد backup فيه نسخ احتياطية بنفس الاسم. القاعدة: نحتفظ بأربعة ملفات ونسلّمها ونضعها على GitHub: .lpi .lpr .pas .lfm، والباقي يصنعه Lazarus وحده.') +
    zh('扩展名是文件名里点后面的字母，表示文件的类型（在文件资源管理器里显示：Visualizza → Mostra → Estensioni nomi file）。第 1 组，项目：.lpi（项目信息和选项，XML 格式，像项目卡片；双击它继续工作）、.lpr（主程序）、.lps（会话：像书签，记住你停在哪里：编辑器里打开了哪些文件、顺序、光标位置；里面没有程序，可以删掉，Lazarus 会再做一个）、.res（资源）、.ico（图标）。第 2 组，窗口和代码：.lfm（窗口的样子，像房间的平面图）、.pas（你的代码，像菜谱；单元也可以是 .pp）。第 3 组，做好的程序：.exe（像做好的蛋糕，没有 Lazarus 也能打开）。第 4 组，编译器的工作文件：lib\\x86_64-win64 文件夹里有 .o（一个单元的机器码）、.ppu（编译好的单元）、.compiled（怎么编译的记录）、.or（编译好的资源）；backup 文件夹里是同名的备份。规则：要保留、提交、放到 GitHub 上的是 4 个文件：.lpi .lpr .pas .lfm，其他的 Lazarus 会自己再做。') });
S.push({ titolo: '8. Fallo tuo · ٨. اجعله خاصًا بك · 8. 做成你自己的',
  testo: '<p>Il programma funziona? Adesso rendilo <b>tuo</b>. Scegli almeno una cosa:</p>' +
    '<p><b>1.</b> Il saluto nella <b>tua lingua</b>: al posto di ' + k("'Ciao '") + ' scrivi ' + k("'Hello '") + ', ' + k("'مرحبا '") + ', ' + k("'你好 '") + ', ' + k("'Hola '") + '…</p>' +
    '<p><b>2.</b> Il <b>titolo</b> della finestra: clicca su un punto vuoto della Form1, nell\'Ispettore oggetti cambia ' + k('Caption') + ' (per esempio «Il saluto di Ahmed»).</p>' +
    '<p><b>3.</b> Il <b>colore</b>: sempre sulla Form1, proprietà ' + k('Color') + ', scegli un colore dalla tendina.</p>' +
    '<p><b>4.</b> Per i più veloci: aggiungi una TLabel e una seconda riga, ' + k("Label1.Caption := 'Ciao ' + Edit1.Text;") + ': il saluto resta scritto anche nella finestra.</p>' +
    '<p>Poi <b>spiegalo in 30 secondi</b> al compagno: «Ho messo una TEdit e un TButton; quando clicco, la funzione Button1Click apre una finestrella con Ciao e il nome».</p>' +
    ar('غيّر التحية إلى لغتك (مرحبا، 你好، Hello)، غيّر عنوان النافذة (Caption في Form1) ولونها (Color). ثم اشرح لزميلك في 30 ثانية ماذا يفعل برنامجك.') +
    zh('把问候改成你的语言（你好、مرحبا、Hello），改窗口的标题（Form1 的 Caption）和颜色（Color）。然后用 30 秒跟同学讲你的程序做什么。') });
S.push({ titolo: '9. Consegna · ٩. التسليم · 9. 提交',
  testo: '<p>Su Classroom c\'è il compito <b>«Il mio primo programma: Ciao in Lazarus»</b>. Dentro c\'è un <b>Documento Google</b> già pronto, solo tuo. Aprilo e fai 3 cose:</p>' +
    '<p><b>1. Il codice.</b> In Lazarus seleziona con il mouse la tua procedura, da ' + k('procedure TForm1.Button1Click') + ' fino a ' + k('end;') + ', premi ' + k('Ctrl') + ' + ' + k('C') + '; nel Documento clicca sotto «1. Il mio codice» e premi ' + k('Ctrl') + ' + ' + k('V') + '.</p>' +
    '<p><b>2. Lo screenshot.</b> Fai partire il programma (' + k('F9') + '), scrivi il tuo nome e premi Saluta. Poi premi ' + k('Win') + ' + ' + k('Shift') + ' + ' + k('S') + ' e trascina un rettangolo intorno alla tua finestra. Nel Documento clicca sotto «2. Il mio programma che funziona» e premi ' + k('Ctrl') + ' + ' + k('V') + '.</p>' +
    '<p><b>3. Con parole tue.</b> Sotto «3» scrivi in una o due frasi che cosa fa la riga ' + k("ShowMessage('Ciao ' + Edit1.Text);") + '. Puoi scrivere anche nella tua lingua.</p>' +
    '<p>Poi in Classroom premi <b>Consegna</b> (il bottone blu in alto a destra nel compito).</p>' +
    ar('في Classroom الواجب «Il mio primo programma». داخله مستند Google خاص بك. ١) انسخ الكود من procedure إلى end; (Ctrl+C) والصقه (Ctrl+V). ٢) شغّل البرنامج، اكتب اسمك، اضغط Saluta، ثم Win+Shift+S وحدد نافذتك، والصق في المستند. ٣) اكتب بكلماتك ماذا يفعل السطر. ثم اضغط «Consegna» (الزر الأزرق).') +
    zh('Classroom 里有作业「Il mio primo programma」，里面有一份你自己的 Google 文档。1）复制代码，从 procedure 到 end;（Ctrl+C），粘贴（Ctrl+V）。2）运行程序，写名字，按 Saluta，然后按 Win+Shift+S 框住你的窗口，粘贴到文档里。3）用你自己的话写这一行做什么。然后按「Consegna」（蓝色按钮）提交。') });
const B = { id: '1inf-lazarus-ciao-v1', classe: '1INF', titolo: 'Lazarus: il mio primo programma · Lazarus: برنامجي الأول · Lazarus：我的第一个程序',
  sotto: '1INF · 28/10/2026 · TEdit, TButton, il clic, i file del progetto · consegna su Classroom',
  stato: 'stato/1inf-lazarus-ciao.json', risultati: 'risultati.html?b=1inf-lazarus-ciao', minuti: 10, anteprima: '868848605',
  aree: { nozioni: { nome: 'Lazarus: le parole giuste', peso: 100 } }, schede: S, schede_temi: {},
  strumenti: [{ t: 'La mia giornata: voto, fatto e da fare', u: '../1inf-oggi/', c: '#b45309' }, { t: 'Il monitor della lezione', u: '../1inf-monitor/', c: '#6e40c9' }],
  allenamento: [], crocette: [], aperte: [], recupero: [] };
fs.writeFileSync(DOCS + 'verifica/banche/1inf-lazarus-ciao.js', '// 1INF · Lazarus, il primo programma «Ciao» (28/10/2026), IT/AR/ZH. Generato da classe-1/lazarus-ciao/_build/lazarus.js\nwindow.BANCA = ' + JSON.stringify(B, null, 1) + ';\n');
const st = DOCS + 'verifica/stato/1inf-lazarus-ciao.json';
if (!fs.existsSync(st)) fs.writeFileSync(st, JSON.stringify({ verifica: 'chiusa', recupero: 'chiuso', _nota: '28/10: si consegna il Documento su Classroom' }, null, 1));
console.log('ok', S.length, 'schede');
