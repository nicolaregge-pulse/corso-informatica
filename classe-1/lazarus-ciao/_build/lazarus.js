// 28/10/2026 1INF, Laboratorio (Nicola: «iniziamo a far vedere Lazarus: una Edit e un bottone, scrive il nome, preme e compare Ciao e il suo nome»).
// Teoria in schede IT/AR/ZH + esercitazione + consegna (Documento su Classroom con il codice e lo screenshot).
// Uso: node lazarus.js  →  docs/verifica/banche/1inf-lazarus-ciao.js (+ stato). Le foto della lavagna del prof vanno in FOTO (percorsi da docs/verifica/).
const fs = require('fs'), path = require('path'); const DOCS = path.join(__dirname, '../../../docs/');
const FOTO = JSON.parse(fs.existsSync(path.join(__dirname, 'foto.json')) ? fs.readFileSync(path.join(__dirname, 'foto.json'), 'utf8') : '{}');
const ar = t => '<p lang="ar" dir="rtl" style="color:#5b6573">' + t + '</p>', zh = t => '<p lang="zh" style="color:#5b6573">' + t + '</p>';
const k = t => '<code style="background:#eef2f7;border:1px solid #d5dbe3;border-radius:6px;padding:1px 6px">' + t + '</code>';
const box = t => '<pre style="background:#0d1117;color:#e6edf3;padding:12px;border-radius:10px;font-size:17px;overflow-x:auto">' + t + '</pre>';
const tab = (h, r) => '<table style="border-collapse:collapse;width:100%;margin:8px 0"><tr>' + h.map(x => '<th style="border:1px solid #d5dbe3;padding:6px;background:#eef2f7;text-align:left">' + x + '</th>').join('') + '</tr>' +
  r.map(rr => '<tr>' + rr.map(x => '<td style="border:1px solid #d5dbe3;padding:6px;vertical-align:top">' + x + '</td>').join('') + '</tr>').join('') + '</table>';
const foto = n => (FOTO[n] || []).map(f => '<p><img src="' + f + '" alt="foto della lavagna" style="max-width:100%;border-radius:10px;border:1px solid #d5dbe3"></p>').join('');
const S = [];
S.push({ titolo: '1. Che cos\'è Lazarus · ١. ما هو Lazarus · 1. Lazarus 是什么',
  testo: '<p><b>Lazarus</b> è un programma che serve a <b>creare altri programmi</b>, con le finestre e i bottoni, come quelli che usi ogni giorno. Funziona come i <b>mattoncini</b>: prendi un pezzo già pronto (un bottone, una casella), lo metti nella finestra e poi scrivi <b>che cosa deve fare</b>. Il linguaggio si chiama <b>Pascal</b>.</p>' +
    '<p>Oggi facciamo il primo programma di tutti i programmatori: il <b>«Ciao»</b>. Scrivi il tuo nome in una casella, premi un bottone e il programma ti saluta: <b>Ciao Ahmed</b>.</p>' +
    '<p>Per aprire Lazarus: doppio clic sull\'icona di Lazarus (il prof vi mostra dove si trova). Poi in alto: menu <b>Progetto</b> → <b>Nuovo progetto</b> → <b>Applicazione</b> → <b>OK</b>.</p>' + foto(1) +
    ar('Lazarus برنامج نصنع به برامج أخرى بنوافذ وأزرار. نأخذ قطعة جاهزة (زر، خانة) ونضعها في النافذة، ثم نكتب ماذا تفعل. اللغة اسمها Pascal. اليوم نصنع برنامج «Ciao» (مرحبًا): تكتب اسمك، تضغط الزر، فيقول لك البرنامج مرحبًا.') +
    zh('Lazarus 是用来做其他程序的软件，可以做有窗口和按钮的程序。像搭积木一样：拿一个现成的零件（按钮、输入框），放进窗口，再写它要做什么。语言叫 Pascal。今天做第一个程序「Ciao」（你好）：写名字，按按钮，程序就跟你打招呼。') });
