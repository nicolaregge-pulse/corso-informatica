# -*- coding: utf-8 -*-
"""Sicurezza digitale — VOCI E VOLTI FALSI (deepfake): riconoscerli e difendersi. Per tutte le classi.

Genera, da un'unica fonte trilingue (IT · AR · ZH):
  1. docs/sicurezza-deepfake/index.html  — pagina unica per i ragazzi (bottoni lingua; ?lang=it|ar|zh)
  2. docs/quiz/banche/sicurezza-deepfake.js — banca del quiz personale (motore docs/quiz/)
  3. sicurezza-deepfake/sicurezza-deepfake.md — fonte MD (le 3 lingue, per l'IA dei ragazzi)
  4. sicurezza-deepfake/Deepfake-Voci-Volti-Falsi-{IT,AR,ZH}-vX.Y.pdf — 3 PDF monolingui
Uso: python3 sicurezza-deepfake/_build/gen_deepfake.py
"""
import html, json, os, subprocess

VERS = "1.0"
B = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(os.path.dirname(B))
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
QUIZ = "https://nicolaregge-pulse.github.io/corso-informatica/quiz/?b=sicurezza-deepfake&n=1"
LINGUE = {"it": "Italiano", "ar": "العربية", "zh": "中文"}

T = {
 "it": {
  "titolo": "Voci e volti falsi (deepfake)",
  "sotto": "Riconoscerli e difendersi · Sicurezza digitale",
  "carta": "Carta e penna sul banco: alla fine disegni lo schema «segnali d'allarme → cosa faccio».",
  "sez": [
   ("1. Che cos'è un deepfake", [
     "È un audio, una foto o un video FALSO, fatto con l'intelligenza artificiale (IA).",
     "Bastano pochi secondi della tua voce, o qualche foto del tuo viso, per imitarti.",
     "Sembra vero: ci cascano anche gli adulti."]),
   ("2. Come si usa per ingannare", [
     "Una telefonata o un vocale con la voce di un parente: «Sono nei guai, mandami subito dei soldi, non dirlo a nessuno».",
     "Un video di una persona famosa che regala telefoni o consiglia di investire soldi.",
     "Un audio o un video falso di un compagno per prenderlo in giro: è bullismo."]),
   ("3. I segnali d'allarme", [
     "FRETTA: «subito», «adesso», «non c'è tempo».",
     "SOLDI: ricariche, codici, password, dati della carta.",
     "SEGRETO: «non dirlo a nessuno».",
     "NUMERO sconosciuto o diverso dal solito.",
     "Attenzione: la voce può sembrare perfetta. Non fidarti dell'orecchio: controlla."]),
   ("4. Come difendersi", [
     "PAROLA D'ORDINE DI FAMIGLIA: decidete in casa una parola segreta. Se qualcuno chiede aiuto con la voce di un familiare, chiedetegli la parola.",
     "Chiudi e RICHIAMA TU, al numero che conosci già.",
     "Non mandare MAI soldi, codici o password per telefono o messaggio.",
     "Profili social privati; pochi vocali e video pubblici con la tua voce.",
     "Prima di condividere un video «incredibile», chiediti: è vero? Chi lo dice?"]),
   ("5. A scuola (regolamento)", [
     "È vietato registrare la voce o il viso di compagni e docenti senza il loro permesso.",
     "È vietato usare l'IA per imitare la voce o il volto di qualcuno, anche per scherzo. Può essere un reato."]),
   ("6. Se succede a te", [
     "Non è colpa tua e non ti devi vergognare.",
     "Dillo subito a un adulto di fiducia o al prof.",
     "Non cancellare niente: salva messaggi, numeri e link (fai gli screenshot).",
     "Si può denunciare alla Polizia Postale. Indirizzo internet, scrivilo esattamente così: commissariatodips.it"]),
  ],
  "compito_t": "7. Il compito",
  "compito": [
   "Apri il quiz personale con il bottone qui sotto. Scrivi nome e cognome, rispondi, premi Controlla. Alla fine premi il bottone verde Copia.",
   "Su Classroom apri il Documento del compito.",
   "Parte 1: incolla il quiz con Ctrl + V.",
   "Parte 2: leggi la storia e scrivi cosa fai, in 3 passi.",
   "Parte 3: scrivi come proporrai alla tua famiglia la parola d'ordine. NON scrivere la parola!",
   "Parte 4: cosa non ho capito.",
   "Premi il bottone blu in alto a destra (Consegna)."],
  "storia": "LA STORIA. Ricevi un vocale: è la voce di tuo cugino. Dice: «Ho perso il portafoglio, mandami 50 euro con una ricarica, subito, e non dirlo ai tuoi».",
  "quiz": "Apri il quiz personale",
 },
 "ar": {
  "titolo": "أصوات ووجوه مزيّفة (ديب فيك)",
  "sotto": "كيف نكتشفها وكيف نحمي أنفسنا · الأمان الرقمي",
  "carta": "الورقة والقلم على الطاولة: في النهاية ارسم المخطط «إشارات الخطر ← ماذا أفعل».",
  "sez": [
   ("1. ما هو الديب فيك؟", [
     "هو صوت أو صورة أو فيديو مزيّف، مصنوع بالذكاء الاصطناعي.",
     "تكفي ثوانٍ قليلة من صوتك، أو بعض صور وجهك، لتقليدك.",
     "يبدو حقيقياً: حتى الكبار ينخدعون به."]),
   ("2. كيف يُستعمل للخداع", [
     "مكالمة أو رسالة صوتية بصوت أحد الأقارب: «أنا في مشكلة، أرسل لي المال فوراً، ولا تخبر أحداً».",
     "فيديو لشخص مشهور يوزّع هواتف هدية أو ينصح باستثمار المال.",
     "صوت أو فيديو مزيّف لزميل للسخرية منه: هذا تنمّر."]),
   ("3. إشارات الخطر", [
     "الاستعجال: «فوراً»، «الآن»، «لا يوجد وقت».",
     "المال: شحن رصيد، رموز، كلمات سر، بيانات البطاقة.",
     "السرّ: «لا تخبر أحداً».",
     "رقم مجهول أو مختلف عن المعتاد.",
     "انتبه: قد يبدو الصوت مطابقاً تماماً. لا تثق بأذنك: تحقّق."]),
   ("4. كيف تحمي نفسك", [
     "كلمة سرّ للعائلة: اتفقوا في البيت على كلمة سرّية. إذا طلب أحد المساعدة بصوت أحد أفراد العائلة، اسألوه عن الكلمة.",
     "أغلق الخط واتصل أنت بالرقم الذي تعرفه.",
     "لا ترسل أبداً مالاً أو رموزاً أو كلمات سر عبر الهاتف أو الرسائل.",
     "اجعل حساباتك على مواقع التواصل خاصة؛ وقلّل الرسائل الصوتية والفيديوهات العامة بصوتك.",
     "قبل أن تشارك فيديو «لا يُصدَّق»، اسأل نفسك: هل هو حقيقي؟ من يقول ذلك؟"]),
   ("5. في المدرسة (النظام الداخلي)", [
     "ممنوع تسجيل صوت أو وجه الزملاء والأساتذة بدون إذنهم.",
     "ممنوع استعمال الذكاء الاصطناعي لتقليد صوت أو وجه أي شخص، حتى للمزاح. قد يكون ذلك جريمة."]),
   ("6. إذا حدث لك ذلك", [
     "ليس ذنبك، ولا داعي للخجل.",
     "أخبر فوراً شخصاً بالغاً تثق به أو الأستاذ.",
     "لا تحذف شيئاً: احفظ الرسائل والأرقام والروابط (التقط صوراً للشاشة).",
     "يمكن تقديم شكوى إلى شرطة الإنترنت (Polizia Postale). العنوان الإلكتروني، اكتبه هكذا تماماً: commissariatodips.it"]),
  ],
  "compito_t": "7. الواجب",
  "compito": [
   "افتح الاختبار الشخصي بالزر في الأسفل. اكتب اسمك ولقبك، أجب، ثم اضغط زر التحقق. في النهاية اضغط الزر الأخضر للنسخ.",
   "في Classroom افتح المستند الخاص بالواجب.",
   "الجزء 1: الصق الاختبار بالضغط على Ctrl + V.",
   "الجزء 2: اقرأ القصة واكتب ماذا تفعل، في 3 خطوات.",
   "الجزء 3: اكتب كيف ستقترح على عائلتك كلمة السرّ. لا تكتب الكلمة نفسها!",
   "الجزء 4: ما الذي لم أفهمه.",
   "اضغط الزر الأزرق في أعلى اليمين (للتسليم، بالإيطالية Consegna)."],
  "storia": "القصة: تصلك رسالة صوتية: إنه صوت ابن عمك. يقول: «أضعتُ محفظتي، أرسل لي 50 يورو بشحن رصيد، فوراً، ولا تخبر أهلك».",
  "quiz": "افتح الاختبار الشخصي",
 },
 "zh": {
  "titolo": "假声音和假面孔(深度伪造)",
  "sotto": "如何识别,如何保护自己 · 网络安全",
  "carta": "桌上放好纸和笔:最后画出示意图「危险信号 → 我该怎么做」。",
  "sez": [
   ("1. 什么是深度伪造?", [
     "它是用人工智能做出来的假的声音、照片或视频。",
     "只要你几秒钟的声音,或者几张你的脸部照片,就能模仿你。",
     "看起来很真:连大人也会上当。"]),
   ("2. 骗子怎么用它", [
     "用亲戚的声音打电话或发语音:「我遇到麻烦了,马上给我转钱,不要告诉任何人」。",
     "名人的视频,说要送手机,或者劝你投资。",
     "做同学的假声音或假视频来嘲笑他:这是欺凌。"]),
   ("3. 危险信号", [
     "催促:「马上」、「现在」、「没有时间了」。",
     "要钱:充值、验证码、密码、银行卡信息。",
     "保密:「不要告诉任何人」。",
     "陌生号码,或者和平时不一样的号码。",
     "注意:声音可能一模一样。不要相信耳朵:要核实。"]),
   ("4. 如何保护自己", [
     "家庭暗号:在家里约定一个秘密词语。如果有人用家人的声音求助,就问他暗号。",
     "挂断电话,由你自己打回到你已经知道的号码。",
     "绝对不要通过电话或消息发送钱、验证码或密码。",
     "社交账号设为私密;少发带有你声音的公开语音和视频。",
     "转发一个「难以置信」的视频之前,问问自己:这是真的吗?是谁说的?"]),
   ("5. 在学校(校规)", [
     "未经同意,禁止录下同学和老师的声音或脸。",
     "禁止用人工智能模仿任何人的声音或脸,开玩笑也不行。这可能是犯罪。"]),
   ("6. 如果发生在你身上", [
     "这不是你的错,不用感到羞耻。",
     "马上告诉一个你信任的大人或老师。",
     "什么都不要删除:保存消息、号码和链接(截屏)。",
     "可以向网络警察(Polizia Postale)报案。网址,请完全照这样写:commissariatodips.it"]),
  ],
  "compito_t": "7. 作业",
  "compito": [
   "点下面的按钮打开个人测验。写你的姓名,回答问题,点检查按钮。最后点绿色的复制按钮。",
   "在 Classroom 里打开作业的文档。",
   "第 1 部分:按 Ctrl + V 粘贴测验结果。",
   "第 2 部分:读下面的故事,写出你会怎么做,分 3 步。",
   "第 3 部分:写你会怎样向家人提议设立暗号。不要写出暗号本身!",
   "第 4 部分:我没有听懂的地方。",
   "点右上角的蓝色按钮(提交,意大利语是 Consegna)。"],
  "storia": "故事:你收到一条语音,是你表哥的声音。他说:「我把钱包丢了,马上给我充值 50 欧元,不要告诉你爸妈」。",
  "quiz": "打开个人测验",
 },
}

