// Vista del cruscotto 2INF 03/11 (docente e ragazzi). Dati: cruscotto.json (cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> · '+e(D.fonte)+'</p>';
  if(docente){h+='<p style="margin:6px 0">'+(D.fonti_ora||[]).map(function(f){return '<span class="mini" style="'+(f.vecchio?'color:#c62828;font-weight:800':'')+'">'+e(f.fonte)+': '+e(f.ora)+'</span>'}).join(' · ')+'</p>';
    if(!D.veyon_ok)h+='<p style="color:#c62828;font-weight:800">Veyon: nessun dato di oggi. Manda gli screenshot di Veyon e li leggo.</p>'}
  h+='<p class="mu"><b>Come si legge:</b> ✔ verde = fatto; ✘ rosso = manca; grigio = non ancora aperto. I più avanti stanno in alto.</p>';
  h+='<p class="mu"><b>Il voto (KPI della pagina):</b> si parte da 40; 2FA attiva +10; mail giuste 6 o più su 8 +10 (4-5 +5); quiz phishing 9 o più su 12 +15 (6-8 +8); scheda del PC +5. Massimo 80.</p>';
  if(!R.length)return h+'<p class="ante">Nessun dato ancora.</p>';
  var o2=D.ora2_aperta;
  h+='<div class="tw"><table><thead><tr><th class="fix">Allievo</th><th>2FA</th><th>Scheda PC</th><th>Quiz rete (ieri)</th><th>Quiz DHCP e DNS</th><th>Mail giuste su 8</th><th>Quiz phishing</th><th>Fermo da</th><th>'+(docente?'Veyon / note':'Veyon')+'</th><th>Voto</th></tr></thead><tbody>';
  R.forEach(function(r){var v=r.veyon||{},f=r.fa2||{},q=r.quiz_reti,m=r.mail,p=r.quiz_ph;
   h+='<tr><td class="fix"><b>'+e(r.nome)+'</b></td>';
   h+='<td class="'+(f.ok?'si':'no')+'">'+(f.ok?'✔ ':'✘ ')+e(f.txt)+(f.ora?' <span class="mini">'+e(f.ora)+'</span>':'')+'</td>';
   h+='<td class="'+(r.scheda&&r.scheda.ok?'si':'no')+'">'+(r.scheda&&r.scheda.ok?'✔ consegnata':'✘ manca')+'</td>';
   h+=q?'<td class="si">✔ <b>'+q.p+'/'+q.m+'</b></td>':'<td class="no">✘ manca</td>';
   var d=r.quiz_dhcp;h+=d?'<td class="si">✔ <b>'+d.p+'/'+d.m+'</b> <span class="mini">'+e((d.giorno&&d.giorno!=='03/11'?d.giorno+' ':'')+d.ora)+'</span></td>':'<td class="no">✘ manca</td>';
   h+=m?'<td class="'+(m.p>=6?'si':'nu')+'"><b>'+m.p+'/'+m.su+'</b></td>':'<td class="'+(o2?'no':'')+'">'+(o2?'✘ da fare':'<span class="mini">ora 2 chiusa</span>')+'</td>';
   h+=p?'<td class="si">✔ <b>'+p.p+'/'+p.m+'</b>'+(p.ora?' <span class="mini">'+e(p.ora)+'</span>':'')+'</td>':'<td class="'+(o2?'no':'')+'">'+(o2?'✘ da fare':'<span class="mini">ora 2 chiusa</span>')+'</td>';
   h+='<td>'+(r.fermo_da?e(r.fermo_da):'·')+'</td>';
   var vv=(!D.veyon_ok||!v.giri)?'<span class="mini" style="color:#888">n.d.</span>':v.fuori?'<span style="color:#c62828;font-weight:800">fuori compito: '+v.fuori+'</span>':'<span class="mini">ok</span>';
   if(docente){(r.note||[]).forEach(function(z){vv+='<br><span class="mini">'+e(z)+'</span>'})}
   h+='<td style="white-space:normal;min-width:150px;text-align:left">'+vv+'</td><td class="voto"><b>'+r.voto+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>'});
  return h+'</tbody></table></div>'}
