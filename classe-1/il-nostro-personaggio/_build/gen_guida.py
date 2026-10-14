# -*- coding: utf-8 -*-
"""Mini-guida «Il nostro personaggio» (1INF, 14/10/2026): ritagliare, salvare, caricare sul Modulo, Gemini Immagini.
Una sola fonte (i dati qui sotto) -> MD + HTML + PDF, in tre lingue (IT, AR, ZH).
Uso: python3 classe-1/il-nostro-personaggio/_build/gen_guida.py"""
import html, os, shutil, subprocess

VER = "1.0"
DATA = "14/10/2026"
QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(QUI))
PDF = f"20261014_Il-Nostro-Personaggio_Classe-1-PerTutti_multilingua_v{VER}.pdf"
MODULO = "https://docs.google.com/forms/d/e/1FAIpQLSdmNWUBtzzCzKNXQSH9X0A7q85F8AKLPCM2k_JBt-N8QYHkLA/viewform"
GEMINI = "gemini.google.com"

FRASE = ("Trasforma questa foto in un personaggio cartoonesco, stile cartone animato: solo la testa, simpatico e sorridente. Immagine quadrata, sfondo bianco.",
         "حوّل هذه الصورة إلى شخصية كرتونية بأسلوب الرسوم المتحركة: الرأس فقط، لطيفة ومبتسمة. صورة مربعة، خلفية بيضاء.",
         "把这张照片变成一个卡通人物：只要头，可爱、在笑。正方形图片，白色背景。")

