// Genera le slide per la lezione frontale (HTML + PDF) dalla banca docs/verifica/banche/1inf-byte-velocita.js
// Uso: NODE_PATH=$(npm root -g) node classe-1/byte-velocita/_build/gen_slide.js
const fs = require('fs'), path = require('path');
const R = path.resolve(__dirname, '../../..'), OUT = path.resolve(__dirname, '..');
const SC = []; for (const f of ['1inf-byte-velocita', '1inf-gamer']) { global.window = {}; delete require.cache[require.resolve(R + '/docs/verifica/banche/' + f + '.js')]; require(R + '/docs/verifica/banche/' + f + '.js'); window.BANCA.schede.forEach((s, i) => { if (f === '1inf-gamer' && i === 0) return; SC.push(s); }); }
const B = { schede: SC };
const NOME = '20261020_Classe-1-PerTutti_v1.3_Bit-Byte-Rete-Gamer_multilingua';
const css = `@page{size:A4 landscape;margin:0}*{box-sizing:border-box}body{margin:0;font-family:"DejaVu Sans",Arial,sans-serif;color:#1b2430;--mu:#5c6672;--ln:#b9c2cc}
.s{width:297mm;height:210mm;padding:14mm 18mm;page-break-after:always;display:flex;flex-direction:column;overflow:hidden;border-top:10mm solid #1f6feb}
h1{font-size:30pt;margin:0 0 6mm;line-height:1.15}h1 span{font-size:17pt!important}
.t{font-size:19pt;line-height:1.4}.t table{font-size:16pt!important}.t td,.t th{padding:4px 10px!important}
[lang=ar]{font-family:Amiri,serif;font-size:1.05em!important}[lang=zh]{font-family:"WenQuanYi Zen Hei",sans-serif}
.pie{margin-top:auto;font-size:11pt;color:#5c6672}.cop{justify-content:center;text-align:center}.cop h1{font-size:40pt}`;
let h = `<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Bit, byte e velocità della rete</title><style>${css}</style></head><body>`;
h += `<div class="s cop"><h1>Quanto pesa un file?<br>Quanto va veloce la rete?</h1><div class="t">Bit, byte, KB, MB, GB · Mbps · streaming · Wi-Fi e cavi<br>ping, lag, FPS, Hz · monitor · schede video · cavi VGA e HDMI<br><span lang="ar" dir="rtl">كم يزن الملف؟ كم سرعة الشبكة؟</span><br><span lang="zh">文件有多大？网速有多快？</span></div><div class="pie">Classe 1 · 20 e 21/10/2026 · v1.3</div></div>`;
B.schede.forEach((s, i) => { const tt = s.titolo.replace(/^\d+\.\s*/, (i + 1) + '. ').split(' · '); h += `<div class="s"><h1>${tt[0]}<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:#5c6672">${tt[1] || ''}</span><span lang="zh" style="display:block;font-weight:400;color:#5c6672">${tt[2] || ''}</span></h1><div class="t">${s.testo}</div><div class="pie">Bit, byte, rete e gamer · ${i + 1} / ${B.schede.length}</div></div>`; });
// v1.2 (20/10, Nicola): le foto della lavagna della lezione frontale
const LAV = [['20261020_lavagna-bit-byte-crc.jpg', 'Alla lavagna: bit, byte, Mbps e il controllo dei dati', 'على السبورة: البت والبايت والتحقق من البيانات', '黑板上：比特、字节和数据校验', 'Un byte = 8 bit. KB, MB, GB: mille volte di più a ogni passo. Mbps = megabit al secondo. Chi spedisce conta gli 1 di ogni byte e manda il numero: chi riceve rifà il conto. Se non torna, un bit si è rovinato. Il CRC è il controllo vero, più furbo.'],
 ['20261020_lavagna-segnale-0V-5V.jpg', 'Alla lavagna: il byte diventa corrente nel cavo', 'على السبورة: البايت يصبح تيارًا في الكابل', '黑板上：字节在电缆里变成电流', 'Il byte 01011101 viaggia nel cavo come tensione: 5 volt = 1, 0 volt = 0. Se un disturbo cambia la tensione, un bit si rovina: per questo serve il controllo dei dati.'],
 ['20261021_lavagna-3MB-byte.jpg', 'Alla lavagna: una foto è fatta di byte', 'على السبورة: الصورة مصنوعة من البايتات', '黑板上：一张照片由字节组成', 'Una foto del telefono pesa circa 3 MB = 3.000.000 byte. Ogni byte è una fila di 8 bit (0 e 1): una foto è una fila di 3 milioni di queste scatoline.'],
 ['20261021_lavagna-quante-foto.jpg', 'Alla lavagna: quante foto ci stanno nel telefono?', 'على السبورة: كم صورة تتسع في الهاتف؟', '黑板上：手机能放多少张照片？', 'Telefono con 64 GB liberi = 64.000 MB. Una foto = 3 MB. 64.000 : 3 = circa 21.000 foto. E 32 foto? 32 × 3 = 96 MB. Regola: prima tutto nella stessa unità, poi dividi.'],
 ['20261021_lavagna-velocita-rete.jpg', 'Alla lavagna: Mb/s e MB/s', 'على السبورة: Mb/s و MB/s', '黑板上：Mb/s 和 MB/s', 'In rete i bit viaggiano uno dopo l\'altro: la velocità si misura in Mb/s (megabit al secondo, b piccola). 8 Mb/s = 1 MB/s (megabyte al secondo, B grande). Quindi 100 Mb/s ≈ 12 MB/s: circa 4 foto al secondo.']];
LAV.forEach(l => { h += `<div class="s"><h1>${l[1]}<span lang="ar" dir="rtl" style="display:block;font-weight:400;color:#5c6672">${l[2]}</span><span lang="zh" style="display:block;font-weight:400;color:#5c6672">${l[3]}</span></h1><div style="display:flex;gap:8mm;min-height:0;flex:1"><img src="${l[0].replace('.jpg','_slide.jpg')}" style="height:118mm;border-radius:3mm;object-fit:contain"><div class="t" style="font-size:17pt">${l[4]}</div></div><div class="pie">La lavagna della lezione · ${l[0].slice(6,8)}/${l[0].slice(4,6)}/${l[0].slice(0,4)}</div></div>`; });
h += `<div class="s cop"><h1>Adesso tocca a te!</h1><div class="t">Apri il compito su Classroom: ripasso, poi il test.<br>Ti serve: quanti GB ha il tuo telefono.<br><span lang="ar" dir="rtl">الآن دورك! افتح الواجب في Classroom.</span><br><span lang="zh">现在轮到你了！打开 Classroom 上的作业。</span></div></div></body></html>`;
fs.writeFileSync(`${OUT}/${NOME}.html`, h);
(async () => { const { chromium } = require('playwright'); const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage(); await p.goto('file://' + `${OUT}/${NOME}.html`); await p.waitForTimeout(400);
  await p.evaluate(() => document.querySelectorAll('.s').forEach(s => { const t = s.querySelector('.t'); let f = 19; while (s.scrollHeight > s.clientHeight + 1 && f > 11) { f -= 0.5; t.style.fontSize = f + 'pt'; t.querySelectorAll('table').forEach(x => x.style.setProperty('font-size', (f - 3) + 'pt', 'important')); } }));
  fs.writeFileSync(`${OUT}/${NOME}.html`, await p.content());
  await p.pdf({ path: `${OUT}/${NOME}.pdf`, landscape: true, format: 'A4', printBackground: true }); await b.close(); console.log(`${OUT}/${NOME}.pdf`); })();
