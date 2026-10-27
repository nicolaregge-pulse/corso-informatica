// Generato da classe-1/ripasso-27-10/_build/ripasso.js (27/10/2026)
window.BANCA = {
 "id": "1inf-ripasso-2710-v1",
 "classe": "1INF",
 "titolo": "Ripasso da zero · مراجعة من البداية · 从头复习",
 "sotto": "1INF · 27/10/2026 · bit, byte, Mbps, ping, jitter, FPS, Hz · poi il quiz di ripasso su Moduli",
 "stato": "stato/1inf-ripasso-2710.json",
 "risultati": "risultati.html?b=1inf-ripasso-2710",
 "minuti": 10,
 "anteprima": "868848605",
 "aree": {
  "nozioni": {
   "nome": "Bit, byte e unità di misura",
   "peso": 50
  },
  "conti": {
   "nome": "I conti con i tuoi numeri",
   "peso": 30
  },
  "spiega": {
   "nome": "Saperlo spiegare (parole tue)",
   "peso": 20
  },
  "parere": {
   "nome": "Il tuo parere (non conta per il voto)",
   "peso": 0
  }
 },
 "schede": [
  {
   "titolo": "1. Il bit: 0 oppure 1 · ١. البِت: صفر أو واحد · 1. 比特：0 或 1",
   "testo": "Il computer capisce solo <b>due cose</b>: corrente <b>sì</b> o corrente <b>no</b>, come una lampadina accesa o spenta. Le scriviamo <b>1</b> e <b>0</b>.<br>Un solo 0 o 1 si chiama <b>bit</b>. È il pezzo più piccolo di informazione. Lo avete già visto con il <b>binario</b>: 1010 sono 4 bit.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">الحاسوب يفهم شيئين فقط: 1 أو 0، مثل مصباح مضاء أو مطفأ. الرقم الواحد اسمه «بِت».</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">电脑只懂两种状态：1 或 0，就像灯开或关。一个 0 或 1 叫做“比特”（bit）。</span>"
  },
  {
   "titolo": "2. Il byte: 8 bit insieme · ٢. البايت: ٨ بِت معًا · 2. 字节：8 个比特",
   "testo": "Un bit da solo dice poco. <b>8 bit insieme</b> fanno un <b>byte</b>. Con un byte il computer scrive <b>una lettera</b>: la A è 01000001.<br>Quindi: <b>1 byte = 8 bit = una lettera</b>.<br>Il bit si scrive con la <b>b piccola</b>, il byte con la <b>B grande</b>. Ricordatelo: serve dopo, per la velocità.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">٨ بِت = ١ بايت = حرف واحد. البِت يُكتب b صغيرة، والبايت B كبيرة.</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">8 个比特 = 1 个字节 = 一个字母。比特写小写 b，字节写大写 B。</span>"
  },
  {
   "titolo": "3. Le unità: KB, MB, GB, TB · ٣. الوحدات: KB، MB، GB، TB · 3. 单位：KB、MB、GB、TB",
   "testo": "I file sono fatti di tantissimi byte. Per non scrivere numeri lunghi usiamo i <b>multipli</b>, ogni gradino è <b>circa 1000 volte</b> più grande:<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Nome</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Si scrive</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Quanto è</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">kilobyte</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">KB</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">1000 byte</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">megabyte</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">MB</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">1000 KB</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">gigabyte</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">GB</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">1000 MB</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">terabyte</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">TB</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">1000 GB</td></tr></table>Come i metri: 1000 metri = 1 chilometro. (Il computer, per essere precisi, usa 1024 invece di 1000: per i nostri conti va bene 1000.)<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">كل درجة أكبر بنحو ١٠٠٠ مرة: ١٠٠٠ بايت = KB، ١٠٠٠ KB = MB، ١٠٠٠ MB = GB.</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">每一级大约大 1000 倍：1000 字节 = 1 KB，1000 KB = 1 MB，1000 MB = 1 GB。</span>"
  },
  {
   "titolo": "4. Attenzione: b piccola e B grande · ٧. انتبه: b صغيرة و B كبيرة · 7. 注意：小写 b 和大写 B",
   "testo": "La rete si misura in <b>Mb</b> (megabit, b piccola). I file si misurano in <b>MB</b> (megabyte, B grande).<br>Siccome 1 byte = 8 bit, per passare dalla velocità della rete ai MB al secondo <b>divido per 8</b>:<br>100 Mbps : 8 = <b>12,5 MB al secondo</b>.<br>Per questo, con una linea da 100 «mega», il download non va a 100 MB al secondo ma a circa 12.<span lang=\"ar\" dir=\"rtl\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:4px\">الشبكة بالميغابِت (b صغيرة) والملفات بالميغابايت (B كبيرة). نقسم على ٨: ١٠٠ Mbps ÷ ٨ = ١٢٫٥ MB في الثانية.</span><span lang=\"zh\" style=\"display:block;font-weight:400;color:var(--mu);font-size:.95em;margin-top:2px\">网速用兆比特（小写 b），文件用兆字节（大写 B）。除以 8：100 Mbps ÷ 8 = 每秒 12.5 MB。</span>"
  },
  {
   "titolo": "5. Il ping · البينغ · 延迟(ping)",
   "testo": "Il <b>ping</b> è il tempo che un messaggio impiega ad andare dal tuo PC al server del gioco e tornare indietro. Si misura in <b>millisecondi (ms)</b>: 1000 ms = 1 secondo.<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Ping</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Come si gioca</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">sotto 30 ms</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">ottimo</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">30-60 ms</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">buono</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">60-100 ms</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">si sente un po'</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">oltre 150 ms</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">lag: i colpi arrivano in ritardo</td></tr></table>Il ping dipende soprattutto dalla <b>distanza</b> dal server, non dai Mbps. <a href=\"../1inf-gamer/\" target=\"_blank\" rel=\"noopener\"><b>Apri il Laboratorio del gamer</b></a>: prova il gioco dei bersagli con ping 20 e con ping 200."
  },
  {
   "titolo": "6. Il jitter · التذبذب · 抖动",
   "testo": "Il <b>jitter</b> è quanto il ping <b>cambia</b> da un momento all'altro. Ping sempre 40 ms: jitter 0, il gioco è regolare. Ping che salta da 20 a 120 ms: jitter alto, il personaggio «salta» e a volte teletrasporta. Nel laboratorio prova jitter 0 e jitter 150 con lo stesso ping."
  },
  {
   "titolo": "7. Gli FPS · الإطارات في الثانية · 帧率(FPS)",
   "testo": "Un video o un gioco è fatto di tante <b>immagini ferme</b> mostrate una dopo l'altra. <b>FPS</b> = frame per second, immagini al secondo.<table style=\"border-collapse:collapse;width:100%;font-size:15px;margin:8px 0\"><tr><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">FPS</th><th style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">Come appare</th></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">15</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">a scatti</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">30</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">accettabile, film e console vecchie</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">60</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">fluido</td></tr><tr><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">144 e più</td><td style=\"border:1px solid var(--ln,#ccc);padding:5px 7px;text-align:left\">molto fluido, giochi veloci</td></tr></table>Gli FPS li produce la <b>scheda video</b>. Nel laboratorio, parte 2: guarda il quadrato a 5, 15, 30, 60 FPS."
  },
  {
   "titolo": "8. Gli Hz del monitor · الهرتز · 刷新率(Hz)",
   "testo": "Gli <b>Hz</b> (hertz) dicono quante volte al secondo il <b>monitor</b> ridisegna l'immagine. Un monitor da 60 Hz mostra al massimo 60 immagini al secondo: se la scheda video ne fa 200, ne vedi comunque 60.<br>Regola: <b>FPS della scheda video e Hz del monitor devono andare d'accordo</b>. Monitor da gaming: 144 o 240 Hz. Il laboratorio ti dice gli Hz dello schermo che stai usando.<div style=\"margin-top:18px;padding:14px;border:2px solid #1a7f37;border-radius:12px\"><p><b>FINE DEL RIPASSO · نهاية المراجعة · 复习结束</b></p><p><a href=\"https://docs.google.com/forms/d/e/1FAIpQLSfGk_SZIFZ5pJ6bxXXmSQkSHMlKuKH54Jlpebvdn2WtvmAD8g/viewform\" target=\"_blank\" rel=\"noopener\" style=\"display:inline-block;background:#1a7f37;color:#fff;padding:12px 18px;border-radius:10px;font-weight:700;text-decoration:none;font-size:18px\">QUIZ di ripasso · اختبار المراجعة · 复习测验</a></p><p>Poi la teoria nuova · ثم الدرس الجديد · 然后新课: <a href=\"./?b=1inf-video-cavi\">la scheda video e i cavi video</a></p></div>"
  }
 ],
 "schede_temi": {},
 "allenamento": [],
 "crocette": [],
 "aperte": [],
 "recupero": []
};