# quiz: (domanda, [opzioni], indice giusto) — ogni testo in IT, AR, ZH
Q = [
 (("Che cos'è un deepfake?", "ما هو الديب فيك؟", "什么是深度伪造?"),
  [("Un audio, una foto o un video falso fatto con l'IA", "صوت أو صورة أو فيديو مزيّف مصنوع بالذكاء الاصطناعي", "用人工智能做的假声音、照片或视频"),
   ("Un virus del computer", "فيروس كمبيوتر", "一种电脑病毒"), ("Un tipo di password", "نوع من كلمات السر", "一种密码"), ("Un social network", "موقع تواصل اجتماعي", "一个社交网络")], 0),
 (("Quanta voce serve all'IA per imitare una persona?", "كم من الصوت يحتاج الذكاء الاصطناعي لتقليد شخص؟", "人工智能需要多少声音才能模仿一个人?"),
  [("Pochi secondi", "ثوانٍ قليلة", "几秒钟"), ("Almeno 10 ore", "10 ساعات على الأقل", "至少 10 个小时"),
   ("Serve la persona davanti", "يجب أن يكون الشخص حاضراً", "这个人必须在场"), ("Non è possibile", "هذا غير ممكن", "不可能")], 0),
 (("Ricevi un vocale con la voce di tua madre che chiede subito dei soldi. Cosa fai per prima cosa?", "تصلك رسالة صوتية بصوت أمك تطلب المال فوراً. ماذا تفعل أولاً؟", "你收到一条妈妈声音的语音,要你马上转钱。你首先做什么?"),
  [("Chiudo e la richiamo al suo numero", "أغلق وأتصل بها على رقمها", "挂断,然后打她的号码"), ("Mando subito i soldi", "أرسل المال فوراً", "马上转钱"),
   ("Rispondo con la mia password", "أرد بكلمة السر الخاصة بي", "回复我的密码"), ("Inoltro il vocale a tutti", "أرسل الرسالة للجميع", "把语音转发给所有人")], 0),
 (("Quale di queste frasi è un segnale d'allarme?", "أيّ من هذه الجمل إشارة خطر؟", "下面哪句话是危险信号?"),
  [("«Fai presto e non dirlo a nessuno»", "«أسرع ولا تخبر أحداً»", "「快点,不要告诉任何人」"), ("«Ci vediamo a cena»", "«نلتقي على العشاء»", "「晚饭见」"),
   ("«Buon compleanno»", "«عيد ميلاد سعيد»", "「生日快乐」"), ("«Ho finito i compiti»", "«أنهيت واجباتي»", "「我做完作业了」")], 0),
 (("A cosa serve la parola d'ordine di famiglia?", "ما فائدة كلمة سرّ العائلة؟", "家庭暗号有什么用?"),
  [("A capire se chi chiama è davvero un familiare", "لمعرفة إن كان المتصل فعلاً من العائلة", "确认打电话的人真的是家人"), ("A entrare in Instagram", "للدخول إلى إنستغرام", "登录 Instagram"),
   ("A pagare online", "للدفع عبر الإنترنت", "网上付款"), ("A sbloccare il telefono", "لفتح قفل الهاتف", "解锁手机")], 0),
 (("La voce al telefono sembra proprio quella di tuo zio. Allora...", "الصوت في الهاتف يشبه تماماً صوت عمك. إذن...", "电话里的声音和你叔叔一模一样。那么……"),
  [("Può essere falsa lo stesso: controllo", "قد يكون مزيّفاً رغم ذلك: أتحقّق", "也可能是假的:我要核实"), ("È sicuramente lui", "إنه هو بالتأكيد", "肯定是他"),
   ("Gli do il codice della carta", "أعطيه رمز البطاقة", "把银行卡验证码给他"), ("Gli mando la foto dei documenti", "أرسل له صورة الوثائق", "把证件照片发给他")], 0),
 (("Un compagno crea con l'IA un audio finto con la voce del prof. Com'è?", "زميل يصنع بالذكاء الاصطناعي صوتاً مزيّفاً بصوت الأستاذ. ما رأيك؟", "一个同学用人工智能做了老师声音的假录音。这怎么样?"),
  [("È vietato e può essere un reato", "ممنوع وقد يكون جريمة", "这是禁止的,可能是犯罪"), ("È uno scherzo permesso", "مزاح مسموح", "这是允许的玩笑"),
   ("Va bene se fa ridere", "لا بأس إن كان مضحكاً", "好笑就可以"), ("Va bene se lo vedono in pochi", "لا بأس إن رآه قليلون", "很少人看到就可以")], 0),
 (("Qualcuno ha messo in rete un video falso con il tuo viso. Cosa fai?", "نشر أحدهم فيديو مزيّفاً بوجهك. ماذا تفعل؟", "有人在网上发了用你的脸做的假视频。你怎么办?"),
  [("Lo dico a un adulto di fiducia e salvo le prove", "أخبر شخصاً بالغاً أثق به وأحفظ الأدلة", "告诉信任的大人,并保存证据"), ("Sto zitto e cancello tutto", "أسكت وأحذف كل شيء", "不说话,全部删除"),
   ("Rispondo con insulti", "أرد بالشتائم", "用脏话回击"), ("Faccio un video falso anch'io", "أصنع أنا أيضاً فيديو مزيّفاً", "我也做一个假视频")], 0),
 (("Come si riduce il rischio di essere imitati?", "كيف نقلّل خطر أن يقلّدنا أحد؟", "怎样减少被模仿的风险?"),
  [("Profilo social privato e pochi vocali pubblici", "حساب خاص ورسائل صوتية عامة قليلة", "社交账号设为私密,少发公开语音"), ("Pubblicare tanti video con la mia voce", "نشر فيديوهات كثيرة بصوتي", "发很多有我声音的视频"),
   ("Dare il mio numero a tutti", "إعطاء رقمي للجميع", "把我的号码给所有人"), ("Usare la stessa password ovunque", "استعمال كلمة السر نفسها في كل مكان", "到处用同一个密码")], 0),
 (("Un video mostra un calciatore famoso che regala telefoni: basta cliccare e pagare la spedizione.", "فيديو يُظهر لاعب كرة مشهوراً يوزّع هواتف: يكفي أن تضغط وتدفع ثمن الشحن.", "一个视频里,著名足球运动员送手机:只要点一下,付运费就行。"),
  [("Probabilmente è una truffa con un deepfake", "على الأرجح احتيال بالديب فيك", "很可能是用深度伪造的诈骗"), ("È vero perché c'è il suo viso", "إنه حقيقي لأن وجهه موجود", "是真的,因为有他的脸"),
   ("Clicco subito", "أضغط فوراً", "马上点"), ("Lo mando a tutti i compagni", "أرسله لكل الزملاء", "发给所有同学")], 0),
 (("Posso registrare la voce del prof durante la lezione?", "هل يمكنني تسجيل صوت الأستاذ أثناء الدرس؟", "上课时我可以录老师的声音吗?"),
  [("Solo con il suo permesso", "فقط بإذنه", "只有在他同意的情况下"), ("Sì, sempre", "نعم، دائماً", "可以,随时"),
   ("Sì, se lo metto su TikTok", "نعم، إذا نشرته على تيك توك", "可以,如果我发到 TikTok 上"), ("Sì, se non se ne accorge", "نعم، إذا لم ينتبه", "可以,如果他没发现")], 0),
 (("A chi si può denunciare un deepfake?", "لمن يمكن تقديم شكوى عن الديب فيك؟", "可以向谁举报深度伪造?"),
  [("Alla Polizia Postale", "إلى شرطة الإنترنت (Polizia Postale)", "向网络警察(Polizia Postale)"), ("Al negozio di telefoni", "إلى متجر الهواتف", "向手机店"),
   ("A nessuno", "لا أحد", "不能向任何人"), ("A chi l'ha fatto, per chiedere scusa", "إلى من صنعه لأعتذر", "向做这件事的人道歉")], 0),
]


