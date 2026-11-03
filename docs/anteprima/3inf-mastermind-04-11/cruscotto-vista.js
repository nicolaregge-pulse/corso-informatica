// Vista del cruscotto 3INF · 04/11 Mastermind in rete (docente e ragazzi). Dati: cruscotto.json (anche cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function pill(ok,txt){return '<td class="'+(ok?'si':'no')+'">'+(ok?'✔ ':'✘ ')+e(txt||'')+'</td>'}
function num(n,t,s){n=n||0;return '<td class="'+(n>=s?'si':n>0?'nu':'no')+'"><b>'+n+'/'+t+'</b></td>'}
function qz(q,s){return q?'<td class="'+(q.p>=s?'si':'nu')+'">✔ <b>'+q.p+'/'+q.m+'</b></td>':'<td class="no">✘ da fare</td>'}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> · '+e(D.fonte)+'</p>';
  h+='<p class="mu"><b>Come si legge:</b> ✔ verde = fatto; ✘ rosso = manca. I più avanti stanno in alto.</p>';
  h+='<p class="mu"><b>Il voto (KPI proposti, in attesa del sì del Professore):</b> si parte da 40; client collegato al server +10; partita di classe finita con il codice indovinato +10; commit su GitHub con messaggio chiaro +10; quiz su Moduli (8 domande) con almeno 6 giuste +10. Massimo 80.</p>';
  if(!R.length){return h+'<p class="ante">Presenze non ancora segnate: appena il Professore le segna, qui compare una riga per ogni presente.</p>'}
  h+='<div class="tw"><table><thead><tr><th class="fix">Allievo</th><th>Passo (7)</th><th>Collegato</th><th>Partita finita</th><th>Commit GitHub</th><th>Quiz Moduli (8)</th><th>Fermo da</th><th>'+(docente?'Veyon / note':'Veyon')+'</th><th>Voto</th></tr></thead><tbody>';
  R.forEach(function(r){var v=r.veyon||{},q=r.quiz;
   h+='<tr><td class="fix"><b>'+e(r.nome)+'</b></td>';
   h+=num(r.passo,7,7);
   h+=pill(r.collegato,r.collegato?'collegato':'manca');
   h+=pill(r.partita,r.partita?'indovinato':'manca');
   h+=pill(r.github,r.github?'consegnato':'da fare');
   h+=qz(q,6);
   h+='<td>'+(r.fermo_da?e(r.fermo_da):'·')+'</td>';
   var vv=v.fuori?'<span style="color:#c62828;font-weight:800">fuori compito: '+v.fuori+'</span>':'<span class="mini">ok</span>';
   if(docente){(r.note||[]).forEach(function(z){vv+='<br><span class="mini">'+e(z)+'</span>'})}
   h+='<td style="white-space:normal;min-width:150px;text-align:left">'+vv+'</td><td class="voto"><b>'+r.voto+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>'});
  return h+'</tbody></table></div>'}
