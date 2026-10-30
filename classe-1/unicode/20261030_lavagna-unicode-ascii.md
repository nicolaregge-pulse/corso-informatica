# Unicode e codice ASCII: la lavagna del 30/10

**Versione 1.1** — 30/10/2026
*Fonte del libro di testo della 1INF per la lezione del 30/10/2026 (ora 8-9): foto e trascrizione delle tre lavagne. La pagina della lezione è docs/1inf-unicode/.*

---

## La lavagna del 30/10

![La lavagna del 30/10: Unicode, interi e stringhe, codice ASCII, solo 256 caratteri](immagini/20261030_lavagna-unicode-ascii.jpg)

1. Oggi: 1) **Unicode** · 2) **Interi e stringhe**.
2. Il computer conosce solo 0 e 1: 0101010101010.
3. **Codice ASCII:** ogni lettera ha un numero. **A** = 65 = 01000001; **B** = 66 = 01000010.
4. In rosso: **solo 256 caratteri**, da 00000000 a 11111111.

<div class="scheda"><p lang="it">Perché 256? Con 8 bit ci sono 256 combinazioni: da 00000000 a 11111111. Il primissimo ASCII usava 7 bit, cioè 128 caratteri; la versione a 8 bit ne ha 256. Per tutte le lingue del mondo 256 non bastano: per questo è nato <b>Unicode</b>.</p><p lang="ar" dir="rtl">لماذا 256؟ مع 8 بت توجد 256 تركيبة: من 00000000 إلى 11111111. أول ASCII كان يستعمل 7 بت، أي 128 رمزاً؛ ونسخة 8 بت فيها 256. لكل لغات العالم 256 لا تكفي: لهذا وُلد Unicode.</p><p lang="zh">为什么是 256？8 个比特有 256 种组合：从 00000000 到 11111111。最早的 ASCII 用 7 个比特，也就是 128 个字符；8 比特的版本有 256 个。世界上所有的语言，256 个远远不够：所以有了 Unicode。</p></div>

## La lavagna 2: Unicode e le cifre esadecimali

![La lavagna 2 del 30/10: Unicode, A U+0041, arabo U+0628, cinese U+4E2D, le cifre esadecimali](immagini/20261030_lavagna-unicode-esadecimale.jpg)

1. Italiano/inglese: **A** = U+0041.
2. Arabo: **ب** = U+0628.
3. Cinese: **中** = U+4E2D.
4. **Cifre esadecimali:** 0 1 2 3 4 5 6 7 8 9 A B C D E F, con A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.
5. In alto a destra: ABC e lettere di altri alfabeti.

<div class="scheda"><p lang="it">In Unicode ogni carattere ha un numero, scritto con U+ e 4 cifre esadecimali. Le cifre esadecimali sono 16: dopo il 9 vengono le lettere da A (10) a F (15).</p><p lang="ar" dir="rtl">في Unicode لكل رمز رقم، يُكتب بـ U+ و4 أرقام سداسية عشرية. الأرقام السداسية العشرية 16: بعد 9 تأتي الحروف من A (10) إلى F (15). الإنكليزية/الإيطالية: A = U+0041 · العربية: ب = U+0628 · الصينية: 中 = U+4E2D.</p><p lang="zh">在 Unicode 里每个字符都有一个数字，用 U+ 和 4 位十六进制数字来写。十六进制数字有 16 个：9 后面是字母 A（10）到 F（15）。意大利文/英文：A = U+0041 · 阿拉伯文：ب = U+0628 · 中文：中 = U+4E2D。</p></div>

## La lavagna 3: stringhe e interi

![La lavagna 3 del 30/10: stringhe e interi, '12' + '15' = '1215' e 12 + 15 = 27](immagini/20261030_lavagna-stringhe-interi.jpg)

Due colonne: a sinistra **STRINGHE**, a destra **INTERI**.

1. 1 → 1.
2. 123 → 123: cerchiato, **NUMERI**.
3. '123' ← '123': cerchiato, **CARATTERI**.
4. 'Ciao' ← 'Ciao': **CARATTERI**.
5. '12' + '15' = '1215'.
6. 12 + 15 = 27.

<div class="scheda"><p lang="it">Con gli apici è una <b>stringa</b> (caratteri): il + attacca i testi uno dopo l'altro, quindi '12' + '15' = '1215'. Senza apici è un <b>intero</b> (numero): il + fa la somma, quindi 12 + 15 = 27.</p><p lang="ar" dir="rtl">مع علامات الاقتباس هو نص (String، رموز): علامة + تلصق النصوص واحداً بعد الآخر، إذن '12' + '15' = '1215'. بدون علامات الاقتباس هو عدد صحيح (Integer): علامة + تجمع، إذن 12 + 15 = 27.</p><p lang="zh">有引号的是字符串（String，字符）：+ 把文字一个接一个连起来，所以 '12' + '15' = '1215'。没有引号的是整数（Integer，数字）：+ 做加法，所以 12 + 15 = 27。</p></div>

## Changelog
1. **v1.0 (30/10/2026)**: prima versione, con la foto della lavagna e la trascrizione.
2. **v1.1 (30/10/2026)**: le lavagne 2 (Unicode e cifre esadecimali) e 3 (stringhe e interi), con foto e trascrizione.