def L(t):
    return {"it": t[0], "ar": t[1], "zh": t[2]}


def banca():
    d = {"titolo": "Sicurezza — Voci e volti falsi (deepfake)",
         "sotto": "Tutte le classi · Sicurezza digitale · ognuno ha le sue domande · لكل واحد أسئلته · 每个人的题目都不一样",
         "regola": {k: " ".join(T[k]["sez"][2][1][:4]) for k in T},
         "quante": 8,
         "domande": [{"q": L(q), "o": [L(o) for o in opz], "a": a} for q, opz, a in Q]}
    js = "// Sicurezza digitale — deepfake (trilingue IT · AR · ZH). Generato da sicurezza-deepfake/_build/gen_deepfake.py\nwindow.BANCA = " + json.dumps(d, ensure_ascii=False, indent=1) + ";\n"
    open(os.path.join(R, "docs", "quiz", "banche", "sicurezza-deepfake.js"), "w", encoding="utf-8").write(js)


def blocco(k):
    t, e = T[k], html.escape
    rtl = " dir='rtl'" if k == "ar" else ""
    h = "<section class='lang %s' lang='%s'%s><h1>%s</h1><p class='sub'>%s</p><p class='carta'>%s</p>" % (k, k, rtl, e(t["titolo"]), e(t["sotto"]), e(t["carta"]))
    for titolo, voci in t["sez"]:
        h += "<h2>%s</h2><ol>%s</ol>" % (e(titolo), "".join("<li>%s</li>" % e(v) for v in voci))
    h += "<h2>%s</h2><div class='storia'>%s</div><ol>%s</ol>" % (e(t["compito_t"]), e(t["storia"]), "".join("<li>%s</li>" % e(v) for v in t["compito"]))
    h += "<a class='quiz' href='%s'>%s</a></section>" % (QUIZ, e(t["quiz"]))
    return h


