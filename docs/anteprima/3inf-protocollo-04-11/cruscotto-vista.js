// Vista generica del cruscotto (docente e ragazzi): colonne da D.colonne, celle da r.celle[k] = {ok:true|false|null, t:testo}.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function cella(c){if(!c)return '<td class="nu">-</td>';return '<td class="'+(c.ok===true?'si':c.ok===false?'no':'nu')+'" style="white-space:normal">'+(c.ok===true?'✔ ':c.ok===false?'✘ ':'? ')+e(c.t)+'</td>'}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> · '+e(D.fonte)+'</p>';
  (D.avvisi||[]).forEach(function(a){h+='<p style="color:#c62828;font-weight:800">'+e(a)+'</p>'});
  h+='<p class="mu"><b>Come si legge:</b> ✔ verde = fatto; ✘ rosso = manca; ? = arrivato ma da controllare. I più avanti stanno in alto.</p><p class="mu"><b>Il voto (KPI proposti, in attesa del sì del Professore):</b> '+e(D.legenda||'')+'</p>';
  if(!R.length)return h+'<p>Nessun iscritto da mostrare.</p>';
  h+='<div class="tw"><table><thead><tr><th class="fix">Allievo</th>';
  (D.colonne||[]).forEach(function(c){h+='<th>'+e(c.l)+'</th>'});
  h+='<th>Fermo da</th><th>'+(docente?'Veyon / note':'Veyon')+'</th><th>Voto proposto</th></tr></thead><tbody>';
  R.forEach(function(r){var v=r.veyon||{};h+='<tr><td class="fix"><b>'+e(r.nome)+'</b></td>';
    (D.colonne||[]).forEach(function(c){h+=cella((r.celle||{})[c.k])});
    var vv=(!D.veyon_ok||!v.giri)?'<span class="mini" style="color:#888">n.d.</span>':v.fuori?'<span style="color:#c62828;font-weight:800">fuori compito: '+v.fuori+(v.fuori>1?' volte':' volta')+'</span>'+(docente&&v.ultima?'<br><span class="mini">'+e(v.ultima)+'</span>':''):'<span style="color:#1a7f37">in compito</span>';
    if(docente)(r.note||[]).forEach(function(z){vv+='<br><span class="mini">'+e(z)+'</span>'});
    h+='<td>'+(r.fermo_da?e(r.fermo_da):'·')+'</td><td style="white-space:normal;min-width:150px;text-align:left">'+vv+'</td><td class="voto"><b>'+(r.voto==null?'—':r.voto)+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>'});
  return h+'</tbody></table></div>'}

// Sezione «Il mio comportamento» (solo ragazzi): Nome C., verde/rosso, mai COSA guardavano, niente voto.
function disegnaComportamento(D){
  var R=D.righe||[];
  var h='<section id="comportamento" style="border:3px solid #0969da;border-radius:12px;padding:10px 14px;margin:10px 0"><h2 style="margin-top:0">Il mio comportamento</h2>'
  +'<p class="mu"><b>Come si legge:</b> il Professore guarda gli schermi; qui vedi se eri sul lavoro o fuori. Nessun punto si toglie da solo.</p>';
  if(!D.veyon_ok||!R.length)return h+'<p class="mu">Il controllo degli schermi non è ancora arrivato. Premi F5 tra poco.</p></section>';
  h+='<div style="display:flex;flex-wrap:wrap;gap:8px">';
  R.forEach(function(r){var v=r.veyon||{};if(!v.giri){h+='<span style="padding:6px 10px;border-radius:999px;background:#eee;color:#555"><b>'+e(r.nome)+'</b> · non ancora controllato</span>';return}
    var f=v.fuori>0;
    h+='<span style="padding:6px 10px;border-radius:999px;color:#fff;background:'+(f?'#c62828':'#1a7f37')+'"><b>'+e(r.nome)+'</b> · '+(f?'fuori compito: '+v.fuori+(v.fuori>1?' volte':' volta'):'in compito')+' · ultimo controllo '+e(v.ora||'')+'</span>'});
  h+='</div>';
  if(R.some(function(r){return (r.veyon||{}).fuori>0}))h+='<p style="font-weight:700;margin-top:10px">Se eri fuori compito: succede. Ora torna sul lavoro: la pagina è qui sopra.</p>';
  return h+'</section>'}
