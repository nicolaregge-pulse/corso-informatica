#!/usr/bin/env python3
"""Prove di promemoria-errori.py v1.2: il «primo messaggio del giorno» lo consuma solo un messaggio umano."""
import json, os, subprocess, sys, tempfile
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HOOK = os.path.join(H, "promemoria-errori.py")
casi = []
def caso(n, o, a): casi.append((n, o, a))

def lancia(prompt, stato):
    env = dict(os.environ, CORSO_STATO_RILETTURA=stato)
    r = subprocess.run([sys.executable, HOOK], input=json.dumps({"cwd": os.path.join(H, "..", ".."), "prompt": prompt}),
                       capture_output=True, text=True, env=env)
    return r.stdout

def ha_rilettura(out):
    return "RILETTURA DEL MATTINO" in out

TRIGGER = [
    "<task-notification>\n<task-type>queued-remote-notifications</task-type>\n<summary>1 unread notification (scheduled trigger (the stored prompt of a routine or task on this account): 1)</summary>",
    "PROMEMORIA: preparazione di domani",
    "Controllo di fine giornata avviato: ...",
    "Preparazione notturna 19/11: esegui .claude/passi-notturni.md",
    "Fired by routine trig_01113v",
]
d = tempfile.mkdtemp()
# 1) notte: il trigger non consuma il segnale; poi il messaggio umano lo riceve
st = os.path.join(d, "s1.txt")
for i, t in enumerate(TRIGGER):
    caso("trigger %d: niente rilettura" % i, ha_rilettura(lancia(t, st)), False)
caso("trigger: file di stato non creato", os.path.exists(st), False)
caso("primo messaggio umano dopo i trigger: rilettura", ha_rilettura(lancia("ciao, buongiorno", st)), True)
caso("secondo messaggio umano: niente rilettura", ha_rilettura(lancia("e ora?", st)), False)
caso("secondo messaggio: restano le regole brevi", "RILETTURA" not in lancia("e ora?", st) and len(lancia("e ora?", st)) > 100, True)
# 2) prompt senza campo prompt e prompt vuoto: umano
st2 = os.path.join(d, "s2.txt")
caso("prompt vuoto trattato come umano", ha_rilettura(lancia("", st2)), True)
# 3) frase umana che contiene la parola promemoria a metà: umano
st3 = os.path.join(d, "s3.txt")
caso("«dammi un promemoria» è umano", ha_rilettura(lancia("dammi un promemoria per domani", st3)), True)
# 4) spento con stato vuoto
caso("CORSO_STATO_RILETTURA vuoto: spento", ha_rilettura(lancia("ciao", "")), False)
# 5) testo: bozze escluse e percorso completo
caso("testo esclude BOZZA", "ESCLUSI i file con BOZZA" in lancia("ciao", os.path.join(d, "s5.txt")), True)
caso("testo: percorso completo didaweb-auto.js",
     "corso-informatica-riservato/strumenti/didaweb-auto.js" in lancia("ciao", os.path.join(d, "s6.txt")), True)
caso("uscita JSON valida", json.loads(lancia("ciao", os.path.join(d, "s7.txt")))["hookSpecificOutput"]["hookEventName"], "UserPromptSubmit")

giusti = sum(1 for _, o, a in casi if o == a)
for n, o, a in casi:
    if o != a: print("SBAGLIATO:", n, "atteso", a, "ottenuto", o)
print("%d/%d" % (giusti, len(casi)))
sys.exit(0 if giusti == len(casi) else 1)
