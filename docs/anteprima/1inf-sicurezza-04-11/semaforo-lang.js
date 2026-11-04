/* scelta lingua + ridisegno: usa DATI e DOC definiti dalla pagina */
function barraLingue(id,ridisegna){var b=document.getElementById(id);var N={it:'Italiano',ar:'العربية',zh:'中文'};
 function d(){b.innerHTML=['it','ar','zh'].map(function(l){return '<button type="button" data-l="'+l+'" class="'+(LG===l?'on':'')+'">'+N[l]+'</button>'}).join('');
  [].forEach.call(b.querySelectorAll('button'),function(x){x.onclick=function(){LG=x.dataset.l;try{localStorage.setItem('lg-sem',LG)}catch(e){}d();ridisegna()}})}
 try{var s=localStorage.getItem('lg-sem');if(T[s])LG=s}catch(e){}d()}
function applicaLingua(){document.getElementById('titolo').textContent=T[LG].h;document.getElementById('sub').textContent=T[LG].sub;document.getElementById('app').className=LG==='ar'?'rtl':'';document.documentElement.lang=LG}
