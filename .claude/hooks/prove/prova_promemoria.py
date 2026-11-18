#!/usr/bin/env python3
"""Prove di promemoria-errori.py v1.3: il «primo messaggio del giorno» lo consuma solo un messaggio umano;
dal primo messaggio umano si ordina di seguire report/PROCEDURA-MATTINA-<ultima versione>.md del riservato."""
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

# 6) v1.3: frase della procedura del mattino (riservato finto nella cartella temporanea)
def lancia_r(prompt, stato, riservato):
    env = dict(os.environ, CORSO_STATO_RILETTURA=stato, CORSO_RISERVATO=riservato)
    r = subprocess.run([sys.executable, HOOK], input=json.dumps({"cwd": os.path.join(H, "..", ".."), "prompt": prompt}),
                       capture_output=True, text=True, env=env)
    return json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"] if r.stdout.strip() else ""

riss = os.path.join(d, "riservato")
os.makedirs(os.path.join(riss, "report"))
for v in ("v1.0", "v1.2", "v1.10", "v1.9"):
    open(os.path.join(riss, "report", "PROCEDURA-MATTINA-%s.md" % v), "w").write("x")
open(os.path.join(riss, "report", "PROCEDURA-MATTINA-v9.9-BOZZA.md"), "w").write("x")
t1 = lancia_r("buongiorno", os.path.join(d, "p1.txt"), riss)
caso("procedura: frase presente al primo messaggio umano", "PROCEDURA DEL MATTINO (v1.3)" in t1, True)
caso("procedura: percorso completo dell'ultima versione (1.10 > 1.9)", os.path.join(riss, "report", "PROCEDURA-MATTINA-v1.10.md") in t1, True)
caso("procedura: ordine PRIMA di rispondere nel merito", "PRIMA di rispondere nel merito" in t1, True)
caso("procedura: la bozza v9.9-BOZZA non conta", "v9.9" in t1, False)
caso("procedura: la frase viene dopo la rilettura", t1.index("RILETTURA DEL MATTINO") < t1.index("PROCEDURA DEL MATTINO"), True)
caso("procedura: solo Read, Grep e Write, non pubblica", "Read, Grep e Write" in t1 and "non pubblichi nulla" in t1, True)
t2 = lancia_r("e ora?", os.path.join(d, "p1.txt"), riss)
caso("procedura: secondo messaggio senza frase", "PROCEDURA DEL MATTINO" in t2, False)
t3 = lancia_r("Promemoria: preparazione di domani", os.path.join(d, "p3.txt"), riss)
caso("procedura: prompt di trigger senza frase", "PROCEDURA DEL MATTINO" in t3, False)
vuoto = os.path.join(d, "vuoto"); os.makedirs(os.path.join(vuoto, "report"))
t4 = lancia_r("ciao", os.path.join(d, "p4.txt"), vuoto)
caso("procedura: file mancante, la frase lo dice", "non si trova" in t4 and "RILETTURA DEL MATTINO" in t4, True)
caso("procedura: spento con stato vuoto, nessuna frase", "PROCEDURA DEL MATTINO" in lancia_r("ciao", "", riss), False)
caso("procedura: riservato vero, percorso completo",
     "/home/user/corso-informatica-riservato/report/PROCEDURA-MATTINA-v" in lancia("ciao", os.path.join(d, "p7.txt")), True)

giusti = sum(1 for _, o, a in casi if o == a)
for n, o, a in casi:
    if o != a: print("SBAGLIATO:", n, "atteso", a, "ottenuto", o)
print("%d/%d" % (giusti, len(casi)))
sys.exit(0 if giusti == len(casi) else 1)