# ogni passo: (italiano, arabo, cinese) e, se serve, un riquadro da copiare
CAPITOLI = [
 ("00", ("A che cosa serve", "لماذا هذا الدليل", "这份指南有什么用"), [
  (("Oggi il tuo personaggio entra nel gioco della classe. Ti servono due immagini: la tua foto (solo la testa) e il tuo personaggio cartoonesco fatto con Gemini.",
    "اليوم تدخل شخصيتك لعبة الصف. تحتاج صورتين: صورتك (الرأس فقط) وشخصيتك الكرتونية المصنوعة بـ Gemini.",
    "今天你的角色要进入全班的游戏。你需要两张图片：你的照片（只要头）和用 Gemini 做的卡通角色。"), None),
  (("Usa solo una foto tua. Mai foto dei compagni o di altre persone.",
    "استعمل صورتك أنت فقط. لا تستعمل أبدًا صور زملائك أو أشخاص آخرين.",
    "只用你自己的照片。绝不用同学或别人的照片。"), None),
 ]),
 ("01a", ("Ritagliare la foto: dal telefono", "قصّ الصورة: من الهاتف", "裁剪照片：用手机"), [
  (("Apri l'app delle foto: «Galleria» sui telefoni Android, «Foto» sull'iPhone.", "افتح تطبيق الصور: «Galleria» (المعرض) في هواتف أندرويد، «Foto» (الصور) في آيفون.", "打开相册应用：安卓手机是「Galleria」（图库），苹果手机是「Foto」（照片）。"), None),
  (("Tocca la tua foto per aprirla.", "المس صورتك لفتحها.", "点你的照片，打开它。"), None),
  (("In basso tocca la matita «Modifica».", "في الأسفل المس القلم «Modifica» (تعديل).", "在下面点铅笔图标「Modifica」（编辑）。"), None),
  (("Tocca l'icona del ritaglio: un quadrato con le frecce agli angoli.", "المس أيقونة القص: مربع بأسهم في الزوايا.", "点裁剪图标：一个四角有箭头的方框。"), None),
  (("Scegli la forma quadrata: «1:1» oppure «Quadrato».", "اختر الشكل المربع: «1:1» أو «Quadrato» (مربع).", "选正方形：「1:1」或「Quadrato」（正方形）。"), None),
  (("Trascina gli angoli finché nel quadrato resta solo la tua testa.", "اسحب الزوايا حتى يبقى رأسك فقط داخل المربع.", "拖动四个角，直到方框里只剩下你的头。"), None),
  (("In alto tocca «Salva copia» (o «Salva»). Fatto: la foto ritagliata è in Galleria.", "في الأعلى المس «Salva copia» (حفظ نسخة) أو «Salva» (حفظ). تمّ: الصورة المقصوصة في المعرض.", "在上面点「Salva copia」（另存一份）或「Salva」（保存）。好了：裁好的照片在相册里。"), None),
 ]),
 ("01b", ("Ritagliare la foto: dal PC della scuola", "قصّ الصورة: من حاسوب المدرسة", "裁剪照片：用学校的电脑"), [
  (("Apri la tua foto sullo schermo: per esempio la foto del tuo profilo social, nel browser.", "افتح صورتك على الشاشة: مثلًا صورة حسابك في وسائل التواصل، داخل المتصفح.", "在屏幕上打开你的照片：比如在浏览器里打开你社交账号的头像。"), None),
  (("Premi insieme tre tasti: Windows, Maiusc e S.", "اضغط معًا ثلاثة مفاتيح: Windows و Shift (Maiusc) و S.", "同时按三个键：Windows、Shift（Maiusc）和 S。"), "Windows + Maiusc + S"),
  (("Lo schermo diventa più scuro. Tieni premuto il tasto sinistro del mouse e disegna un quadrato intorno alla tua testa.", "تصبح الشاشة أغمق. اضغط زر الفأرة الأيسر باستمرار وارسم مربعًا حول رأسك.", "屏幕变暗。按住鼠标左键，在你的头周围画一个方框。"), None),
  (("Lascia il mouse. In basso a destra compare un riquadro «Strumento di cattura»: cliccalo. La foto ritagliata si apre.", "اترك الفأرة. في الأسفل على اليمين يظهر مربع «Strumento di cattura» (أداة القص): انقر عليه. تُفتح الصورة المقصوصة.", "松开鼠标。右下角出现「Strumento di cattura」（截图工具）的小窗口：点它。裁好的照片就打开了。"), None),
 ]),
 ("02", ("Salvare con il nome giusto", "الحفظ بالاسم الصحيح", "用正确的名字保存"), [
  (("Il nome giusto è: classe, cognome e nome, che cosa è. Senza spazi e senza accenti. Per la foto:", "الاسم الصحيح هو: الصف، اسم العائلة والاسم، ما هي. بدون فراغات وبدون علامات. للصورة:", "正确的名字是：班级、姓和名、是什么。不要空格，不要重音符号。照片这样写："), "1INF_cognome-nome_foto.png"),
  (("Per il personaggio fatto con Gemini:", "للشخصية المصنوعة بـ Gemini:", "用 Gemini 做的角色这样写："), "1INF_cognome-nome_cartoon.png"),
  (("Al posto di «cognome-nome» scrivi i tuoi, per esempio 1INF_rossi-mario_foto.png.", "مكان «cognome-nome» اكتب اسمك، مثلًا 1INF_rossi-mario_foto.png.", "把「cognome-nome」换成你的姓和名，比如 1INF_rossi-mario_foto.png。"), None),
  (("Sul PC: nella finestra «Strumento di cattura», in alto a destra clicca il dischetto «Salva».", "على الحاسوب: في نافذة «Strumento di cattura»، في الأعلى على اليمين انقر على القرص «Salva» (حفظ).", "在电脑上：在「Strumento di cattura」窗口里，点右上角的软盘图标「Salva」（保存）。"), None),
  (("A sinistra clicca la cartella «Immagini».", "على اليسار انقر على مجلد «Immagini» (الصور).", "在左边点文件夹「Immagini」（图片）。"), None),
  (("In basso clicca nella casella «Nome file», cancella e scrivi il nome giusto.", "في الأسفل انقر في خانة «Nome file» (اسم الملف)، امسح واكتب الاسم الصحيح.", "在下面点「Nome file」（文件名）框，删掉原来的，写正确的名字。"), None),
  (("Clicca il bottone «Salva».", "انقر على زر «Salva» (حفظ).", "点「Salva」（保存）按钮。"), None),
  (("Sul telefono il nome lo sceglie il telefono: va bene così.", "في الهاتف، الهاتف يختار الاسم: لا مشكلة.", "在手机上，名字由手机自己起：这样也可以。"), None),
 ]),
 ("03", ("Caricare la foto sul Modulo della consegna", "رفع الصورة إلى نموذج التسليم", "把照片上传到交作业的表单"), [
  (("Apri il compito su Classroom e clicca il Modulo «Consegna». Oppure apri questo indirizzo (scrivilo esattamente così):", "افتح الواجب في Classroom وانقر على النموذج «Consegna» (التسليم). أو افتح هذا العنوان (اكتبه تمامًا هكذا):", "在 Classroom 打开作业，点表单「Consegna」（提交）。或者打开这个网址（照原样输入）："), MODULO),
  (("Se te lo chiede, entra con l'account della scuola.", "إذا طُلب منك، ادخل بحساب المدرسة.", "如果要求登录，用学校的账号登录。"), None),
  (("Prima casella «Cosa consegni?»: scrivi foto.", "الخانة الأولى «Cosa consegni?» (ماذا تسلّم؟): اكتب foto.", "第一个框「Cosa consegni?」（你交什么？）：写 foto。"), "foto"),
  (("Seconda casella: scrivi il mio personaggio.", "الخانة الثانية: اكتب il mio personaggio.", "第二个框：写 il mio personaggio。"), "il mio personaggio"),
  (("Clicca il bottone «Aggiungi file» (ha una freccia in su).", "انقر على زر «Aggiungi file» (إضافة ملف)، عليه سهم إلى الأعلى.", "点「Aggiungi file」（添加文件）按钮，上面有一个向上的箭头。"), None),
  (("Nella finestra che si apre clicca il bottone blu «Sfoglia».", "في النافذة التي تُفتح انقر على الزر الأزرق «Sfoglia» (تصفّح).", "在打开的窗口里点蓝色按钮「Sfoglia」（浏览）。"), None),
  (("Scegli il tuo file (1INF_cognome-nome_foto.png) e clicca «Apri».", "اختر ملفك (1INF_cognome-nome_foto.png) وانقر «Apri» (فتح).", "选你的文件（1INF_cognome-nome_foto.png），点「Apri」（打开）。"), None),
  (("Se compare, clicca «Carica».", "إذا ظهر، انقر «Carica» (رفع).", "如果出现，点「Carica」（上传）。"), None),
  (("In basso clicca il bottone viola «Invia». Compare «Ricevuto»: fatto!", "في الأسفل انقر على الزر البنفسجي «Invia» (إرسال). يظهر «Ricevuto» (تم الاستلام): تمّ!", "在下面点紫色按钮「Invia」（发送）。出现「Ricevuto」（收到了）：完成！"), None),
 ]),
 ("04", ("Gemini Immagini: il personaggio cartoonesco", "Gemini Immagini: الشخصية الكرتونية", "Gemini 图片：卡通角色"), [
  (("Apri una scheda nuova (Ctrl+T) e scrivi questo indirizzo, poi premi Invio:", "افتح تبويبًا جديدًا (Ctrl+T) واكتب هذا العنوان، ثم اضغط Enter:", "打开一个新标签页（Ctrl+T），输入这个网址，然后按回车："), GEMINI),
  (("Se te lo chiede, entra con l'account della scuola.", "إذا طُلب منك، ادخل بحساب المدرسة.", "如果要求登录，用学校的账号登录。"), None),
  (("In basso, a sinistra della casella dove si scrive, clicca il «+».", "في الأسفل، على يسار الخانة التي تكتب فيها، انقر على «+».", "在下面输入框的左边，点「+」。"), None),
  (("Clicca «Carica file», scegli la tua foto (1INF_cognome-nome_foto.png) e clicca «Apri».", "انقر «Carica file» (رفع ملف)، اختر صورتك (1INF_cognome-nome_foto.png) وانقر «Apri» (فتح).", "点「Carica file」（上传文件），选你的照片（1INF_cognome-nome_foto.png），点「Apri」（打开）。"), None),
  (("Sotto la casella clicca «Immagini» (o «Crea immagine»).", "تحت الخانة انقر «Immagini» (صور) أو «Crea immagine» (إنشاء صورة).", "在输入框下面点「Immagini」（图片）或「Crea immagine」（创建图片）。"), None),
  (("Nella casella scrivi la frase nella tua lingua:", "في الخانة اكتب الجملة بلغتك:", "在输入框里写你的语言的这句话："), "FRASE"),
  (("Aggiungi una cosa tua (il tuo sport, la tua squadra, il tuo colore) e premi Invio. Aspetta qualche secondo.", "أضف شيئًا عنك (رياضتك، فريقك، لونك) واضغط Enter. انتظر بضع ثوانٍ.", "加一点你自己的东西（你的运动、你的球队、你的颜色），按回车。等几秒钟。"), None),
  (("Non ti piace? Scrivi che cosa cambiare, per esempio «più colorato», e premi Invio.", "لم يعجبك؟ اكتب ماذا تغيّر، مثلًا «più colorato» (ألوان أكثر)، واضغط Enter.", "不喜欢？写要改什么，比如「più colorato」（更多颜色），按回车。"), None),
  (("Ti piace? Passa il mouse sull'immagine e clicca la freccia in giù «Scarica».", "أعجبك؟ مرّر الفأرة فوق الصورة وانقر على السهم إلى الأسفل «Scarica» (تنزيل).", "喜欢吗？把鼠标移到图片上，点向下的箭头「Scarica」（下载）。"), None),
  (("Salvala con il nome giusto (capitolo 02): 1INF_cognome-nome_cartoon.png.", "احفظها بالاسم الصحيح (الفصل 02): 1INF_cognome-nome_cartoon.png.", "用正确的名字保存（第02章）：1INF_cognome-nome_cartoon.png。"), None),
  (("Caricala sul Modulo come nel capitolo 03, ma nella prima casella scrivi cartoon.", "ارفعها إلى النموذج كما في الفصل 03، لكن في الخانة الأولى اكتب cartoon.", "像第03章那样上传到表单，但第一个框写 cartoon。"), "cartoon"),
  (("Fatto! Il prof la controlla e il tuo personaggio entra nel gioco della classe.", "تمّ! الأستاذ يتحقق منها وتدخل شخصيتك لعبة الصف.", "完成！老师检查后，你的角色就进入全班的游戏。"), None),
 ]),
]
TITOLO = ("Il nostro personaggio · mini-guida", "شخصيتنا · دليل صغير", "我们的角色 · 小指南")


