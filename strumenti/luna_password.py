"""Dopo l'export del fork Luna: motore condiviso con treno-godot + riquadro password per le facce protette."""
import os
d = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "giochi", "treno-luna")
for f in ["index.wasm", "index.js", "index.audio.worklet.js", "index.audio.position.worklet.js"]:
    if os.path.exists(os.path.join(d, f)):
        os.remove(os.path.join(d, f))
h = open(os.path.join(d, "index.html"), encoding="utf-8").read()
h = h.replace('src="index.js"', 'src="../treno-godot/index.js"').replace('"executable":"index"', '"executable":"../treno-godot/index","mainPack":"index.pck"')
box = r'''<div id="pwbox" style="position:fixed;left:50%;top:14px;transform:translateX(-50%);z-index:9;background:#161b22;color:#e6edf3;border:2px solid #ffd34d;border-radius:12px;padding:10px 14px;font:16px system-ui,Arial;text-align:center;max-width:92vw">
<b>Facce della 1INF</b> — scrivi la password della classe · اكتب كلمة السر · 写密码<br>
<input id="pwl" type="password" style="font-size:16px;padding:6px;margin:6px;border-radius:6px"> <button onclick="apriFacce()" style="font-size:16px;padding:6px 12px;border-radius:6px;background:#238636;color:#fff;border:0">Apri</button>
<button onclick="document.getElementById('pwbox').remove()" style="font-size:14px;padding:6px 10px;border-radius:6px;border:0">Gioca senza</button><div id="pwm" style="font-size:14px"></div></div>
<script>
var FACCE_URL='/corso-informatica/giochi/treno-luna/facce.json';
function b64(s){return Uint8Array.from(atob(s),function(c){return c.charCodeAt(0)})}
async function decifra(pw){var d=await (await fetch(FACCE_URL+'?t='+Date.now(),{cache:'no-store'})).json();
 var km=await crypto.subtle.importKey('raw',new TextEncoder().encode(pw),'PBKDF2',false,['deriveKey']);
 var k=await crypto.subtle.deriveKey({name:'PBKDF2',salt:b64(d.salt),iterations:d.iter,hash:'SHA-256'},km,{name:'AES-GCM',length:256},false,['decrypt']);
 return new TextDecoder().decode(await crypto.subtle.decrypt({name:'AES-GCM',iv:b64(d.iv)},k,b64(d.ct)))}
async function apriFacce(pw,auto){pw=pw||document.getElementById('pwl').value;try{window.FACCE_JSON=await decifra(pw);
 try{localStorage.setItem('luna-pw',JSON.stringify({p:pw,t:Date.now()}))}catch(e){}
 var b=document.getElementById('pwbox');if(b)b.remove()}catch(e){if(!auto)document.getElementById('pwm').textContent='Password sbagliata, riprova.'}}
try{var s=JSON.parse(localStorage.getItem('luna-pw')||'null');if(s&&Date.now()-s.t<86400000)apriFacce(s.p,true)}catch(e){}
</script>'''
if 'id="pwbox"' not in h:
    h = h.replace("<body>", "<body>" + box, 1)
open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(h)
print("ok")
