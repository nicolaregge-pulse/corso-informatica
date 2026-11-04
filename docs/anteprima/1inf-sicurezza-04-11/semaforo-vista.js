/* Semaforo della Sicurezza 1INF: disegna la tabella. disegnaSemaforo(D, docente) */
var KEYS=['q2','q3','q4','qb'];
var T={
 it:{h:'SEMAFORO DELLA SICUREZZA',sub:'1INF · mercoledì 04/11',fin:'Hanno finito tutto',man:'Mancano ancora',agg:'Ultimo aggiornamento',f5:'Premi F5 per vedere la situazione nuova.',
  old:function(m){return 'Attenzione: il dato ha '+m+' minuti e può essere vecchio. Premi F5. Se i colori non cambiano, il Professore sta aggiornando.'},
  l1:'✔ verde = quiz superato',l2:'✘ rosso = quiz da fare',l3:'⏳ = fatto, ma sotto il 70% (quiz B: 6 su 8)',
  col:{q2:'2ª ora',q3:'3ª ora',q4:'4ª ora',qb:'Quiz B'},cosa:'COSA DEVI FARE ADESSO',nome:'Nome',
  fatto:'Hai finito! Bravo.',
  no:function(k){return 'Fai il quiz '+(k=='qb'?'B':'della '+k.slice(1)+'ª ora')+'.'},
  ts:function(k){return 'Rifai il quiz '+(k=='qb'?'B':'della '+k.slice(1)+'ª ora')+': puoi farcela!'},
  att:function(k){return 'Aspetta il Professore: ti riapre il quiz della '+k.slice(1)+'ª ora.'},
  poi:function(k){return 'Poi: il Professore ti riapre il quiz della '+k.slice(1)+'ª ora.'},
  bt:'APRI IL QUIZ',btB:'APRI IL QUIZ B',errore:'Dati non ancora pronti. Premi F5.'},
 ar:{h:'إشارة المرور للسلامة',sub:'1INF · الأربعاء 04/11',fin:'أنهوا كل شيء',man:'ما زال ينقص',agg:'آخر تحديث',f5:'اضغط F5 لترى الوضع الجديد.',
  old:function(m){return 'تنبيه: البيانات عمرها '+m+' دقيقة وقد تكون قديمة. اضغط F5.'},
  l1:'✔ أخضر = نجحت في الاختبار',l2:'✘ أحمر = الاختبار مطلوب',l3:'⏳ = أجريته لكن أقل من 70% (الاختبار B: 6 من 8)',
  col:{q2:'الساعة 2',q3:'الساعة 3',q4:'الساعة 4',qb:'اختبار B'},cosa:'ماذا عليك أن تفعل الآن',nome:'الاسم',
  fatto:'أنهيت! أحسنت.',
  no:function(k){return 'أجرِ '+(k=='qb'?'اختبار B':'اختبار الساعة '+k.slice(1))+'.'},
  ts:function(k){return 'أعد '+(k=='qb'?'اختبار B':'اختبار الساعة '+k.slice(1))+': تستطيع!'},
  att:function(k){return 'انتظر الأستاذ: سيعيد فتح اختبار الساعة '+k.slice(1)+'.'},
  poi:function(k){return 'ثم: الأستاذ يعيد فتح اختبار الساعة '+k.slice(1)+'.'},
  bt:'افتح الاختبار',btB:'افتح الاختبار B',errore:'البيانات غير جاهزة. اضغط F5.'},
 zh:{h:'安全课红绿灯',sub:'1INF · 11月4日 星期三',fin:'全部完成',man:'还差',agg:'最后更新',f5:'按 F5 查看新情况。',
  old:function(m){return '注意：数据是 '+m+' 分钟前的，可能过时。按 F5。'},
  l1:'✔ 绿色 = 测验通过',l2:'✘ 红色 = 还要做',l3:'⏳ = 做了，但低于 70%（测验 B：8 题对 6 题）',
  col:{q2:'第 2 节',q3:'第 3 节',q4:'第 4 节',qb:'测验 B'},cosa:'你现在要做什么',nome:'名字',
  fatto:'你完成了！太棒了。',
  no:function(k){return '做'+(k=='qb'?'测验 B':'第 '+k.slice(1)+' 节的测验')+'。'},
  ts:function(k){return '重做'+(k=='qb'?'测验 B':'第 '+k.slice(1)+' 节的测验')+'：你可以的！'},
  att:function(k){return '等老师：他会重新打开第 '+k.slice(1)+' 节的测验。'},
  poi:function(k){return '然后：老师会重新打开第 '+k.slice(1)+' 节的测验。'},
  bt:'打开测验',btB:'打开测验 B',errore:'数据还没准备好。按 F5。'}
};
var LG='it';
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function azione(r,D){
 var t=T[LG],man=KEYS.filter(function(k){return r.c[k]!=='ok'});
 if(!man.length)return {fin:true,html:'<span class="fin">✔ '+t.fatto+'</span>'};
 var libero=function(k){return r.c[k]==='no'||(r.c[k]==='ts'&&(k==='q4'||k==='qb'||D.riaperti===true))};
 var bloc=man.filter(function(k){return !libero(k)}),lib=man.filter(libero),h='';
 if(lib.length){var k=lib[0];h=esc(r.c[k]==='no'?t.no(k):t.ts(k))+'<a class="go" target="_blank" rel="noopener" href="'+esc(D.link[k])+'">'+(k==='qb'?t.btB:t.bt)+'</a>';
  if(bloc.length)h+='<span class="poi">'+esc(t.poi(bloc[0]))+'</span>'}
 else h='<span class="att">⏳ '+esc(t.att(bloc[0]))+'</span>';
 return {fin:false,html:h,n:man.length}}