def md():
    r = [f"# {TITOLO[0]}", "", f"**Versione {VER}** — {DATA} — Classe 1 (1INF) · Per tutti · italiano, العربية, 中文", "",
         f"*{TITOLO[1]} · {TITOLO[2]}*", ""]
    for num, tit, passi in CAPITOLI:
        r += [f"## {num} {tit[0]}", "", f"*{tit[1]} · {tit[2]}*", ""]
        for i, (t, box) in enumerate(passi, 1):
            r += [f"{i}. {t[0]}", f"   {t[1]}", f"   {t[2]}"]
            if box == "FRASE":
                for f in FRASE: r += ["", "   ```", f"   {f}", "   ```"]
            elif box:
                r += ["", "   ```", f"   {box}", "   ```"]
            r.append("")
    r += ["## 05 Registro delle versioni", "", f"1. **v1.0 ({DATA}):** prima stesura per la lezione «Il nostro personaggio» (ritagliare, salvare, Modulo, Gemini Immagini).", ""]
    return "\n".join(r)


def pag():
    e = html.escape
    css = """@page{size:A4;margin:14mm}*{box-sizing:border-box}body{margin:0;background:#fbfaf7;color:#111;font:16px/1.5 "DejaVu Sans",system-ui,Arial,sans-serif}
.w{max-width:860px;margin:0 auto;padding:16px}h1{font-size:28px;margin:0 0 2px}h2{font-size:21px;margin:22px 0 8px;padding:6px 10px;border-radius:8px;background:#eef3f8;border:1px solid #d8dee6;break-after:avoid}
.ar{direction:rtl;text-align:right;font-family:"Amiri",serif;font-size:19px;color:#3b4552}.zh{font-family:"WenQuanYi Zen Hei",sans-serif;color:#3b4552}
ol{padding-left:26px;margin:0}li{margin:0 0 10px;break-inside:avoid}.it{font-weight:600}
.box{display:flex;align-items:center;gap:8px;margin:4px 0}.box code{font:15px "DejaVu Sans Mono",monospace;background:#fff6d6;border:1px solid #e6d79a;border-radius:6px;padding:4px 8px;word-break:break-all}
.box button{font:inherit;font-size:14px;border:0;border-radius:6px;background:#1f6feb;color:#fff;padding:4px 10px;cursor:pointer}.t{color:#5d6878;font-size:14px}
@media print{.box button{display:none}body{background:#fff}}"""
    def box(t):
        return f'<div class="box"><code>{e(t)}</code><button onclick="navigator.clipboard.writeText(this.previousSibling.textContent);this.textContent=\'Copiato ✓\'">Copia</button></div>'
    h = [f'<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Il nostro personaggio</title><style>{css}</style></head><body><div class="w">',
         f'<h1>{e(TITOLO[0])}</h1><div class="ar">{e(TITOLO[1])}</div><div class="zh">{e(TITOLO[2])}</div><p class="t">1INF · {DATA} · versione {VER}</p>']
    for num, tit, passi in CAPITOLI:
        h.append(f'<h2>{num} {e(tit[0])}</h2><div class="ar">{e(tit[1])}</div><div class="zh">{e(tit[2])}</div><ol>')
        for t, b in passi:
            h.append(f'<li><div class="it">{e(t[0])}</div><div class="ar">{e(t[1])}</div><div class="zh">{e(t[2])}</div>')
            if b == "FRASE": h += [box(f) for f in FRASE]
            elif b: h.append(box(b))
            h.append('</li>')
        h.append('</ol>')
    h.append('</div></body></html>')
    return "".join(h)


if __name__ == "__main__":
    open(os.path.join(QUI, "il-nostro-personaggio.md"), "w", encoding="utf-8").write(md())
    hp = os.path.join(QUI, "il-nostro-personaggio.html")
    open(hp, "w", encoding="utf-8").write(pag())
    pdf = os.path.join(QUI, PDF)
    subprocess.run(["/opt/pw-browsers/chromium-1194/chrome-linux/chrome", "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", "file://" + hp], check=True, capture_output=True)
    # copia per i ragazzi, accanto al percorso della lezione
    dst = os.path.join(ROOT, "docs", "compito", "1inf-20261014-talpa", "guida")
    os.makedirs(dst, exist_ok=True)
    shutil.copy(hp, os.path.join(dst, "index.html")); shutil.copy(pdf, os.path.join(dst, PDF))
    print(pdf)
