// Vista del cruscotto 2INF · 04/11 Sicurezza (docente e ragazzi). Dati: cruscotto.json (anche cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function pill(ok,txt){return '<td class="'+(ok?'si':'no')+'">'+(ok?'✔ ':'✘ ')+e(txt||'')+'</td>'}
function num(n,t,s){n=n||0;return '<td class="'+(n>=s?'si':n>0?'nu':'no')+'"><b>'+n+'/'+t+'</b></td>'}
function qz(q,s){return q?'<td class="'+(q.p>=s?'si':'nu')+'">✔ <b>'+q.p+'/'+q.m+'</b></td>':'<td class="no">✘ da fare</td>'}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> · '+e(D.fonte)+'</p>';
  h+='<p class="mu"><b>Come si legge:</b> ✔ verde = fatto; ✘ rosso = manca. I più avanti stanno in alto.</p>';
  h+='<p class="mu"><b>Il voto (KPI proposti, in attesa del sì del Professore):</b> si parte da 40; il quiz su Moduli (20 casi, 5 punti l\'uno) dà 40 + 40 × punti / 100, soglia di superamento 70 su 100. Schede lette e ripasso si vedono ma non cambiano il voto. Massimo 80.</p>';
  if(!R.length){return h+'<p class="ante">Presenze non ancora segnate: appena il Professore le segna, qui compare una riga per ogni presente.</p>'}
  h+='<div class="tw"><table><thead><tr><th class="fix">Allievo</th><th>Schede lette (8)</th><th>Ripasso (6)</th><th>Quiz Moduli (100 punti)</th><th>Fermo da</th><th>'+(docente?'Veyon / note':'Veyon')+'</th><th>Voto</th></tr></thead><tbody>';
  R.forEach(function(r){var v=r.veyon||{},q=r.quiz;
   h+='<tr><td class="fix"><b>'+e(r.nome)+'</b></td>';
   h+=num(r.schede,8,8);
   h+=num(r.ripasso,6,6);
   h+=qz(q,70);
   h+='<td>'+(r.fermo_da?e(r.fermo_da):'·')+'</td>';
   var vv=v.fuori?'<span style="color:#c62828;font-weight:800">fuori compito: '+v.fuori+'</span>':'<span class="mini">ok</span>';
   if(docente){(r.note||[]).forEach(function(z){vv+='<br><span class="mini">'+e(z)+'</span>'})}
   h+='<td style="white-space:normal;min-width:150px;text-align:left">'+vv+'</td><td class="voto"><b>'+r.voto+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>'});
  return h+'</tbody></table></div>'}
