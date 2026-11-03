// Vista del cruscotto 2INF · ora 6 Sicurezza (docente e ragazzi). Dati: cruscotto.json (anche cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function pill(ok,txt){return '<td class="'+(ok?'si':'no')+'">'+(ok?'\u2714 ':'\u2718 ')+e(txt||'')+'</td>'}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> \u00b7 '+e(D.fonte)+'</p>';
  h+='<p class="mu"><b>Come si legge:</b> \u2714 verde = fatto; \u2718 rosso = manca. I pi\u00f9 avanti stanno in alto.</p>';
  h+='<p class="mu"><b>Il voto (KPI proposti, in attesa del s\u00ec del Professore):</b> si parte da 40; schede lette +10; analisi delle 8 mail fino a +15; quiz sul phishing fino a +10; la mia regola d\'oro +5. Massimo 80.</p>';
  if(!R.length){return h+'<p class="ante">Presenze non ancora segnate: appena il Professore le segna, qui compare una riga per ogni presente.</p>'}
  h+='<div class="tw"><table><thead><tr><th class="fix">Allievo</th><th>Schede lette</th><th>Mail giuste su 8</th><th>Quiz phishing</th><th>Regola d\'oro</th><th>Fermo da</th><th>'+(docente?'Veyon / note':'Veyon')+'</th><th>Voto</th></tr></thead><tbody>';
  R.forEach(function(r){var v=r.veyon||{},q=r.quiz;
   h+='<tr><td class="fix"><b>'+e(r.nome)+'</b></td><td class="'+((r.schede||0)>=4?'si':(r.schede||0)>0?'nu':'no')+'"><b>'+(r.schede||0)+'/4</b></td>';
   h+=r.mail?'<td class="'+(r.mail.p>=6?'si':'nu')+'"><b>'+r.mail.p+'/8</b></td>':'<td class="no">\u2718 da fare</td>';
   h+=q?'<td class="si">\u2714 <b>'+q.p+'/'+q.m+'</b></td>':'<td class="no">\u2718 da fare</td>';
   h+=pill(r.regola,r.regola?'consegnata':'manca')+'<td>'+(r.fermo_da?e(r.fermo_da):'\u00b7')+'</td>';
   var vv=v.fuori?'<span style="color:#c62828;font-weight:800">fuori compito: '+v.fuori+'</span>':'<span class="mini">ok</span>';
   if(docente){(r.note||[]).forEach(function(z){vv+='<br><span class="mini">'+e(z)+'</span>'})}
   h+='<td style="white-space:normal;min-width:150px;text-align:left">'+vv+'</td><td class="voto"><b>'+r.voto+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>'});
  return h+'</tbody></table></div>'}