def pagina():
    css = """@font-face{font-family:Amiri;src:url('amiri.woff2') format('woff2')}
:root{--blu:#12467a}*{box-sizing:border-box}body{margin:0;background:#f4f7fb;color:#1a2330;font-family:"Segoe UI",Arial,'WenQuanYi Zen Hei',sans-serif}
.w{max-width:820px;margin:0 auto;padding:14px 16px 50px}.bott{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 10px}
.bott button{font-size:18px;padding:8px 16px;border:2px solid #9cc0e4;background:#fff;color:var(--blu);border-radius:10px;cursor:pointer}.bott button.on{background:var(--blu);color:#fff}
h1{color:var(--blu);font-size:26px;margin:6px 0 2px}.sub{color:#556;margin:0 0 8px}h2{color:var(--blu);font-size:20px;margin:18px 0 6px;border-bottom:2px solid #c9d8ea;break-after:avoid}
ol{font-size:18px;line-height:1.5;padding-left:26px}li{margin:4px 0}section[dir=rtl] ol{padding-left:0;padding-right:26px}
section[dir=rtl]{font-family:Amiri,'Traditional Arabic',serif;font-size:19px}.carta{background:#fff8dc;border-left:6px solid #d4a017;padding:8px 12px;border-radius:8px}
section[dir=rtl] .carta,section[dir=rtl] .storia{border-left:0;border-right:6px solid}
.storia{background:#e8f1fb;border-left:6px solid #1f6fa5;padding:10px 12px;border-radius:8px;font-size:18px}
.quiz{display:block;text-align:center;background:#2f9e57;color:#fff;font-size:20px;font-weight:800;border-radius:12px;padding:14px;margin:14px 0;text-decoration:none}
.lang{display:none}.lang.on{display:block}.ver{color:#889;font-size:12px}
@media print{.bott,.quiz{display:none}body{background:#fff}}"""
    js = """var q=new URLSearchParams(location.search).get('lang')||'it';
function mostra(l){document.querySelectorAll('.lang').forEach(function(s){s.classList.toggle('on',s.classList.contains(l))});
document.querySelectorAll('.bott button').forEach(function(b){b.classList.toggle('on',b.dataset.l==l)})}mostra(q);"""
    bott = "".join("<button data-l='%s' onclick=\"mostra('%s')\">%s</button>" % (k, k, v) for k, v in LINGUE.items())
    doc = ("<!doctype html><html lang='it'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
           "<title>Voci e volti falsi (deepfake)</title><style>%s</style></head><body><div class='w'><div class='bott'>%s</div>%s"
           "<p class='ver'>Versione %s</p></div><script>%s</script></body></html>") % (css, bott, "".join(blocco(k) for k in T), VERS, js)
    d = os.path.join(R, "docs", "sicurezza-deepfake")
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(doc)
    import shutil
    shutil.copy(os.path.join(B, "amiri.woff2"), os.path.join(d, "amiri.woff2"))
    for k in T:
        out = os.path.join(R, "sicurezza-deepfake", "Deepfake-Voci-Volti-Falsi-%s-v%s.pdf" % (k.upper(), VERS))
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=2000",
                        "--print-to-pdf=" + out, "file://%s/index.html?lang=%s" % (d, k)], capture_output=True)
        print(out)


def md():
    righe = ["# Voci e volti falsi (deepfake) — riconoscerli e difendersi", "", "**Versione %s** — 06/10/2026 — Sicurezza digitale, tutte le classi." % VERS, "",
             "*Fonte trilingue (italiano, arabo, cinese semplificato). Pagina per i ragazzi: `docs/sicurezza-deepfake/`; quiz: `docs/quiz/?b=sicurezza-deepfake&n=1`.*", ""]
    for k, nome in LINGUE.items():
        t = T[k]
        righe += ["## %s — %s" % (nome, t["titolo"]), "", t["sotto"], "", t["carta"], ""]
        for titolo, voci in t["sez"] + [(t["compito_t"], [t["storia"]] + t["compito"])]:
            righe += ["### " + titolo, ""] + ["%d. %s" % (i + 1, v) for i, v in enumerate(voci)] + [""]
    righe += ["## Registro delle versioni", "", "1. **v1.0 (06/10/2026)**: prima versione."]
    open(os.path.join(R, "sicurezza-deepfake", "sicurezza-deepfake.md"), "w", encoding="utf-8").write("\n".join(righe) + "\n")


if __name__ == "__main__":
    banca()
    md()
    pagina()
