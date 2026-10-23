// Le tappe dell'app «Le misure del mio PC» (1INF, 23/10/2026), in 3 lingue. Ogni tappa: minuti, parole da raggiungere,
// test da fare (ping, down, schermo, lab), passi e capitoli del Documento [titolo, che cosa scrivere, parole minime].
window.TAPPE = {
it: [
 {tit: 'Tappa 0 · Crea il tuo Documento', min: 5, parole: 0, test: null, passi: [
  'Apri Classroom, corso «1 INF 26/27 Laboratorio di Informatica», scheda «Lavori del corso».',
  'Clicca il compito «Dimensioni e unità di misura dell\'informatica», poi «Visualizza compito».',
  'A destra, nel riquadro «Il tuo lavoro», clicca «+ Aggiungi o crea», poi «Documenti» (icona blu con le righe).',
  'Si apre il tuo Documento: ha già il tuo nome. Non cambiare il titolo. Si salva da solo.',
  'Nel Documento: menu «Strumenti» → «Conteggio parole» → spunta «Mostra conteggio parole durante la digitazione» → «OK». Ora in basso a sinistra vedi le tue parole.',
  'Torna su questa pagina (la scheda in alto nel browser) e premi FATTO.'], cap: []},
 {tit: 'Tappa 1 · Il mio PC e il ping', min: 12, parole: 350, test: 'ping', passi: [
  'Premi il bottone «Misura il ping» qui sotto e aspetta il risultato.',
  'Fai lo screenshot del risultato: Windows + Shift + S, trascina un rettangolo, poi nel Documento Ctrl + V.',
  'Scrivi i capitoli 1, 2 e 3 nel Documento. Il titolo di ogni capitolo in grassetto (Ctrl + B).'], cap: [
  ['1. Il mio PC e il mio posto', 'Guarda il tuo PC: che numero ha? È collegato alla rete con il cavo o con il Wi-Fi? Dietro il monitor: il cavo video è blu (VGA) o piatto (HDMI)? Descrivi quello che vedi.', 100],
  ['2. Il mio test del ping', 'Che cosa hai fatto, quali numeri hai ottenuto per il server A e il server B, perché sono diversi. Il tuo ping è ottimo, buono o da lag? Incolla lo screenshot.', 150],
  ['3. Il jitter che ho misurato', 'Guarda le 10 misure: cambiano poco o tanto? Quanto è il tuo jitter? Che cosa vorrebbe dire per una videochiamata o per un gioco?', 100]]},
 {tit: 'Tappa 2 · Il download e il firewall', min: 12, parole: 800, test: 'down', passi: [
  'Premi «Scarica il file di prova» e aspetta che la barra arrivi in fondo.',
  'Screenshot del risultato e Ctrl + V nel Documento.',
  'Scrivi i capitoli 4, 5 e 6.'], cap: [
  ['4. Il mio test di download', 'Quanti MB, quanti secondi, quanti Mbps e quanti MB al secondo. Spiega perché si divide per 8. Con la tua velocità, quanto ci vuole per un film da 2 GB? Scrivi il conto intero.', 200],
  ['5. TCP o UDP?', 'Il download che hai fatto usa TCP: perché un file ha bisogno che arrivino tutti i pacchetti? Fai 2 esempi di cose che usano UDP (videochiamata, diretta, gioco) e spiega perché lì non si aspetta il pacchetto perso.', 150],
  ['6. Il firewall della scuola', 'A scuola molti siti sono bloccati dal firewall (il «muro» che controlla che cosa entra e che cosa esce dalla rete). Nel test del ping, il server B ha risposto? Secondo te perché una scuola blocca dei siti? Che cosa protegge?', 100]]},
 {tit: 'Tappa 3 · Lo schermo', min: 12, parole: 1200, test: 'schermo', passi: [
  'Premi «Misura lo schermo».',
  'Screenshot della tabella e Ctrl + V nel Documento.',
  'Scrivi i capitoli 7, 8, 9 e 10. Copia i conti dalla tabella ma spiegali con parole tue.'], cap: [
  ['7. Gli Hz del mio schermo', 'Quanti Hz ha il tuo schermo? Quanti millisecondi resta ogni immagine? Se la scheda video facesse 30 FPS, quante volte verrebbe ripetuta ogni immagine?', 100],
  ['8. Risoluzione e pixel', 'La risoluzione del tuo schermo, il conto dei pixel, quante volte ci sta nel 4K. Che cos\'è un pixel? Spiegalo come a un bambino.', 100],
  ['9. Quanto pesa una foto del mio schermo', 'Il conto pixel × 3 byte. Perché 3 byte? Quanto pesa 1 minuto di video senza compressione? Perché i video veri pesano molto meno (compressione)?', 100],
  ['10. Il cavo video del mio PC', 'Guarda di nuovo dietro il monitor: che cavo è? La banda del tuo schermo (dalla tabella): quale cavo basterebbe? Il tuo cavo va bene?', 100]]},
 {tit: 'Tappa 4 · Il gioco del lag e la consegna', min: 12, parole: 1500, test: 'lab', passi: [
  'Apri il Laboratorio del gamer con il bottone qui sotto, parte 1: gioca con ping 20 e poi con ping 200.',
  'Scrivi i capitoli 11, 12 e 13.',
  'Guarda in basso a sinistra nel Documento: hai almeno 1500 parole? Se no, aggiungi esempi ai capitoli più corti.',
  'Torna su Classroom, nel riquadro «Il tuo lavoro» clicca il bottone blu «Consegna» e poi di nuovo «Consegna». FATTO!'], cap: [
  ['11. Il gioco dei bersagli con il lag', 'Che cosa cambia tra ping 20 e ping 200? Quanti bersagli hai preso nei due casi? Collega quello che hai sentito con il ping che hai misurato nella tappa 1.', 100],
  ['12. Il PC del laboratorio va bene per giocare?', 'Usa tutti i tuoi numeri (ping, jitter, Mbps, Hz, risoluzione) e le tabelle della dispensa: per ogni numero di\' se va bene o no. Alla fine dai il tuo voto al PC.', 150],
  ['13. Che cosa ho imparato', 'Tre cose che hai imparato oggi, una cosa che non ti è ancora chiara, e come spiegheresti il ping a un amico.', 100]]}
],
ar: [
 {tit: 'المرحلة 0 · أنشئ مستندك', min: 5, parole: 0, test: null, passi: [
  'افتح Classroom، الصف «1 INF 26/27 Laboratorio di Informatica»، التبويب الثاني «Lavori del corso» (أعمال الصف).',
  'اضغط الواجب «Dimensioni e unità di misura dell\'informatica»، ثم «Visualizza compito» (عرض الواجب).',
  'على اليمين، في مربع «Il tuo lavoro» (عملك)، اضغط «+ Aggiungi o crea» (أضف أو أنشئ)، ثم «Documenti» (الأيقونة الزرقاء بالخطوط).',
  'يُفتح مستندك: فيه اسمك من قبل. لا تغيّر العنوان. يحفظ وحده.',
  'في المستند: القائمة «Strumenti» (أدوات) ← «Conteggio parole» (عدد الكلمات) ← ضع علامة على «Mostra conteggio parole durante la digitazione» ← «OK». الآن ترى كلماتك في الأسفل على اليسار.',
  'ارجع إلى هذه الصفحة (علامة التبويب في أعلى المتصفح) واضغط «تمّ».'], cap: []},
 {tit: 'المرحلة 1 · حاسوبي والبينغ', min: 12, parole: 350, test: 'ping', passi: [
  'اضغط الزر «قِس البينغ» في الأسفل وانتظر النتيجة.',
  'خذ لقطة شاشة للنتيجة: Windows + Shift + S، اسحب مستطيلًا، ثم في المستند Ctrl + V.',
  'اكتب الفصول 1 و2 و3 في المستند. عنوان كل فصل عريض (Ctrl + B).'], cap: [
  ['1. حاسوبي ومكاني', 'انظر إلى حاسوبك: ما رقمه؟ هل هو متّصل بالشبكة بالكابل أم بالواي فاي؟ خلف الشاشة: هل كابل الفيديو أزرق (VGA) أم مسطّح (HDMI)؟ صف ما تراه.', 100],
  ['2. اختبار البينغ الخاص بي', 'ماذا فعلت، ما الأرقام التي حصلت عليها للخادم A والخادم B، ولماذا هي مختلفة. هل البينغ عندك ممتاز أم جيد أم فيه تأخير؟ الصق لقطة الشاشة.', 150],
  ['3. التذبذب الذي قسته', 'انظر إلى القياسات العشرة: هل تتغيّر قليلًا أم كثيرًا؟ كم التذبذب عندك؟ ماذا يعني ذلك لمكالمة فيديو أو للعبة؟', 100]]},
 {tit: 'المرحلة 2 · التنزيل وجدار الحماية', min: 12, parole: 800, test: 'down', passi: [
  'اضغط «نزّل ملف التجربة» وانتظر حتى يصل الشريط إلى النهاية.',
  'لقطة شاشة للنتيجة و Ctrl + V في المستند.',
  'اكتب الفصول 4 و5 و6.'], cap: [
  ['4. اختبار التنزيل الخاص بي', 'كم MB، كم ثانية، كم Mbps وكم MB في الثانية. اشرح لماذا نقسم على 8. بسرعتك، كم يحتاج فيلم 2 GB؟ اكتب الحساب كاملًا.', 200],
  ['5. TCP أم UDP؟', 'التنزيل الذي قمت به يستعمل TCP: لماذا يحتاج الملف أن تصل كل الحزم؟ أعطِ مثالين لأشياء تستعمل UDP (مكالمة فيديو، بثّ مباشر، لعبة) واشرح لماذا لا ننتظر هناك الحزمة الضائعة.', 150],
  ['6. جدار الحماية في المدرسة', 'في المدرسة مواقع كثيرة محجوبة بجدار الحماية (firewall، «الجدار» الذي يراقب ما يدخل ويخرج من الشبكة). في اختبار البينغ، هل أجاب الخادم B؟ برأيك لماذا تحجب المدرسة بعض المواقع؟ ماذا تحمي؟', 100]]},
 {tit: 'المرحلة 3 · الشاشة', min: 12, parole: 1200, test: 'schermo', passi: [
  'اضغط «قِس الشاشة».',
  'لقطة شاشة للجدول و Ctrl + V في المستند.',
  'اكتب الفصول 7 و8 و9 و10. يمكنك نقل الحسابات من الجدول لكن اشرحها بكلماتك.'], cap: [
  ['7. الهرتز في شاشتي', 'كم Hz في شاشتك؟ كم ميلي ثانية تبقى كل صورة؟ لو كانت بطاقة الرسوميات تعطي 30 FPS، كم مرة تتكرّر كل صورة؟', 100],
  ['8. الدقّة والبكسلات', 'دقّة شاشتك، حساب البكسلات، كم مرة تدخل في 4K. ما هو البكسل؟ اشرحه كما تشرحه لطفل.', 100],
  ['9. كم تزن صورة لشاشتي', 'الحساب البكسلات × 3 بايت. لماذا 3 بايت؟ كم تزن دقيقة فيديو بدون ضغط؟ لماذا الفيديوهات الحقيقية أخفّ بكثير (الضغط)؟', 100],
  ['10. كابل الفيديو في حاسوبي', 'انظر مرة أخرى خلف الشاشة: أي كابل هو؟ نطاق شاشتك (من الجدول): أي كابل يكفي؟ هل كابلك مناسب؟', 100]]},
 {tit: 'المرحلة 4 · لعبة التأخير والتسليم', min: 12, parole: 1500, test: 'lab', passi: [
  'افتح مختبر اللاعب بالزر في الأسفل، الجزء 1: العب ببينغ 20 ثم ببينغ 200.',
  'اكتب الفصول 11 و12 و13.',
  'انظر في الأسفل على اليسار في المستند: هل عندك 1500 كلمة على الأقل؟ إذا لا، أضف أمثلة إلى الفصول الأقصر.',
  'ارجع إلى Classroom، في مربع «Il tuo lavoro» اضغط الزر الأزرق «Consegna» (تسليم) ثم مرة أخرى «Consegna». تمّ!'], cap: [
  ['11. لعبة الأهداف مع التأخير', 'ماذا يتغيّر بين بينغ 20 وبينغ 200؟ كم هدفًا أصبت في الحالتين؟ اربط ما شعرت به بالبينغ الذي قسته في المرحلة 1.', 100],
  ['12. هل حاسوب المختبر مناسب للعب؟', 'استعمل كل أرقامك (البينغ، التذبذب، Mbps، Hz، الدقّة) وجداول الملف: لكل رقم قل هل هو جيد أم لا. في النهاية أعطِ علامتك للحاسوب.', 150],
  ['13. ماذا تعلّمت', 'ثلاثة أشياء تعلّمتها اليوم، شيء واحد ما زال غير واضح، وكيف تشرح البينغ لصديق.', 100]]}
],
zh: [
 {tit: '第 0 步 · 创建你的文档', min: 5, parole: 0, test: null, passi: [
  '打开 Classroom，课程 «1 INF 26/27 Laboratorio di Informatica»，第二个标签 «Lavori del corso»（课堂作业）。',
  '点作业 «Dimensioni e unità di misura dell\'informatica»，再点 «Visualizza compito»（查看作业）。',
  '在右边 «Il tuo lavoro»（你的作业）框里，点 «+ Aggiungi o crea»（添加或创建），再点 «Documenti»（蓝色有横线的图标）。',
  '你的文档打开了：标题里已经有你的名字。不要改标题。它会自动保存。',
  '在文档里：菜单 «Strumenti»（工具）→ «Conteggio parole»（字数统计）→ 勾选 «Mostra conteggio parole durante la digitazione» → «OK»。现在左下角能看到你的词数。',
  '回到这个页面（浏览器上方的标签页），按“完成”。'], cap: []},
 {tit: '第 1 步 · 我的电脑和 ping', min: 12, parole: 350, test: 'ping', passi: [
  '按下面的按钮“测量 ping”，等结果出来。',
  '给结果截图：Windows + Shift + S，拖一个长方形，然后在文档里按 Ctrl + V。',
  '在文档里写第 1、2、3 章。每章标题加粗（Ctrl + B）。'], cap: [
  ['1. 我的电脑和我的座位', '看看你的电脑：编号是多少？它用网线还是 Wi-Fi 连网？显示器后面：视频线是蓝色的 (VGA) 还是扁的 (HDMI)？描述你看到的。', 100],
  ['2. 我的 ping 测试', '你做了什么，服务器 A 和服务器 B 的数字是多少，为什么不一样。你的 ping 是非常好、好，还是会卡？粘贴截图。', 150],
  ['3. 我测到的抖动', '看看 10 个测量值：变化小还是大？你的抖动是多少？这对视频通话或游戏意味着什么？', 100]]},
 {tit: '第 2 步 · 下载和防火墙', min: 12, parole: 800, test: 'down', passi: [
  '按“下载测试文件”，等进度条走到最后。',
  '给结果截图，在文档里按 Ctrl + V。',
  '写第 4、5、6 章。'], cap: [
  ['4. 我的下载测试', '多少 MB，多少秒，多少 Mbps，每秒多少 MB。解释为什么要除以 8。用你的速度，下载 2 GB 的电影要多久？写出完整计算。', 200],
  ['5. TCP 还是 UDP？', '你做的下载用的是 TCP：为什么文件需要所有数据包都到达？举 2 个用 UDP 的例子（视频通话、直播、游戏），解释为什么那里不等丢失的数据包。', 150],
  ['6. 学校的防火墙', '在学校，很多网站被防火墙（firewall，检查什么进出网络的“墙”）拦截。在 ping 测试里，服务器 B 有回应吗？你觉得学校为什么要拦截一些网站？它在保护什么？', 100]]},
 {tit: '第 3 步 · 屏幕', min: 12, parole: 1200, test: 'schermo', passi: [
  '按“测量屏幕”。',
  '给表格截图，在文档里按 Ctrl + V。',
  '写第 7、8、9、10 章。可以抄表格里的计算，但要用自己的话解释。'], cap: [
  ['7. 我屏幕的 Hz', '你的屏幕是多少 Hz？每张图片停留多少毫秒？如果显卡只有 30 FPS，每张图片会重复几次？', 100],
  ['8. 分辨率和像素', '你屏幕的分辨率，像素的计算，4K 是它的几倍。什么是像素？像对小朋友那样解释。', 100],
  ['9. 我屏幕的一张图片有多大', '计算 像素 × 3 字节。为什么是 3 字节？不压缩的 1 分钟视频有多大？为什么真正的视频小得多（压缩）？', 100],
  ['10. 我电脑的视频线', '再看看显示器后面：是什么线？你屏幕的带宽（看表格）：哪种线就够了？你的线合适吗？', 100]]},
 {tit: '第 4 步 · 延迟游戏和提交', min: 12, parole: 1500, test: 'lab', passi: [
  '用下面的按钮打开玩家实验室，第 1 部分：先用 ping 20 玩，再用 ping 200 玩。',
  '写第 11、12、13 章。',
  '看文档左下角：至少 1500 个词了吗？如果没有，在短的章节里加例子。',
  '回到 Classroom，在 «Il tuo lavoro» 框里点蓝色按钮 «Consegna»（提交），再点一次 «Consegna»。完成！'], cap: [
  ['11. 有延迟的打靶游戏', 'ping 20 和 ping 200 有什么不同？两次各打中几个靶？把你的感觉和第 1 步测到的 ping 联系起来。', 100],
  ['12. 实验室的电脑适合玩游戏吗？', '用你所有的数字（ping、抖动、Mbps、Hz、分辨率）和讲义里的表格：每个数字说说好不好。最后给这台电脑打分。', 150],
  ['13. 我学到了什么', '今天学到的三件事，一件还不清楚的事，以及你会怎么向朋友解释 ping。', 100]]}
]};
