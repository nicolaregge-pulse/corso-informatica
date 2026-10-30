// 1INF · 30/10/2026: String e Integer. APERTA ai ragazzi alle 06:45 (Tecnologia 8-9, parte 2 della lezione Unicode, e laboratorio): teoria e ripasso; il quiz è su Moduli. Generato da classe-1/lazarus-lab-30-10/_build/genera.py; schede semplificate A MANO il 30/10 alle 08:45 (box IN PAROLE SEMPLICI): NON rigenerare senza riportare le modifiche nel generatore
window.BANCA = {
 "id": "1inf-lab3010-tipi-v1",
 "classe": "1INF",
 "titolo": "String e Integer · String و Integer · String 和 Integer",
 "sotto": "1INF · 30/10/2026 · laboratorio, 1ª ora · variabili, String, Integer, StrToInt, IntToStr · teoria, ripasso e quiz",
 "stato": "stato/1inf-lab3010-tipi.json",
 "minuti": 20,
 "anteprima": "868848605",
 "aree": {
  "tipi": {
   "nome": "String e Integer",
   "peso": 85
  },
  "mia": {
   "nome": "Nel mio programma (parole tue)",
   "peso": 15
  }
 },
 "strumenti": [
  {
   "t": "La mia giornata: voto, fatto e da fare",
   "u": "../1inf-oggi/",
   "c": "#b45309"
  }
 ],
 "schede": [
  {
   "titolo": "1. La variabile: una scatola con un nome · ١. المتغير: صندوق له اسم · 1. 变量：一个有名字的盒子",
   "testo": "<div style=\"border:3px solid #b45309;background:#fff3cd;color:#000;border-radius:12px;padding:10px;margin:0 0 14px\"><p style=\"font-size:1.2em;margin:0 0 6px\"><b>IN PAROLE SEMPLICI</b></p><p lang=\"ar\" dir=\"rtl\" style=\"color:#333\">بكلمات بسيطة</p><p lang=\"zh\" style=\"color:#333\">简单地说</p><p style=\"color:#000\">1. Una <b>STRINGA</b> è testo: si scrive tra apici, <code>'12'</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#333\">١. String هي نص: تُكتب بين علامتين ' '، مثل '12'.</p><p lang=\"zh\" style=\"color:#333\">1. 字符串（String）是文字：写在引号 ' ' 里，比如 '12'。</p><p style=\"color:#000\">2. Un <b>INTERO</b> è un numero: <code>12</code>, senza apici.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#333\">٢. Integer هو عدد: 12، بدون علامات ' '.</p><p lang=\"zh\" style=\"color:#333\">2. 整数（Integer）是数字：12，没有引号。</p><p style=\"color:#000\">3. Con le stringhe il + le attacca: <code>'12' + '15' = '1215'</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#333\">٣. مع النصوص، علامة + تلصقها: '12' + '15' = '1215'.</p><p lang=\"zh\" style=\"color:#333\">3. 字符串的 + 是连起来：'12' + '15' = '1215'。</p><p style=\"color:#000\">4. Con gli interi il + fa la somma: <code>12 + 15 = 27</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#333\">٤. مع الأعداد، علامة + تجمع: 12 + 15 = 27.</p><p lang=\"zh\" style=\"color:#333\">4. 整数的 + 是相加：12 + 15 = 27。</p><p style=\"color:#000\">5. Trucco: se vedi gli apici <code>' '</code> è una stringa.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#333\">٥. حيلة: إذا رأيت العلامتين ' ' فهو نص (String).</p><p lang=\"zh\" style=\"color:#333\">5. 小窍门：看到引号 ' ' 就是字符串。</p></div><p>Una <b>variabile</b> è una <b>scatola</b>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">المتغير صندوق.</p><p lang=\"zh\" style=\"color:#5b6573\">变量是一个盒子。</p><p>Sulla scatola c'è un nome: per esempio <code>eta</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">على الصندوق اسم: مثلاً eta.</p><p lang=\"zh\" style=\"color:#5b6573\">盒子上有名字：比如 eta。</p><p>Dentro la scatola c'è un valore: per esempio <code>12</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">داخل الصندوق قيمة: مثلاً 12.</p><p lang=\"zh\" style=\"color:#5b6573\">盒子里有一个值：比如 12。</p><p><code>:=</code> vuol dire «metti dentro».</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">:= تعني «ضع داخل».</p><p lang=\"zh\" style=\"color:#5b6573\">:= 的意思是“放进去”。</p><p>Oggi due tipi di scatola: <b>String</b> (testo) e <b>Integer</b> (numero).</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">اليوم نوعان من الصناديق: String (نص) و Integer (عدد).</p><p lang=\"zh\" style=\"color:#5b6573\">今天两种盒子：String（文字）和 Integer（数字）。</p><pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">var\n  nome: String;     { scatola per il testo }\n  eta: Integer;     { scatola per un numero intero }\nbegin\n  nome := &#x27;Ahmed&#x27;;\n  eta := 12;</pre>"
  },
  {
   "titolo": "2. String: il testo tra apici · ٢. String: النص بين علامتي اقتباس · 2. String：引号里的文字",
   "testo": "<p>Esempi: <code>'Ciao'</code>, <code>'Milano'</code>, <code>'007'</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">أمثلة: 'Ciao'، 'Milano'، '007'.</p><p lang=\"zh\" style=\"color:#5b6573\">例子：'Ciao'、'Milano'、'007'。</p><p>Sono tutte <b>String</b>: testo.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">كلها String: نص.</p><p lang=\"zh\" style=\"color:#5b6573\">它们都是 String：文字。</p><p>Una String si scrive tra <b>apici</b> <code>' '</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">String تُكتب بين علامتين ' '.</p><p lang=\"zh\" style=\"color:#5b6573\">String 写在引号 ' ' 里。</p><p><code>'007'</code> ha gli apici: è una String, anche se ha dei numeri.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">'007' لها علامتان ' ': هي String، حتى لو فيها أرقام.</p><p lang=\"zh\" style=\"color:#5b6573\">'007' 有引号：它是 String，虽然里面是数字。</p><p>Il + attacca le String: <code>'Ciao ' + 'Ahmed'</code> = <code>'Ciao Ahmed'</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">علامة + تلصق النصوص: 'Ciao ' + 'Ahmed' = 'Ciao Ahmed'.</p><p lang=\"zh\" style=\"color:#5b6573\">+ 把 String 连起来：'Ciao ' + 'Ahmed' = 'Ciao Ahmed'。</p><pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">&#x27;Ciao&#x27;      String\n&#x27;007&#x27;       String (ha gli apici!)\n&#x27;Ciao &#x27; + &#x27;Ahmed&#x27;  -&gt;  &#x27;Ciao Ahmed&#x27;</pre>"
  },
  {
   "titolo": "3. Integer: il numero intero · ٣. Integer: العدد الصحيح · 3. Integer：整数",
   "testo": "<p>Esempi: <code>0</code>, <code>7</code>, <code>2026</code>, <code>-5</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">أمثلة: 0، 7، 2026، -5.</p><p lang=\"zh\" style=\"color:#5b6573\">例子：0、7、2026、-5。</p><p>Sono tutti <b>Integer</b>: numeri interi.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">كلها Integer: أعداد صحيحة.</p><p lang=\"zh\" style=\"color:#5b6573\">它们都是 Integer：整数。</p><p>Niente apici. Niente virgola.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">بدون علامات ' '. بدون فاصلة.</p><p lang=\"zh\" style=\"color:#5b6573\">没有引号。没有小数点。</p><p>Con gli Integer fai i conti: <code>12 + 3</code> = <code>15</code>.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">مع Integer تحسب: 12 + 3 = 15.</p><p lang=\"zh\" style=\"color:#5b6573\">Integer 可以计算：12 + 3 = 15。</p><p><code>3.5</code> NON è un Integer: ha la virgola.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">3.5 ليس Integer: فيه فاصلة.</p><p lang=\"zh\" style=\"color:#5b6573\">3.5 不是 Integer：它有小数点。</p><pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">12          Integer\n-5          Integer\n3.5         NON e&#x27; un Integer (ha la virgola)\n12 + 3  -&gt;  15</pre>"
  },
  {
   "titolo": "4. La trappola: '5' + '3' oppure 5 + 3? · ٤. الفخ: '5' + '3' أم 5 + 3؟ · 4. 陷阱：'5' + '3' 还是 5 + 3？",
   "testo": "<p><code>'5' + '3'</code> = <code>'53'</code>: sono String, il + le attacca.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">'5' + '3' = '53': هي نصوص، علامة + تلصقها.</p><p lang=\"zh\" style=\"color:#5b6573\">'5' + '3' = '53'：是 String，+ 把它们连起来。</p><p><code>5 + 3</code> = <code>8</code>: sono Integer, il + fa la somma.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">5 + 3 = 8: هي أعداد، علامة + تجمعها.</p><p lang=\"zh\" style=\"color:#5b6573\">5 + 3 = 8：是 Integer，+ 做加法。</p><p>Lo stesso + fa due cose diverse.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">نفس العلامة + تفعل شيئين مختلفين.</p><p lang=\"zh\" style=\"color:#5b6573\">同一个 + 做两件不同的事。</p><p>Guarda gli apici: con gli apici è testo.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">انظر إلى العلامتين ' ': معهما هو نص.</p><p lang=\"zh\" style=\"color:#5b6573\">看引号：有引号就是文字。</p><pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">&#x27;5&#x27; + &#x27;3&#x27;   -&gt;  &#x27;53&#x27;   (String: attacca)\n 5  +  3   -&gt;   8     (Integer: somma)</pre><img src=\"../1inf-unicode/immagini/lavagna-2026-10-30-3.jpg\" alt=\"La lavagna del 30/10: stringhe e interi, &#x27;12&#x27; + &#x27;15&#x27; = &#x27;1215&#x27; e 12 + 15 = 27\" style=\"display:block;width:100%;max-width:520px;height:auto;margin:10px auto 4px;border-radius:10px;border:1px solid #d5dbe3\" loading=\"lazy\"><p>La lavagna di oggi: <code>'12' + '15' = '1215'</code> (String, attacca). <code>12 + 15 = 27</code> (Integer, somma).</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">سبورة اليوم: '12' + '15' = '1215' (String، تلصق). 12 + 15 = 27 (Integer، تجمع).</p><p lang=\"zh\" style=\"color:#5b6573\">今天的白板：'12' + '15' = '1215'（String，连起来）。12 + 15 = 27（Integer，相加）。</p>"
  },
  {
   "titolo": "5. In Lazarus le caselle hanno String · ٥. في Lazarus الخانات فيها String · 5. 在 Lazarus 里，输入框里是 String",
   "testo": "<p>Nella casella scrivi 15.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">في الخانة تكتب 15.</p><p lang=\"zh\" style=\"color:#5b6573\">你在输入框里写 15。</p><p>Dentro <code>Edit1.Text</code> c'è <code>'15'</code>: testo, una String.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">داخل Edit1.Text يوجد '15': نص، String.</p><p lang=\"zh\" style=\"color:#5b6573\">Edit1.Text 里面是 '15'：文字，是 String。</p><p>Anche <code>Label1.Caption</code> è una String.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">Label1.Caption أيضاً String.</p><p lang=\"zh\" style=\"color:#5b6573\">Label1.Caption 也是 String。</p><p><code>Label1.Caption := 7;</code> dà errore: 7 è un Integer.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">Label1.Caption := 7; يعطي خطأ: 7 هو Integer.</p><p lang=\"zh\" style=\"color:#5b6573\">Label1.Caption := 7; 会出错：7 是 Integer。</p><p>Giusto: <code>Label1.Caption := '7';</code></p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">الصحيح: Label1.Caption := '7';</p><p lang=\"zh\" style=\"color:#5b6573\">正确：Label1.Caption := '7';</p><pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">Edit1.Text       String  (scrivo 15 -&gt; &#x27;15&#x27;)\nLabel1.Caption   String\nLabel1.Caption := 7;     ERRORE: Incompatible types\nLabel1.Caption := &#x27;7&#x27;;   giusto</pre>"
  },
  {
   "titolo": "6. I due traduttori: StrToInt e IntToStr · ٦. المترجمان: StrToInt و IntToStr · 6. 两个翻译：StrToInt 和 IntToStr",
   "testo": "<p><code>StrToInt('7')</code> = <code>7</code>: da testo a numero.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">StrToInt('7') = 7: من نص إلى عدد.</p><p lang=\"zh\" style=\"color:#5b6573\">StrToInt('7') = 7：从文字变成数字。</p><p><code>IntToStr(7)</code> = <code>'7'</code>: da numero a testo.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">IntToStr(7) = '7': من عدد إلى نص.</p><p lang=\"zh\" style=\"color:#5b6573\">IntToStr(7) = '7'：从数字变成文字。</p><p>Il viaggio: casella → <code>StrToInt</code> → conto → <code>IntToStr</code> → Caption.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">الرحلة: الخانة ← StrToInt ← الحساب ← IntToStr ← Caption.</p><p lang=\"zh\" style=\"color:#5b6573\">过程：输入框 → StrToInt → 计算 → IntToStr → Caption。</p><p>Se nella casella c'è <i>ciao</i>, <code>StrToInt</code> dà errore.</p><p lang=\"ar\" dir=\"rtl\" style=\"color:#5b6573\">إذا كانت في الخانة كلمة ciao، يعطي StrToInt خطأ.</p><p lang=\"zh\" style=\"color:#5b6573\">如果输入框里是 ciao，StrToInt 会出错。</p><pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">Edit1.Text   &#x27;7&#x27;  --StrToInt--&gt;  7  --(+1)--&gt;  8  --IntToStr--&gt;  &#x27;8&#x27;   Label1.Caption</pre>"
  }
 ],
 "allenamento": [
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Che cos'è una variabile?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ما هو المتغير؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">什么是变量？</span>",
   "o": [
    "una scatola con un nome, con dentro un valore",
    "un bottone della Form",
    "un errore di Lazarus"
   ],
   "a": 0,
   "spiega": "Ha un nome e un tipo; := ci mette dentro un valore.",
   "scheda": 1
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Quale di questi è una String?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">أيّ من هذه هو String؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">下面哪个是 String？</span>",
   "o": [
    "'Milano'",
    "25",
    "Milano senza apici"
   ],
   "a": 0,
   "spiega": "Le String stanno tra apici.",
   "scheda": 2
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Quale di questi è un Integer?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">أيّ من هذه هو Integer؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">下面哪个是 Integer？</span>",
   "o": [
    "15",
    "'15'",
    "3.5"
   ],
   "a": 0,
   "spiega": "Numero intero, senza apici e senza virgola.",
   "scheda": 3
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Che cosa dà '2' + '2'?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا تعطي '2' + '2'؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">'2' + '2' 得到什么？</span>",
   "o": [
    "'22'",
    "4",
    "'4'"
   ],
   "a": 0,
   "spiega": "Due String si attaccano.",
   "scheda": 4
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "L'utente scrive 10 in Edit1. Che cos'è Edit1.Text?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">المستخدم يكتب 10 في Edit1. ما هو Edit1.Text؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">用户在 Edit1 里写 10。Edit1.Text 是什么？</span>",
   "o": [
    "la String '10'",
    "l'Integer 10",
    "l'Integer 0"
   ],
   "a": 0,
   "spiega": "Quello che c'è in una casella è sempre testo.",
   "scheda": 5
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Vuoi mostrare il numero 8 in Label1.Caption. Che cosa usi?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">تريد أن تُظهر الرقم 8 في Label1.Caption. ماذا تستعمل؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你想在 Label1.Caption 里显示数字 8。用什么？</span>",
   "o": [
    "IntToStr(8)",
    "StrToInt(8)",
    "niente: Label1.Caption := 8;"
   ],
   "a": 0,
   "spiega": "IntToStr: da Integer a String.",
   "scheda": 6
  }
 ],
 "crocette": [
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "tipo",
   "q": "Che tipo è <code>'42'</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ما نوع <code>'42'</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>'42'</code> 是什么类型？</span>",
   "o": [
    "String",
    "Integer",
    "nessuno dei due"
   ],
   "a": 0,
   "spiega": "Ha gli apici: è testo."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "tipo",
   "q": "Che tipo è <code>42</code> (senza apici)?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ما نوع <code>42</code> (بلا علامات اقتباس)؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>42</code>（不带引号）是什么类型？</span>",
   "o": [
    "Integer",
    "String",
    "nessuno dei due"
   ],
   "a": 0,
   "spiega": "Numero intero senza apici."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "tipo",
   "q": "Che tipo è <code>'007'</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ما نوع <code>'007'</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>'007'</code> 是什么类型？</span>",
   "o": [
    "String",
    "Integer, perché sono cifre",
    "Integer: vale 7"
   ],
   "a": 0,
   "spiega": "Gli apici decidono: è testo, anche se ci sono cifre."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "tipo",
   "q": "Che tipo è <code>' 12'</code> (con uno spazio prima del 12)?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ما نوع <code>' 12'</code> (مع مسافة قبل 12)؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>' 12'</code>（12 前面有一个空格）是什么类型？</span>",
   "o": [
    "String",
    "Integer",
    "nessuno: è un errore"
   ],
   "a": 0,
   "spiega": "Ha gli apici: è testo, lo spazio fa parte del testo."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "tipo",
   "q": "Che tipo è <code>-5</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ما نوع <code>-5</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>-5</code> 是什么类型？</span>",
   "o": [
    "Integer",
    "String",
    "non è un numero"
   ],
   "a": 0,
   "spiega": "Gli Integer possono essere negativi."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "tipo",
   "q": "<code>3.5</code> è un Integer?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">هل <code>3.5</code> هو Integer؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>3.5</code> 是 Integer 吗？</span>",
   "o": [
    "no: ha la virgola, non è un numero intero",
    "sì",
    "no: è una String"
   ],
   "a": 0,
   "spiega": "Integer = solo numeri interi. 3.5 è un numero con la virgola (senza apici non è una String)."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "lazarus",
   "q": "L'utente scrive <b>15</b> nella casella Edit1. Che cos'è <code>Edit1.Text</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">يكتب المستخدم 15 في الخانة Edit1. ما هو <code>Edit1.Text</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">用户在输入框 Edit1 里写 15。<code>Edit1.Text</code> 是什么？</span>",
   "o": [
    "la String '15'",
    "l'Integer 15",
    "l'Integer 0"
   ],
   "a": 0,
   "spiega": "Il testo di una casella è sempre una String."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "lazarus",
   "q": "<code>var anno: String;</code> e poi <code>anno := '2026';</code>. Di che tipo è <code>anno</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\"><code>var anno: String;</code> ثم <code>anno := '2026';</code>. ما نوع <code>anno</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>var anno: String;</code> 然后 <code>anno := '2026';</code>。<code>anno</code> 是什么类型？</span>",
   "o": [
    "String, anche se dentro ci sono cifre",
    "Integer, perché 2026 è un numero",
    "cambia tipo da solo"
   ],
   "a": 0,
   "spiega": "Il tipo lo decide la riga var: la scatola anno è per il testo."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "conto",
   "q": "Che cosa dà <code>IntToStr(5) + '5'</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا يعطي <code>IntToStr(5) + '5'</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>IntToStr(5) + '5'</code> 得到什么？</span>",
   "o": [
    "la String '55'",
    "l'Integer 10",
    "la String '10'",
    "un errore"
   ],
   "a": 0,
   "spiega": "IntToStr(5) è '5'; due String si attaccano."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "conto",
   "q": "Che cosa dà <code>StrToInt('3') + 2</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا يعطي <code>StrToInt('3') + 2</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>StrToInt('3') + 2</code> 得到什么？</span>",
   "o": [
    "l'Integer 5",
    "la String '32'",
    "la String '5'",
    "un errore"
   ],
   "a": 0,
   "spiega": "StrToInt('3') è il numero 3; 3 + 2 = 5."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "conto",
   "q": "Che cosa dà <code>'3' + '4'</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا يعطي <code>'3' + '4'</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>'3' + '4'</code> 得到什么？</span>",
   "o": [
    "'34'",
    "7",
    "'7'"
   ],
   "a": 0,
   "spiega": "Due String si attaccano."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "conto",
   "q": "<code>a</code> e <code>b</code> sono Integer: <code>a := 2; b := 3;</code>. Che cosa mostra <code>Label1.Caption := IntToStr(a + b);</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">a و b من نوع Integer: <code>a := 2; b := 3;</code>. ماذا يُظهر <code>Label1.Caption := IntToStr(a + b);</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">a 和 b 是 Integer：<code>a := 2; b := 3;</code>。<code>Label1.Caption := IntToStr(a + b);</code> 显示什么？</span>",
   "o": [
    "5",
    "23",
    "un errore"
   ],
   "a": 0,
   "spiega": "Prima la somma (5), poi la traduzione in testo."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "conto",
   "q": "Stessi <code>a := 2; b := 3;</code>. Che cosa mostra <code>Label1.Caption := IntToStr(a) + IntToStr(b);</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">نفس <code>a := 2; b := 3;</code>. ماذا يُظهر <code>Label1.Caption := IntToStr(a) + IntToStr(b);</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">同样 <code>a := 2; b := 3;</code>。<code>Label1.Caption := IntToStr(a) + IntToStr(b);</code> 显示什么？</span>",
   "o": [
    "23",
    "5",
    "un errore"
   ],
   "a": 0,
   "spiega": "Prima diventano testo ('2' e '3'), poi si attaccano."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "conto",
   "q": "Che cosa dà <code>'Ciao' + 5</code>?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا يعطي <code>'Ciao' + 5</code>؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>'Ciao' + 5</code> 得到什么？</span>",
   "o": [
    "errore quando premi F9: non si attacca un Integer a una String",
    "'Ciao5'",
    "'Ciao 5'"
   ],
   "a": 0,
   "spiega": "Serve IntToStr: 'Ciao' + IntToStr(5)."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "errore",
   "q": "Quale riga dà errore quando premi F9 (Lazarus non la compila)?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">أيّ سطر يعطي خطأ عندما تضغط F9 (لا يترجمه Lazarus)؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">按 F9 时哪一行会出错（Lazarus 编译不了）？</span>",
   "o": [
    "Label1.Caption := 7;",
    "Label1.Caption := '7';",
    "Label1.Caption := IntToStr(7);",
    "Label1.Caption := '7' + '7';"
   ],
   "a": 0,
   "spiega": "La Caption vuole una String: 7 senza apici è un Integer."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "errore",
   "q": "<code>n</code> è un Integer. Quale riga è GIUSTA?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\"><code>n</code> من نوع Integer. أيّ سطر صحيح؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\"><code>n</code> 是 Integer。哪一行是对的？</span>",
   "o": [
    "n := StrToInt(Edit1.Text);",
    "n := Edit1.Text;",
    "n := 'Edit1.Text';",
    "n := IntToStr(Edit1.Text);"
   ],
   "a": 0,
   "spiega": "Edit1.Text è una String: per metterla in un Integer serve StrToInt."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "errore",
   "q": "Il programma esegue <code>n := StrToInt('ciao');</code>. Che cosa succede?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">البرنامج ينفّذ <code>n := StrToInt('ciao');</code>. ماذا يحدث؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">程序执行 <code>n := StrToInt('ciao');</code>。会发生什么？</span>",
   "o": [
    "parte, ma quando arriva a questa riga si ferma con un errore: 'ciao' non è un numero",
    "n vale 0",
    "n vale 4 (le lettere)",
    "n vale 'ciao'"
   ],
   "a": 0,
   "spiega": "StrToInt sa tradurre solo testo fatto di cifre."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "traccia",
   "q": "Che cosa mostra la Label alla fine?<pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">var s: String;\nbegin\n  s := &#x27;1&#x27;;\n  s := s + &#x27;1&#x27;;\n  s := s + &#x27;1&#x27;;\n  Label1.Caption := s;</pre><span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا تُظهر الـ Label في النهاية؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">最后 Label 显示什么？</span>",
   "o": [
    "111",
    "3",
    "1"
   ],
   "a": 0,
   "spiega": "s è una String: '1', poi '11', poi '111'."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "traccia",
   "q": "Che cosa mostra la Label alla fine?<pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">var n: Integer;\nbegin\n  n := 1;\n  n := n + n;\n  n := n + n;\n  Label1.Caption := IntToStr(n);</pre><span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا تُظهر الـ Label في النهاية؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">最后 Label 显示什么？</span>",
   "o": [
    "4",
    "2",
    "11",
    "1111"
   ],
   "a": 0,
   "spiega": "n è un Integer: 1, poi 2, poi 4."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "traccia",
   "q": "Nella casella Edit1 c'è scritto <b>7</b>. Che cosa mostra la Label?<pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">var n: Integer;\nbegin\n  n := StrToInt(Edit1.Text) + 3;\n  Label1.Caption := Edit1.Text + IntToStr(n);</pre><span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">في الخانة Edit1 مكتوب 7. ماذا تُظهر الـ Label؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">输入框 Edit1 里写着 7。Label 显示什么？</span>",
   "o": [
    "710",
    "10",
    "17",
    "73"
   ],
   "a": 0,
   "spiega": "n = 7 + 3 = 10; poi si attaccano '7' e '10'."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "traccia",
   "q": "Che cosa mostra la Label alla fine?<pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">var x: Integer; s: String;\nbegin\n  x := 4;\n  s := IntToStr(x) + IntToStr(x);\n  x := StrToInt(s) + 1;\n  Label1.Caption := IntToStr(x);</pre><span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا تُظهر الـ Label في النهاية؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">最后 Label 显示什么？</span>",
   "o": [
    "45",
    "9",
    "441",
    "8"
   ],
   "a": 0,
   "spiega": "s = '44'; StrToInt('44') + 1 = 45."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "traccia",
   "q": "Che cosa mostra la Label alla fine?<pre style=\"background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;white-space:pre-wrap\">var nome: String;\nbegin\n  nome := &#x27;Sara&#x27;;\n  Label1.Caption := &#x27;nome&#x27; + &#x27; &#x27; + nome;</pre><span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا تُظهر الـ Label في النهاية؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">最后 Label 显示什么？</span>",
   "o": [
    "nome Sara",
    "Sara Sara",
    "nome nome"
   ],
   "a": 0,
   "spiega": "'nome' tra apici è la parola; nome senza apici è la scatola che contiene Sara."
  }
 ],
 "aperte": [
  {
   "area": "mia",
   "tema": "mio",
   "q": "IL TUO SEGNAPUNTI (ora 3). Copia QUI SOTTO, scrivendola tu, la riga del TUO programma che trasforma il testo della casella Edit1 in un numero. Poi spiega con parole tue che cosa succederebbe se togliessi StrToInt.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">عدّاد نقاطك (الساعة 3). اكتب هنا بنفسك سطر برنامجك الذي يحوّل نص الخانة Edit1 إلى رقم. ثم اشرح بكلماتك ماذا يحدث لو حذفت StrToInt.</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你的记分牌（第 3 节）。在下面亲手写出你程序里把输入框 Edit1 的文字变成数字的那一行。再用你自己的话解释：如果去掉 StrToInt 会怎样。</span>",
   "aiuto": "Almeno 15 parole. Puoi scrivere anche nella tua lingua.",
   "min_parole": 15,
   "criteri": "riga vera con StrToInt(Edit1.Text) e il nome della propria variabile; senza StrToInt: errore Incompatible types, la casella è una String"
  },
  {
   "area": "mia",
   "tema": "mio",
   "q": "Sul tuo segnapunti c'è 12 e nella casella scrivi 5. Che numero vedi dopo Aggiungi? E che cosa vedresti se la riga fosse Label1.Caption := Label1.Caption + Edit1.Text; ? Spiega il perché con le parole String e Integer.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">على عدّاد نقاطك 12 وفي الخانة تكتب 5. أيّ رقم ترى بعد Aggiungi؟ وماذا سترى لو كان السطر Label1.Caption := Label1.Caption + Edit1.Text; ؟ اشرح السبب بكلمتي String و Integer.</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你的记分牌上是 12，输入框里写 5。按 Aggiungi 后看到几？如果那一行是 Label1.Caption := Label1.Caption + Edit1.Text; 会看到什么？用 String 和 Integer 这两个词解释原因。</span>",
   "aiuto": "Almeno 15 parole. Puoi scrivere anche nella tua lingua.",
   "min_parole": 15,
   "criteri": "17; con la riga sbagliata 125: le String si attaccano, gli Integer si sommano"
  },
  {
   "area": "mia",
   "tema": "mio",
   "q": "IL TUO SOPRANNOME (ora 2). Scrivi che cosa hai messo nelle due caselle e che cosa è comparso. Perché in quel programma NON serve StrToInt?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">لقبك (الساعة 2). اكتب ماذا وضعت في الخانتين وماذا ظهر. لماذا لا نحتاج StrToInt في ذلك البرنامج؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你的外号（第 2 节）。写出你在两个输入框里填了什么、出现了什么。为什么那个程序不需要 StrToInt？</span>",
   "aiuto": "Almeno 15 parole. Puoi scrivere anche nella tua lingua.",
   "min_parole": 15,
   "criteri": "valori propri delle caselle e frase comparsa; solo testo attaccato con +, nessun conto, quindi niente Integer"
  }
 ],
 "recupero": [
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Che cos'è una variabile?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ما هو المتغير؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">什么是变量？</span>",
   "o": [
    "una scatola con un nome, con dentro un valore",
    "un bottone della Form",
    "un errore di Lazarus"
   ],
   "a": 0,
   "spiega": "Ha un nome e un tipo; := ci mette dentro un valore."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Quale di questi è una String?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">أيّ من هذه هو String؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">下面哪个是 String？</span>",
   "o": [
    "'Milano'",
    "25",
    "Milano senza apici"
   ],
   "a": 0,
   "spiega": "Le String stanno tra apici."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Quale di questi è un Integer?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">أيّ من هذه هو Integer؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">下面哪个是 Integer？</span>",
   "o": [
    "15",
    "'15'",
    "3.5"
   ],
   "a": 0,
   "spiega": "Numero intero, senza apici e senza virgola."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Che cosa dà '2' + '2'?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">ماذا تعطي '2' + '2'؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">'2' + '2' 得到什么？</span>",
   "o": [
    "'22'",
    "4",
    "'4'"
   ],
   "a": 0,
   "spiega": "Due String si attaccano."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "L'utente scrive 10 in Edit1. Che cos'è Edit1.Text?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">المستخدم يكتب 10 في Edit1. ما هو Edit1.Text؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">用户在 Edit1 里写 10。Edit1.Text 是什么？</span>",
   "o": [
    "la String '10'",
    "l'Integer 10",
    "l'Integer 0"
   ],
   "a": 0,
   "spiega": "Quello che c'è in una casella è sempre testo."
  },
  {
   "tipo": "c",
   "area": "tipi",
   "tema": "",
   "q": "Vuoi mostrare il numero 8 in Label1.Caption. Che cosa usi?<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">تريد أن تُظهر الرقم 8 في Label1.Caption. ماذا تستعمل؟</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">你想在 Label1.Caption 里显示数字 8。用什么？</span>",
   "o": [
    "IntToStr(8)",
    "StrToInt(8)",
    "niente: Label1.Caption := 8;"
   ],
   "a": 0,
   "spiega": "IntToStr: da Integer a String."
  }
 ]
};