S.push({ titolo: '2. Le finestre di Lazarus · ٢. نوافذ Lazarus · 2. Lazarus 的窗口',
  testo: '<p>Quando apri un progetto nuovo vedi più finestre. Ognuna ha un lavoro:</p>' +
    tab(['Dove', 'Si chiama', 'A che cosa serve'], [
      ['in alto', '<b>menu</b> e <b>palette dei componenti</b>', 'i comandi (File, Progetto, Esegui…) e, sotto, i pezzi da mettere nella finestra, divisi in linguette'],
      ['a sinistra', '<b>Ispettore oggetti</b>', 'le <b>proprietà</b> del pezzo selezionato (il testo, il nome, il colore) e i suoi <b>eventi</b> (che cosa succede quando lo clicchi)'],
      ['al centro', '<b>Form1</b>, con i puntini', 'la <b>finestra del tuo programma</b>: qui metti i pezzi'],
      ['dietro la Form', '<b>Editor del codice</b> (unit1.pas)', 'qui scrivi <b>che cosa fa</b> il programma'],
      ['in basso', '<b>Messaggi</b>', 'Lazarus ti dice se è andato tutto bene o dove c\'è un errore']]) +
    '<p>Per passare dalla Form al codice e ritorno: tasto ' + k('F12') + '.</p>' + foto(2) +
    ar('في الأعلى: القوائم ولوحة المكوّنات. على اليسار: «مفتش الكائنات» (الخصائص والأحداث). في الوسط: Form1 وهي نافذة برنامجك. خلفها: محرر الكود. في الأسفل: الرسائل والأخطاء. للتنقل بين النافذة والكود: F12.') +
    zh('上面：菜单和组件面板。左边：对象检查器（属性和事件）。中间：Form1，就是你的程序窗口。后面：代码编辑器。下面：消息（错误会写在这里）。窗口和代码之间切换：按 F12。') });
S.push({ titolo: '3. La palette: come scegliere il pezzo giusto · ٣. لوحة المكوّنات: كيف نختار القطعة · 3. 组件面板：怎么选零件',
  testo: '<p>La <b>palette dei componenti</b> è la fila di icone in alto, sotto il menu. I pezzi di oggi sono nella linguetta <b>Standard</b>. Per scegliere, chiediti: <b>che cosa deve fare chi usa il programma?</b></p>' +
    tab(['Deve…', 'Pezzo (componente)', 'Icona nella palette', 'Proprietà che conta'], [
      ['<b>scrivere</b> qualcosa', '<b>TEdit</b> (casella di testo)', 'una casella bianca con «abc» o «ab|»', k('Text') + ' = quello che c\'è scritto dentro'],
      ['<b>premere</b> per far succedere una cosa', '<b>TButton</b> (bottone)', 'un bottone con «OK»', k('Caption') + ' = la scritta sul bottone'],
      ['<b>leggere</b> un testo (solo guardare)', '<b>TLabel</b> (etichetta)', 'una «A»', k('Caption') + ' = il testo che si vede']]) +
    '<p>Per metterlo nella finestra: <b>un clic</b> sull\'icona nella palette, poi <b>un clic</b> sulla Form1, nel punto dove lo vuoi. Lazarus gli dà un nome da solo: ' + k('Edit1') + ', ' + k('Button1') + '. Il <b>nome</b> (' + k('Name') + ') è quello che userai nel codice.</p>' + foto(3) +
    ar('لوحة المكوّنات هي صف الأيقونات في الأعلى، اللسان «Standard». اسأل نفسك: ماذا يفعل المستخدم؟ يكتب ← TEdit (خانة نص، الخاصية Text). يضغط ← TButton (زر، الخاصية Caption). يقرأ فقط ← TLabel. نقرة على الأيقونة ثم نقرة على Form1.') +
    zh('组件面板是上面一排图标，在 Standard 标签里。问自己：用户要做什么？要写字 → TEdit（输入框，属性 Text）。要按 → TButton（按钮，属性 Caption）。只看文字 → TLabel。点一下图标，再点一下 Form1。') });
