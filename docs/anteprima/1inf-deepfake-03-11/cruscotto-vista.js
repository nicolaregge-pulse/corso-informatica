// Vista del cruscotto 1INF · 03/11 Deepfake (docente e ragazzi). Dati: cruscotto.json (anche cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function pill(ok,txt){return '<td class="'+(ok?'si':'no')+'">'+(ok?'✔ ':'✘ ')+e(txt||'')+'</td>'}
function num(n,t,s,sg){if(n==null)return '<td class="nu" style="white-space:normal;font-size:.8em">'+(sg===false?'nessun segnale: lo conta il Professore':'-')+'</td>';n=n||0;return '<td class="'+(n>=s?'si':n>0?'nu':'no')+'"><b>'+n+'/'+t+'</b></td>'}
function qz(q,s){return q?'<td class="'+(q.p>=s?'si':'nu')+'">✔ <b>'+q.p+'/'+q.m+'</b>'+(q.ora?' <span class="mini">'+e(q.ora)+'</span>':'')+'</td>':'<td class="no">✘ da fare</td>'}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> · '+e(D.fonte)+'</p>';
  (D.avvisi||[]).forEach(function(a){h+='<p style="color:#c62828;font-weight:800">'+e(a)+'</p>'});
  h+='<p class="mu"><b>Come si legge:</b> ✔ verde = fatto; ✘ rosso = manca. I più avanti stanno in alto.</p>';
  h+='<p class="mu"><b>Il voto (KPI proposti, in attesa del sì del Professore):</b> si parte da 40; ripasso Unicode 3 su 3 +5; schede lette +5; vero o falso 5-6 su 6 +10 (3-4 su 6 +5); quiz su Moduli 18 o più su 26 +15 (13-17 su 26 +8); quaderno ricopiato +5. Massimo 80.</p>';
  if(!R.length){return h+'<p class="ante">Nessun iscritto da mostrare.</p>'}
  h+='<div class="tw"><table><thead><tr><th class="fix">Allievo</th><th>Ripasso Unicode (3)</th><th>Schede lette (4)</th><th>Vero o falso (6)</th><th>Quiz Moduli (26)</th><th>Quaderno</th><th>Fermo da</th><th>'+(docente?'Veyon / note':'Veyon')+'</th><th>Voto</th></tr></thead><tbody>';
  R.forEach(function(r){var v=r.veyon||{},q=r.quiz;
   h+='<tr><td class="fix"><b>'+e(r.nome)+'</b></td>';
   h+=num(r.ripasso,3,3,r.segnale);
   h+=num(r.schede,4,4,r.segnale);
   h+=num(r.vf,6,5,r.segnale);
   h+=qz(q,18);
   h+=(r.quaderno==null?'<td class="nu" style="font-size:.8em">-</td>':pill(r.quaderno,r.quaderno?'ricopiato':'da fare'));
   h+='<td>'+(r.fermo_da?e(r.fermo_da):'·')+'</td>';
   var vv=v.fuori?'<span style="color:#c62828;font-weight:800">fuori compito: '+v.fuori+'</span>':'<span class="mini">ok</span>';
   if(docente){(r.note||[]).forEach(function(z){vv+='<br><span class="mini">'+e(z)+'</span>'})}
   h+='<td style="white-space:normal;min-width:150px;text-align:left">'+vv+'</td><td class="voto"><b>'+r.voto+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>'});
  return h+'</tbody></table></div>'}
