// Vista comune del cruscotto 2INF · reti e phishing (docente e ragazzi). Dati: cruscotto.json (cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function pill(ok,txt,sub){return '<td class="'+(ok?'si':'no')+'">'+(ok?'✔ ':'✘ ')+(txt||'')+(sub?'<br><span class="mini">'+e(sub)+'</span>':'')+'</td>'}
function sch(n,t){return '<td class="'+(n>=t?'si':n>0?'nu':'no')+'">'+(n>=t?'✔ ':'')+'<b>'+n+'/'+t+'</b></td>'}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> · '+e(D.fonte)+'</p>';
  if(D.presenti_ok===false)h+='<p class="ante">Attenzione: l\'elenco dei presenti non è ancora arrivato dal registro: si vedono tutti gli allievi della classe.</p>';
  if(D.fonti_ora&&D.fonti_ora.length){h+='<p class="fonti-ora" style="display:flex;flex-wrap:wrap;gap:6px;margin:6px 0">';D.fonti_ora.forEach(function(f){var t=f.iso?Date.parse(f.iso):NaN,v=!f.iso||isNaN(t)||(Date.now()-t)>15*60000;h+='<span style="padding:3px 8px;border-radius:6px;font-size:.9em;border:1px solid '+(v?'#c62828':'#2e7d32')+';color:'+(v?'#c62828':'inherit')+';font-weight:'+(v?'700':'400')+'">'+e(f.fonte)+': dato aggiornato alle '+(f.ora?e(f.ora):'nessun dato')+(v?' (vecchio)':'')+'</span>'});h+='</p>'}
  h+='<p class="mu"><b>Come si legge:</b> ✔ verde = fatto; ✘ rosso = manca; il numero tra le schede è «schede lette su 6». I più avanti stanno in alto.</p>';
  h+='<p class="mu"><b>Il voto (KPI proposti, in attesa del sì del Professore):</b> si parte da 40; teoria sulla rete letta +5; scheda d\'identità del PC consegnata +10; analisi delle 8 mail: fino a +20 (2,5 per ogni mail giusta); extra budget consegnato +5. Massimo 80. Il quiz di chiusura sulla rete si vede ma per ora non conta.</p>';
  h+='<div class="tw"><table><thead><tr><th class="fix" rowspan="2">Allievo</th><th colspan="2">1 · Teoria</th><th colspan="2">2 · Pratica</th><th rowspan="2">Quiz di chiusura rete</th><th colspan="2">3 · Phishing</th><th rowspan="2">4 · Extra budget</th><th rowspan="2">Fermo da</th><th rowspan="2">'+(docente?'Veyon / note':'Veyon')+'</th><th rowspan="2">Voto</th></tr>';
  h+='<tr><th>Reti</th><th>Phishing</th><th>Scheda del PC</th><th>Dove</th><th>Mail giuste</th><th>Indizi giusti</th></tr></thead><tbody>';
  R.forEach(function(r){var s=r.scheda||{},p=r.phishing,q=r.quiz_reti,x=r.extra||{},v=r.veyon||{};
   h+='<tr><td class="fix"><b>'+e(r.nome)+'</b></td>'+sch(r.teoria.reti,r.teoria.tot)+sch(r.teoria.ph,r.teoria.tot);
   h+=pill(s.consegnata,s.consegnata?'consegnata':'manca',s.ora?'alle '+s.ora:'')+'<td class="nu">'+(s.classroom?'Classroom: '+e(s.classroom):'')+(s.pagina?(s.classroom?'<br>':'')+'pagina del corso':'')+(!s.classroom&&!s.pagina?'·':'')+'</td>';
   h+=q?'<td class="si">✔ <b>'+q.p+'/'+q.m+'</b>'+(q.ora?'<br><span class="mini">'+e(q.ora)+'</span>':'')+'</td>':'<td class="nu">·</td>';
   h+=p?'<td class="'+(p.p>=6?'si':p.p>=4?'nu':'no')+'"><b>'+p.p+'/'+p.su+'</b>'+(p.ora?'<br><span class="mini">'+e(p.ora)+'</span>':'')+'</td><td class="nu">'+p.indizi_ok+'/'+p.su+'</td>':'<td class="no">✘ da fare</td><td class="nu">·</td>';
   h+=pill(x.consegnato,x.consegnato?'consegnato':'—',x.classroom&&!x.consegnato?x.classroom:'');
   h+='<td>'+(r.fermo_da?e(r.fermo_da):'·')+'</td>';
   var vv=(v.fuori?'<span style="color:#c62828;font-weight:800">fuori compito: '+v.fuori+'</span>':'<span class="mini">ok</span>');
   if(docente){(v.fuori_dett||[]).forEach(function(z){vv+='<br><span class="mini" style="color:#c62828">'+e(z)+'</span>'});(r.note||[]).forEach(function(z){vv+='<br><span class="mini">'+e(z)+'</span>'});if(v.ultimo)vv+='<br><span class="mini">ultimo: '+e(v.ultimo)+'</span>'}
   h+='<td style="white-space:normal;min-width:150px;text-align:left">'+vv+'</td>';
   h+='<td class="voto"><b>'+r.voto+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>'});
  h+='</tbody></table></div>';return h}