function disegnaSemaforo(D,doc){
 var t=T[LG],R=D.righe.map(function(r){var a=azione(r,D);return {r:r,a:a}});
 R.sort(function(x,y){return (y.a.fin-x.a.fin)||((x.a.n||0)-(y.a.n||0))||x.r.nome.localeCompare(y.r.nome)});
 var nf=R.filter(function(x){return x.a.fin}).length,m=R.length-nf;
 var gen=new Date(D.generato),min=isNaN(gen)?999:Math.round((Date.now()-gen.getTime())/60000);
 var h='<div class="num3"><div class="v"><b>'+nf+'</b><span>'+esc(t.fin)+'</span></div><div class="r"><b>'+m+'</b><span>'+esc(t.man)+'</span></div><div><b>'+esc(D.ora)+'</b><span>'+esc(t.agg)+'</span></div></div>';
 if(min>15)h+='<p class="avviso">⚠ '+esc(t.old(min))+'</p>';
 h+='<p class="f5">'+esc(t.f5)+'</p>';
 h+='<div class="leg"><p><b style="color:var(--ok)">'+esc(t.l1)+'</b></p><p><b style="color:var(--ko)">'+esc(t.l2)+'</b></p><p><b style="color:var(--wa)">'+esc(t.l3)+'</b></p></div>';
 h+='<div class="testa"><span>'+esc(t.nome)+'</span>'+KEYS.map(function(k){return '<span>'+esc(t.col[k])+'</span>'}).join('')+'<span>'+esc(t.cosa)+'</span>'+(doc?'<span>Veyon / note</span>':'')+'</div>';
 R.forEach(function(x){var r=x.r;
  h+='<div class="riga'+(x.a.fin?' fin':'')+'"><div class="nome">'+esc(r.nome)+'</div>'+KEYS.map(function(k){var s=r.c[k];
   return '<div class="s '+s+'"><small>'+esc(t.col[k])+'</small>'+(s==='ok'?'✔':s==='ts'?'⏳':'✘')+(doc&&r.p&&r.p[k]?'<span class="sm">'+esc(r.p[k])+'</span>':'')+'</div>'}).join('')
   +'<div class="az">'+x.a.html+'</div>'+(doc?'<div class="nt">'+esc((r.note||[]).join(' · '))+'</div>':'')+'</div>'});
 if(doc){var d=R.filter(function(x){return !x.a.fin});
  h+='<div class="da"><h2>Da fare ('+d.length+')</h2><ol>'+d.map(function(x){var r=x.r;var mm=KEYS.filter(function(k){return r.c[k]!=='ok'}).map(function(k){return T.it.col[k]+(r.c[k]==='ts'?' (sotto soglia '+(r.p[k]||'')+')':'')});return '<li><b>'+esc(r.nome)+'</b>: '+esc(mm.join(', '))+'</li>'}).join('')+'</ol></div>'}
 return h}