S.push({ titolo: '4. Esercitazione: il mio «Ciao» · ٤. التمرين: برنامج «Ciao» · 4. 练习：我的「Ciao」',
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
    '<p>Tutto insieme: <b>«apri una finestrella con scritto Ciao e il nome che c\'è nella casella»</b>. Come alla lavagna: scrivi MARIO, premi Saluta, compare <b>Ciao MARIO</b> con il bottone OK. È la funzione che risponde al <b>clic</b> del bottone: si chiama ' + k('Button1Click') + '.</p>' + foto(4) +
    ar('١) ضع TEdit في النافذة وامسح نص «Edit1» من الخاصية Text. ٢) ضع TButton واجعل Caption = Saluta. ٣) انقر مرتين على الزر، يُفتح الكود. ٤) بين begin و end اكتب: ShowMessage(\'Ciao \' + Edit1.Text); المعنى: تفتح نافذة صغيرة فيها «Ciao» + الاسم وزر OK.') +
    zh('1）放一个 TEdit，在 Text 属性里删掉「Edit1」。2）放一个 TButton，Caption 改成 Saluta。3）双击按钮，打开代码。4）在 begin 和 end 中间写：ShowMessage(\'Ciao \' + Edit1.Text); 意思：打开一个小窗口，写着「Ciao」加上名字，还有 OK 按钮。') });
S.push({ titolo: '5. Salva e fai partire · ٥. احفظ وشغّل · 5. 保存并运行',
  testo: '<p><b>0.</b> Come alla lavagna: prima <b>chiudi tutti i file</b> aperti (menu <b>File</b> → <b>Chiudi tutto</b>), poi crei la tua cartella e salvi lì dentro tutti i file.</p><p><b>1.</b> Prima di tutto si <b>salva</b>. Menu <b>Progetto</b> → <b>Salva progetto con nome…</b>. Crea una cartella tua (bottone «Nuova cartella»), per esempio ' + k('ciao') + ', ed entraci. Salva il progetto come ' + k('ciao.lpi') + ' e poi la unit come ' + k('unit1.pas') + '.</p>' +
    '<p><b>2.</b> Premi ' + k('F9') + ' (oppure la freccia verde ▶ in alto). Lazarus prepara il programma e lo fa partire: si apre la TUA finestra.</p>' +
    '<p><b>3.</b> Scrivi il tuo nome nella casella e premi <b>Saluta</b>. Si apre una finestrella con <b>Ciao</b> e il tuo nome: premi <b>OK</b>. Ce l\'hai fatta: hai scritto il tuo primo programma!</p>' +
    '<p><b>4.</b> Per tornare a lavorare chiudi la finestra del programma con la X. Da ora in poi: ogni volta che una cosa funziona, ' + k('Ctrl') + ' + ' + k('S') + '.</p>' +
    '<p><b>Errore? È normale, succede a tutti i programmatori.</b> Guarda la finestra Messaggi in basso: dice la riga. I più comuni: manca il ' + k(';') + '; hai scritto ' + k('=') + ' invece di ' + k(':=') + '; manca un apice ' + k("'") + '; la riga è fuori da begin … end.</p>' + foto(5) +
    ar('احفظ أولًا: قائمة «Progetto» ثم «Salva progetto con nome»، في مجلد خاص بك اسمه ciao. ثم اضغط F9: تفتح نافذتك. اكتب اسمك واضغط Saluta. خطأ؟ هذا طبيعي: انظر إلى «Messaggi» في الأسفل (ينقص ; أو كتبت = بدل :=).') +
    zh('先保存：菜单 Progetto →「Salva progetto con nome」，存在你自己的文件夹 ciao 里。然后按 F9：你的窗口就打开了。写名字，按 Saluta。出错了？很正常：看下面的 Messaggi（少了 ; 或者写了 = 而不是 :=）。') });
