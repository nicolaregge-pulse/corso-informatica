// Vista del cruscotto 4TI · IPv4 03/11 (docente e ragazzi). Dati: cruscotto.json (anche cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function pill(ok,txt){return '<td class="'+(ok?'si':'no')+'">'+(ok?'\u2714 ':'\u2718 ')+e(txt||'')+'</td>'}
function cl(r){var c=r.classroom||{},k=Object.keys(c);if(!k.length)return '<td class="nu">dato non ancora letto</td>';var t=k.filter(function(x){return /TURNED_IN|RETURNED/.test(c[x]||'')}).length;return '<td class="'+(t?'si':'no')+'"><b>'+t+'/'+k.length+'</b> ore</td>'}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> \u00b7 '+e(D.fonte)+'</p>';
  if(D.fonti_ora){h+='<p class="mu"><b>Ultimo dato letto:</b> '+D.fonti_ora.map(function(f){return e(f.fonte)+' '+(f.vecchio?'<span style="color:#c62828;font-weight:800">'+e(f.ora)+'</span>':'<b>'+e(f.ora)+'</b>')}).join(' \u00b7 ')+'</p>'}
  h+='<p class="mu"><b>Come si legge:</b> \u2714 verde = fatto; \u2718 rosso = manca. I pi\u00f9 avanti stanno in alto.</p>';
  h+='<p class="mu"><b>Il voto (KPI proposti, in attesa del sì del Professore):</b> si parte da 40; quattro schede IPv4 completate fino a +15; scheda IPv4 con i numeri del proprio PC fino a +10; quiz di 12 domande su Moduli fino a +10; commit con messaggio chiaro e sezione rete su GitHub fino a +5. Massimo 80.</p>';
  if(!R.length){return h+'<p class="ante">Presenze non ancora segnate: appena il Professore le segna, qui compare una riga per ogni presente.</p>'}
  h+='<div class="tw"><table><thead><tr><th class="fix">Allievo</th><th>Schede s1-s4</th><th>Esercizi</th><th>Scheda IPv4</th><th>Quiz (12)</th><th>Commit GitHub</th><th>Classroom</th><th>Fermo da</th><th>'+(docente?'Veyon / note':'Veyon')+'</th><th>Voto</th></tr></thead><tbody>';
  R.forEach(function(r){var v=r.veyon||{},q=r.quiz;
   h+='<tr><td class="fix"><b>'+e(r.nome)+'</b></td>'+(r.schede==null?'<td class="nu">dato non ancora letto</td>':'<td class="'+(r.schede>=4?'si':r.schede>0?'nu':'no')+'"><b>'+r.schede+'/4</b></td>');
   h+=pill(r.esercizi,r.esercizi?'fatti':'da fare')+pill(r.scheda,r.scheda?'consegnata':'da fare');
   h+=q?'<td class="si">✔ <b>'+q.p+'/'+q.m+'</b></td>':'<td class="no">✘ da fare</td>';
   h+=pill(r.github,r.github?'consegnato':'da fare')+cl(r)+'<td>'+(r.fermo_da?e(r.fermo_da):'·')+'</td>';
   var vv=(!D.veyon_ok)?'<span style="color:#c62828;font-weight:800">Veyon: nessun dato oggi</span>':v.fuori?'<span style="color:#c62828;font-weight:800">fuori compito: '+v.fuori+'</span>':'<span class="mini">ok</span>';
   if(docente){(r.note||[]).forEach(function(z){vv+='<br><span class="mini">'+e(z)+'</span>'})}
   h+='<td style="white-space:normal;min-width:150px;text-align:left">'+vv+'</td><td class="voto"><b>'+r.voto+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>'});
  return h+'</tbody></table></div>'}
