// Vista comune del cruscotto 3INF 02/11 (docente e ragazzi). Dati: cruscotto.json (cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function cella(v,txt){return v===true?'<td class="si" title="'+e(txt||'')+'">✔</td>':v===false?'<td class="no" title="'+e(txt||'')+'">✘</td>':'<td class="nu">·</td>'}
var NOMI={1:'Mastermind 1',2:'Mastermind 2',3:'Slideshow'};
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> · '+e(D.fonte)+'</p>';
  if(D.fonti_ora&&D.fonti_ora.length){h+='<p style="display:flex;flex-wrap:wrap;gap:6px;margin:6px 0">';D.fonti_ora.forEach(function(f){var t=f.iso?Date.parse(f.iso):NaN,v=!f.iso||isNaN(t)||(Date.now()-t)>15*60000;h+='<span style="padding:3px 8px;border-radius:8px;font-size:.8em;border:1px solid '+(v?'#c0392b':'#1a7f37')+';color:'+(v?'#c0392b':'inherit')+'">'+e(f.fonte)+': '+(f.ora?e(f.ora):'nessun dato')+'</span>'});h+='</p>'}
  h+='<p class="mu"><b>Il voto:</b> si parte da 40; per ogni ora +5 unit1.pas, +3 screenshot, +3 codice giusto (vale anche il percorso facilitato). Massimo 80. '+(docente?'È una proposta: la conferma il docente.':'È una proposta: lo conferma il Professore.')+'</p>';
  h+='<div class="tw"><table><thead><tr><th class="fix" rowspan="2">Allievo</th>';
  [1,2,3].forEach(function(o){h+='<th colspan="4" class="o'+o+'">Ora '+o+' · '+NOMI[o]+'</th>'});
  h+='<th colspan="3">Client in rete</th>';
  h+='<th rowspan="2">Fermo da</th><th rowspan="2">'+(docente?'Veyon / note':'Veyon')+'</th><th rowspan="2">Voto</th></tr><tr>';
  [1,2,3].forEach(function(o){h+='<th class="o'+o+'">passo</th><th class="o'+o+'">unit1.pas</th><th class="o'+o+'">foto</th><th class="o'+o+'">codice</th>'});
  h+='<th>passo</th><th>unit1.pas</th><th>foto</th>';
  h+='</tr></thead><tbody>';
  R.forEach(function(r){
    var finito=[1,2].every(function(o){var v=r.ore[o];return v.pas&&v.png});
    h+='<tr><td class="fix"><b>'+e(r.nome)+'</b>'+(finito?' 🏁':'')+'</td>';
    [1,2,3].forEach(function(o){var v=r.ore[o],ps=v.passo?(v.passo+'/'+v.tot):(v.facile?('facile '+v.facile+'/3'):'·');
      var manca=(v.manca||[]).length?'manca: '+v.manca.join(', '):'';
      h+='<td class="o'+o+'" title="'+e(v.titolo||'')+'">'+ps+(v.ultimo?'<br><span class="mini">'+e(v.ultimo)+'</span>':'')+'</td>'+cella(v.pas||(v.stato_cr?false:null),(v.fonti||[]).join(', ')||v.stato_cr)+cella(v.png||(v.stato_cr?false:null),(v.fonti||[]).join(', '))+(v.ok===true?'<td class="si">✔</td>':v.ok===false?'<td class="no" title="'+e(manca)+'">✘<br><span class="mini">'+e(manca)+'</span></td>':'<td class="nu">·</td>')});
    var cl=r.client||{};
    h+='<td>'+(cl.passo?(cl.passo+'/'+cl.tot+(cl.ultimo?'<br><span class="mini">'+e(cl.ultimo)+'</span>':'')):'·')+'</td>'+cella(cl.pas||null,'consegna client')+cella(cl.png||null,'consegna client');
    var vy=r.veyon||{};
    h+='<td>'+(e(r.fermo_da)||'<span class="mu">mai</span>')+'</td><td'+(vy.fuori?' class="no"':'')+'>'+(vy.fuori?vy.fuori+' fuori compito':(vy.giri?'ok':'·'))+(docente&&vy.ultimo?'<br><span class="mini">'+e(vy.ultimo)+'</span>':'')+(docente&&(vy.fuori_dett||[]).length?'<br><span class="mini">'+vy.fuori_dett.map(e).join('<br>')+'</span>':'')+(docente&&(r.note||[]).length?'<br><span class="mini">'+r.note.map(e).join('<br>')+'</span>':'')+'</td>';
    h+='<td><b class="voto">'+(r.voto==null?'—':r.voto)+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>';
  });
  h+='</tbody></table></div>';
  h+='<section class="card"><h2>Come si legge</h2><ol><li><b>passo</b>: a che passo del percorso sei (per esempio 5/10); «facile 2/3» = percorso facilitato.</li><li><b>unit1.pas</b> e <b>foto</b>: ✔ se il file è arrivato; ✘ se manca.</li><li><b>codice</b>: ✔ se il controllo automatico dice che nel tuo unit1.pas ci sono i pezzi giusti (anche col percorso facilitato).</li><li>🏁 = hai consegnato tutto per le prime due ore. Premi F5 per aggiornare.</li></ol></section>';
  return h;
}