S.push({ titolo: '6. I file del progetto, uno per uno · ٦. ملفات المشروع · 6. 项目的文件',
  testo: '<p>Apri la cartella ' + k('ciao') + ' con Esplora file. Lazarus ha creato tanti file. Ognuno ha un\'<b>estensione</b> (le lettere dopo il punto) che dice <b>che cosa c\'è dentro</b>. (Non vedi le estensioni? In Esplora file: <b>Visualizza</b> → <b>Mostra</b> → <b>Estensioni nomi file</b>.)</p>' +
    tab(['File', 'Che cos\'è', 'Che cosa c\'è dentro', 'Importante?'], [
      [k('ciao.lpi'), '<b>L</b>azarus <b>P</b>roject <b>I</b>nformation', 'le impostazioni del progetto: quali file lo compongono, come si prepara. Si apre con doppio clic per riprendere il lavoro', '<b>SÌ</b>'],
      [k('ciao.lpr'), '<b>L</b>azarus <b>PR</b>ogram', 'il programma principale: le poche righe che fanno partire tutto e aprono Form1. Non si tocca', '<b>SÌ</b>'],
      [k('unit1.pas'), 'unit in <b>Pas</b>cal', 'il <b>TUO codice</b>: la procedura ' + k('Button1Click') + ' con la riga del Ciao', '<b>SÌ</b>'],
      [k('unit1.lfm'), '<b>L</b>azarus <b>F</b>or<b>M</b>', '<b>com\'è fatta la finestra</b>: quali pezzi ci sono, dove stanno, grandezza, Caption e Text', '<b>SÌ</b>'],
      [k('ciao.lps'), '<b>L</b>azarus <b>P</b>roject <b>S</b>ession', 'quali file avevi aperto e dov\'era il cursore. Si può buttare', 'no'],
      [k('ciao.res'), '<b>RES</b>ource (risorse)', 'l\'icona e la versione del programma. Lazarus la rifà da solo', 'no'],
      [k('ciao.exe'), '<b>EXE</b>cutable (eseguibile)', 'il <b>programma finito</b>, creato con F9. Si apre anche senza Lazarus', 'no: si rifà con F9'],
      [k('lib'), 'cartella', 'pezzi intermedi che Lazarus prepara per fare l\'exe (file .o e .ppu)', 'no'],
      [k('backup'), 'cartella', 'copie di sicurezza fatte da Lazarus quando salvi', 'no']]) +
    '<p>Regola da ricordare: i <b>4 file importanti</b> sono ' + k('.lpi') + ' ' + k('.lpr') + ' ' + k('.pas') + ' ' + k('.lfm') + '. Con questi 4 il progetto si rifà su qualunque computer.</p>' + foto(6) +
    ar('لكل ملف امتداد (الحروف بعد النقطة). المهمّة أربعة: .lpi (إعدادات المشروع، نفتحه لنكمل العمل)، .lpr (البرنامج الرئيسي)، .pas (الكود الخاص بك)، .lfm (شكل النافذة). الباقي (.lps، .res، .exe، lib، backup) يصنعه Lazarus وحده.') +
    zh('每个文件都有扩展名（点后面的字母）。重要的有 4 个：.lpi（项目设置，双击它继续工作）、.lpr（主程序）、.pas（你的代码）、.lfm（窗口的样子）。其他的（.lps、.res、.exe、lib、backup）Lazarus 会自己再做。') });
S.push({ titolo: '7. Fallo tuo · ٧. اجعله خاصًا بك · 7. 做成你自己的',
  testo: '<p>Il programma funziona? Adesso rendilo <b>tuo</b>. Scegli almeno una cosa:</p>' +
    '<p><b>1.</b> Il saluto nella <b>tua lingua</b>: al posto di ' + k("'Ciao '") + ' scrivi ' + k("'Hello '") + ', ' + k("'مرحبا '") + ', ' + k("'你好 '") + ', ' + k("'Hola '") + '…</p>' +
    '<p><b>2.</b> Il <b>titolo</b> della finestra: clicca su un punto vuoto della Form1, nell\'Ispettore oggetti cambia ' + k('Caption') + ' (per esempio «Il saluto di Ahmed»).</p>' +
    '<p><b>3.</b> Il <b>colore</b>: sempre sulla Form1, proprietà ' + k('Color') + ', scegli un colore dalla tendina.</p>' +
    '<p><b>4.</b> Per i più veloci: aggiungi una TLabel e una seconda riga, ' + k("Label1.Caption := 'Ciao ' + Edit1.Text;") + ': il saluto resta scritto anche nella finestra.</p>' +
    '<p>Poi <b>spiegalo in 30 secondi</b> al compagno: «Ho messo una TEdit e un TButton; quando clicco, la funzione Button1Click apre una finestrella con Ciao e il nome».</p>' +
    ar('غيّر التحية إلى لغتك (مرحبا، 你好، Hello)، غيّر عنوان النافذة (Caption في Form1) ولونها (Color). ثم اشرح لزميلك في 30 ثانية ماذا يفعل برنامجك.') +
    zh('把问候改成你的语言（你好、مرحبا、Hello），改窗口的标题（Form1 的 Caption）和颜色（Color）。然后用 30 秒跟同学讲你的程序做什么。') });
S.push({ titolo: '8. Consegna · ٨. التسليم · 8. 提交',
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
