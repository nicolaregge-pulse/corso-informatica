#!/usr/bin/env python3
"""Dispensa unica 1INF in ARABO: _build/ar/NN.md (un file per capitolo) -> dispensa-1inf-ar.md -> dispensa-1inf-ar-vX.Y.html.
Uso: python3 classe-1/dispensa/_build/genera_ar.py ; poi node classe-1/dispensa/_build/pdf_ar.js
Riusa genera.py (link di Classroom, immagini incorporate, riquadri colorati). Pagina RTL con il font Amiri;
il testo in caratteri latini (codice, nomi di file, menu, link, numeri) viene isolato da sinistra a destra."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genera as G

B, OUT = G.B, G.OUT

# Riepilogo: per ogni compito di genera.COMPITI, «che cosa si consegna» in arabo (stesso ordine)
CONSEGNA_AR = [
 'مستند Google على Classroom', 'مستند فيه البحث؛ وحساب GitHub', 'العمل على قطع الحاسوب، على Classroom',
 'ما يطلبه الواجب', 'قراءة ورقة الإصدارات', 'اختبار مكتمل', 'العمل على قطع الحاسوب، على Classroom', 'اختبار مكتمل',
 'مستند فيه المعايير الخمسة والصور', 'قائمة القطع المتوافقة مع المجموع', 'مستند فيه 8 قطع والأسعار والمجموع',
 'مستند فيه لقطة شاشة والنص المنسوخ وتفكير شخصي', 'كما يقول الواجب', 'قراءة الملزمة', '16 تمرينًا محلولًا',
 'تمارين التحويل', 'قسمة متتالية على 2', 'نتيجة صفحة التمارين', 'نتيجة صفحة التمارين', 'نتيجة صفحة التمارين',
 'كما يقول الواجب', 'مستند فيه الطلب وصورة الرسم', 'مستند فيه الطلب', 'مستند فيه الخطأ', 'مستند فيه المراجعة',
 'واجب واحد مع الاختبار', 'طلب الدمج: السطر، القيمة الجديدة، السبب', 'الصورة المقصوصة والجملة عن الشخصية',
 'المراجعة والتقييم على الصفحة', 'بضعة أسطر عن الدرس', 'التقييم على الصفحة', 'الحاسوب بعد إعادة تركيبه',
 'التحدي مكتمل', 'المراجعة والاختبار على الصفحة', 'المراجعة على الصفحة', 'اختبار Moduli مُرسَل',
 'مسار «كم واحدًا يتسع؟» وألعاب البايت', 'اختبار Moduli مُرسَل', 'المراجعة على الصفحة واختبار Moduli',
 'مستند «الشبكة واللاعب»، 13 فصلًا، 1500 كلمة على الأقل', 'اختبار Moduli مُرسَل', 'الاختباران',
 'مستند فيه الكود ولقطة شاشة وجملة', 'المراجعة على الصفحة واختبار Moduli', 'الاختبارات الناقصة',
 'المراجعة واختباران على Moduli', 'في كل ساعة unit1.pas ولقطة الشاشة',
]
assert len(CONSEGNA_AR) == len(G.COMPITI), (len(CONSEGNA_AR), len(G.COMPITI))


def tabella():
    r = ['| رقم | التاريخ | الواجب (العنوان كما في Classroom) | ماذا تسلّم | الفصل |', '|---|---|---|---|---|']
    for i, ((d, t, c, cap), car) in enumerate(zip(G.COMPITI, CONSEGNA_AR), 1):
        r.append(f'| {i} | {d} | <span dir="ltr" lang="it">{t}</span> | {car} | {cap} |')
    return '\n'.join(r)


def sorgente_a_md():
    import glob  # il sorgente arabo è diviso in un file per capitolo: _build/ar/NN.md
    s = '\n'.join(open(f, encoding='utf8').read().rstrip() + '\n' for f in sorted(glob.glob(os.path.join(B, 'ar', '*.md'))))
    s = re.sub(r'\{\{CR:(\d+)\}\}', lambda m: G.CR + G.LINK[m.group(1)] + '/details', s)
    s = s.replace('{{TABELLA}}', f'يذكر الجدول الواجبات الـ {len(G.COMPITI)} التي أُعطيت على Classroom لصف 1INF حتى 30/10/2026، بترتيب التاريخ. '
                  'يقول عمود «الفصل» أين تجد الشرح والتعليمات. عناوين الواجبات بالإيطالية، كما تراها على Classroom.\n\n' + tabella())
    return s


CSS_AR = """
body{font-family:"Amiri","DejaVu Sans",serif;font-size:12.6pt;line-height:1.7;direction:rtl;text-align:right}
ol{padding-left:0;padding-right:24px}
th,td{text-align:right}
.box{border-left:0;border-right:5px solid}
code,pre,kbd{direction:ltr;unicode-bidi:isolate;text-align:left}
pre{font-size:9.5pt;line-height:1.4}
a{direction:ltr;unicode-bidi:isolate}
[dir=ltr]{unicode-bidi:isolate}
p.it{direction:ltr;text-align:left;font-family:"DejaVu Sans",sans-serif;font-size:9.6pt;color:#5c6672;font-style:italic;margin:-2px 0 8px}
h1,h2,h3{font-family:"Amiri","DejaVu Sans",serif}
h2{font-size:16pt}
h3{font-size:13pt}
figcaption{font-size:10.5pt}
"""

LAT = re.compile(r"[A-Za-z0-9'«À-ɏ](?:[\x20-\x7EÀ-ɏ«»→]*[A-Za-z0-9'»)À-ɏ])?")


def isola_latino(corpo):
    """Avvolge in <span dir="ltr"> i pezzi in caratteri latini del testo normale (non in code, pre, a, span, style)."""
    out, salta = [], 0
    for pezzo in re.split(r'(<[^>]+>)', corpo):
        if pezzo.startswith('<'):
            m = re.match(r'<(/?)(code|pre|a|span|style|title)\b', pezzo)
            if m:
                salta += -1 if m.group(1) else 1
            out.append(pezzo)
        elif salta > 0 or not re.search(r'[؀-ۿ]', pezzo):
            out.append(pezzo)
        else:
            out.append(LAT.sub(lambda m: f'<span dir="ltr">{m.group(0)}</span>', pezzo))
    return ''.join(out)


def main():
    md = sorgente_a_md()
    ver = re.search(r'\*\*الإصدار (\d+\.\d+)\*\*', md).group(1)
    open(os.path.join(OUT, 'dispensa-1inf-ar.md'), 'w', encoding='utf8').write(md)
    corpo = G.md_a_html(md)
    corpo = isola_latino(corpo)
    doc = (f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>Dispensa 1INF AR v{ver}</title><style>{G.CSS}{CSS_AR}</style></head><body>{corpo}</body></html>')
    out = os.path.join(OUT, f'dispensa-1inf-ar-v{ver}.html')
    open(out, 'w', encoding='utf8').write(doc)
    print(out, len(doc) // 1024, 'KB')


if __name__ == '__main__':
    main()
