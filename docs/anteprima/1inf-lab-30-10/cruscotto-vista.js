// Vista comune del cruscotto dei tre percorsi (docente e ragazzi). Dati: cruscotto.json (cifrato) o cruscotto-ragazzi.json.
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function cella(v,txt){return v===true?'<td class="si" title="'+e(txt||'')+'">✔</td>':v===false?'<td class="no" title="'+e(txt||'')+'">✘</td>':'<td class="nu">·</td>'}
function disegnaCruscotto(D,docente){
  var R=D.righe||[],h='<p class="mu">Aggiornato alle <b>'+e(D.ora)+'</b> · '+e(D.fonte)+'</p>';
  if(D.kpi_proposti)h+='<p class="mu"><b>KPI proposti, da confermare con il prof:</b> base 40; per ogni ora +5 unit1.pas, +3 screenshot, +3 codice verificato; quiz +7 se almeno 60%. Massimo 80.</p>';
  h+='<div class="tw"><table><thead><tr><th class="fix" rowspan="2">Allievo</th><th rowspan="2">Teoria · quiz</th>';
  [1,2,3].forEach(function(o){h+='<th colspan="4" class="o'+o+'">Ora '+o+' · '+['','pasticcio','soprannome','segnapunti'][o]+'</th>'});
  h+='<th rowspan="2">Fermo da</th><th rowspan="2">Veyon</th><th rowspan="2">Voto</th></tr><tr>';
  [1,2,3].forEach(function(o){h+='<th class="o'+o+'">passo</th><th class="o'+o+'">.pas</th><th class="o'+o+'">foto</th><th class="o'+o+'">codice</th>'});
  h+='</tr></thead><tbody>';
  R.forEach(function(r){
    var finito=[1,2,3].every(function(o){var v=r.ore[o];return v.pas&&v.png});
    var t=r.teoria||{},q=r.quiz;
    h+='<tr><td class="fix"><b>'+e(r.nome)+'</b>'+(finito?' 🏁':'')+'</td><td>'+(t.schede?('schede '+t.schede+'/6'):'<span class="mu">·</span>')+(q?'<br>quiz <b>'+q.giuste+'/'+q.su+'</b>':'')+'</td>';
    [1,2,3].forEach(function(o){var v=r.ore[o],ps=v.passo?(v.passo+'/'+v.tot):(v.facile?('facile '+v.facile+'/3'):'·');
      var manca=(v.manca||[]).length?'manca: '+v.manca.join(', '):'';
      h+='<td class="o'+o+'" title="'+e(v.titolo||'')+'">'+ps+(v.ultimo?'<br><span class="mu">'+e(v.ultimo)+'</span>':'')+'</td>'+cella(v.pas||(v.stato_cr?false:null),v.fonti.join(', ')||v.stato_cr)+cella(v.png||(v.stato_cr?false:null),v.fonti.join(', '))+(v.ok===null?'<td class="nu">·</td>':cella(v.ok,manca)).replace('</td>',(v.ok===false&&docente?'<br><span class="mini">'+e(manca)+'</span>':'')+'</td>')});
    var vy=r.veyon||{};
    h+='<td>'+(e(r.fermo_da)||'<span class="mu">mai</span>')+'</td><td'+(vy.fuori?' class="no"':'')+'>'+(vy.fuori?vy.fuori+' fuori compito':(vy.giri?'ok':'·'))+(docente&&vy.ultimo?'<br><span class="mini">'+e(vy.ultimo)+'</span>':'')+'</td>';
    h+='<td><b class="voto">'+r.voto+'</b><details><summary>il conto</summary><span class="mini">'+(r.conto||[]).map(e).join('<br>')+'</span></details></td></tr>';
  });
  h+='</tbody></table></div>';
  h+='<section class="card"><h2>Come si legge</h2><ol><li>Una riga per ogni presente, dal più avanti al più indietro. 🏁 = ha consegnato unit1.pas e screenshot di tutte e tre le ore.</li><li><b>passo</b>: il passo raggiunto nel percorso (o «facile» per il percorso facilitato) e l\'ora dell\'ultimo segnale.</li><li><b>.pas</b> e <b>foto</b>: ✔ arrivati (dalla pagina di consegna o da Classroom), ✘ manca, · nessun dato.</li><li><b>codice</b>: ✔ il controllo automatico ha trovato i pezzi dell\'ora (ora 1 \'5\' + \'3\', variabili Integer e IntToStr, ora 2 String ed Edit1.Text, ora 3 Integer, StrToInt e IntToStr); ✘ con che cosa manca.</li><li><b>Fermo da</b>: l\'ora dell\'ultima cosa fatta. <b>Veyon</b>: in rosso chi era fuori compito.</li><li><b>Voto</b>: la proposta 40-80; apri «il conto» per vedere il perché.</li></ol></section>';
  return h;
}
