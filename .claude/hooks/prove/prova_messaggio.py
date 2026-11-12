#!/usr/bin/env python3
"""Prove di controllo-messaggio.py ridotto del 04/11/2026: (a), (b), (d), (e)+(o), (gg), (hh) e main.

Uso: python3 /home/user/corso-informatica/.claude/hooks/prove/prova_messaggio.py
Stampa «N/N» (casi giusti / casi totali) e le righe dei casi sbagliati.
Lavora su repository finti in una cartella temporanea: non tocca i repository veri.
"""
import contextlib
import datetime
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import time
from zoneinfo import ZoneInfo

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("cm", os.path.join(H, "controllo-messaggio.py"))
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)
T = tempfile.mkdtemp()
TZ = ZoneInfo("Europe/Rome")


def sh(*a, cwd=None):
    subprocess.run(a, cwd=cwd, check=True, capture_output=True)


def commit(cwd, msg):
    sh("git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", msg, cwd=cwd)


# repository pubblico finto con origin
pub, bare = T + "/pub", T + "/bare.git"
sh("git", "init", "-q", "--bare", bare)
sh("git", "init", "-q", "-b", "main", pub)
os.makedirs(pub + "/docs/1inf")
open(pub + "/docs/1inf/index.html", "w").write("v1")
sh("git", "add", "-A", cwd=pub)
commit(pub, "a")
sh("git", "remote", "add", "origin", bare, cwd=pub)
sh("git", "push", "-q", "origin", "main", cwd=pub)
sh("git", "fetch", "-q", cwd=pub)
cm.PUB = pub
LINK = "Apri https://nicolaregge-pulse.github.io/corso-informatica/1inf/"
casi = []


def caso(nome, ottenuto, atteso):
    casi.append((nome, bool(ottenuto), atteso))


# (e) link senza PUBBLICATO
caso("e: link, pagine appena pushate, nessun timbro", cm.controllo_link_senza_pubblicato(LINK), True)
gd = subprocess.run(["git", "-C", pub, "rev-parse", "--absolute-git-dir"], capture_output=True, text=True).stdout.strip()
head = subprocess.run(["git", "-C", pub, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
open(gd + "/ultimo-pubblicato", "w").write(head)
caso("e: link dopo PUBBLICATO (timbro = HEAD)", cm.controllo_link_senza_pubblicato(LINK), False)
open(pub + "/docs/1inf/index.html", "w").write("v2")
caso("e: link con pagina modificata e non committata", cm.controllo_link_senza_pubblicato(LINK), True)
sh("git", "add", "-A", cwd=pub)
commit(pub, "b")
caso("e: link con commit non pushato", cm.controllo_link_senza_pubblicato(LINK), True)
sh("git", "push", "-q", "origin", "main", cwd=pub)
sh("git", "fetch", "-q", cwd=pub)
caso("e: link dopo il push ma prima di PUBBLICATO", cm.controllo_link_senza_pubblicato(LINK), True)
caso("e: messaggio senza link al sito", cm.controllo_link_senza_pubblicato("Tutto in ordine."), False)
open(pub + "/README.md", "w").write("x")
sh("git", "add", "-A", cwd=pub)
commit(pub, "c")
sh("git", "push", "-q", "origin", "main", cwd=pub)
head2 = subprocess.run(["git", "-C", pub, "rev-parse", "HEAD~1"], capture_output=True, text=True).stdout.strip()
open(gd + "/ultimo-pubblicato", "w").write(head2)
caso("e: dopo PUBBLICATO solo un README cambiato (niente docs/)", cm.controllo_link_senza_pubblicato(LINK), False)

# (n) errore da registrare
tr = T + "/tr.jsonl"


def transcript(testo_docente):
    with open(tr, "w") as f:
        f.write(json.dumps({"type": "user", "message": {"content": testo_docente}}) + "\n")
        f.write(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": "ok"}]}}) + "\n")


# (o) link al riservato
RIS_URL = "https://github.com/nicolaregge-pulse/corso-informatica-riservato/blob/main/diario/x.md"
caso("o: link al riservato senza profilo personale", cm.controllo_link_riservato("Apri " + RIS_URL), True)
caso("o: link al riservato con finestra personale", cm.controllo_link_riservato("Nella finestra dell'account PERSONALE apri " + RIS_URL), False)
caso("o: script dal riservato", cm.controllo_link_riservato("Account personale: copia da https://github.com/nicolaregge-pulse/corso-informatica-riservato/blob/main/strumenti/automazione-corso.gs"), True)

# main(): blocca una volta sola, non blocca i subagenti, input rotto = exit 0
def main_con(dati):
    sys.stdin = io.StringIO(json.dumps(dati))
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        cm.main()
    return "block" in out.getvalue()



# (a) ordine copia/incolla
caso("a: riquadro tra Ctrl+C e Ctrl+V", cm.controllo_copia_incolla("1. Apri la pagina e premi Ctrl+A e Ctrl+C.\n2. Copia questo:\n```\nciao\n```\n3. Premi Ctrl+V.") is not None, True)
caso("a: ordine giusto", cm.controllo_copia_incolla("1. Apri il Modulo.\n2. Apri la pagina e premi Ctrl+A e Ctrl+C.\n3. Torna sul Modulo e premi Ctrl+V."), False)
caso("a: riquadro da incollare senza copia della pagina", cm.controllo_copia_incolla("Incolla questo:\n```\nciao\n```"), False)

# (b) bloccante in prima riga (+ firma già fatta, ex m)
caso("b: firma in fondo", cm.controllo_bloccanti("Il quiz è pronto.\nLa 2INF lavora.\nRicordati la firma entro le 14:05.") is not None, True)
caso("b: firma in prima riga", cm.controllo_bloccanti("FIRMA: 3INF entro le 14:05.\nIl quiz è pronto.\nAltro."), False)
caso("b: PUBB non riuscito in fondo", cm.controllo_bloccanti("Ecco il pacchetto.\nTitolo pronto.\nPUBB 2 NON riuscito: pubblica a mano.") is not None, True)
caso("b: PUBB non riuscito in prima riga", cm.controllo_bloccanti("PUBB 2 NON riuscito: pubblica a mano.\nTitolo:\nTesto:"), False)
cm.PUB = pub
oggi = datetime.datetime.now(TZ).strftime("%d/%m/%Y")
open(pub + "/FIRME-REGISTRO-2026-27.md", "w").write(
    "# 00 Firme\n\n## 01 Oggi %s\n\n1. Ore 08-09, 09-10, 1INF: firmate prima della prima ora.\n2. Ora 11-12, 2INF: firmata.\n" % oggi)
caso("b: firma in fondo ma oggi tutto firmato (ex m)", cm.controllo_bloccanti("Il quiz è pronto.\nLa 2INF lavora.\nLa firma è a posto."), False)
os.remove(pub + "/FIRME-REGISTRO-2026-27.md")

# (d) «pubblicato» senza verifica VERDE
risd = T + "/risd"
os.makedirs(risd + "/dati/verifiche-lezione")
cm.RIS = risd
caso("d: «pubblicato» per la 2INF senza verifica", cm.controllo_pronto_senza_verifica("Compito della 2INF pubblicato.") is not None, True)
adesso = datetime.datetime.now(TZ)
json.dump({"ora": adesso.isoformat(), "esito": "VERDE"}, open(risd + "/dati/verifiche-lezione/%s_2INF.json" % adesso.strftime("%Y-%m-%d"), "w"))
caso("d: «pubblicato» con verifica VERDE recente", cm.controllo_pronto_senza_verifica("Compito della 2INF pubblicato."), False)
caso("d: «non ancora pubblicato»", cm.controllo_pronto_senza_verifica("Il compito della 3INF non è ancora pubblicato."), False)
caso("d: «pubblica a mano» non è «pubblicato»", cm.controllo_pronto_senza_verifica("PUBB 3 NON riuscito per la 3INF: pubblica a mano."), False)

# (gg) ora della giornata: solo se il docente ne ha parlato davvero
transcript("Prima ora teoria: integer e string")
caso("gg: «prima ora» senza orario", cm.controllo_ora_ordinale("Metto String e Integer nella teoria del laboratorio.", {"transcript_path": tr}) is not None, True)
caso("gg: «prima ora» con l'orario", cm.controllo_ora_ordinale("Metto String e Integer nell'ora 8-9 della 1INF.", {"transcript_path": tr}), False)
transcript("PUBB 2")
caso("gg: «PUBB 2» senza orario", cm.controllo_ora_ordinale("Compito pronto, lo pubblico.", {"transcript_path": tr}) is not None, True)
caso("gg: «PUBB 2» con l'orario", cm.controllo_ora_ordinale("PUBB 2 (9-10): compito in coda.", {"transcript_path": tr}), False)
transcript("Ci vediamo tra 1 ora, prepara il quiz")
caso("gg: «tra 1 ora» non è un'ora della giornata", cm.controllo_ora_ordinale("Preparo il quiz.", {"transcript_path": tr}), False)
transcript("Va bene, sistema il cruscotto")
caso("gg: il docente non parla di ore", cm.controllo_ora_ordinale("Sistemo il cruscotto.", {"transcript_path": tr}), False)

# (hh) «non ha consegnato» con dato non fresco (#314, 12/11/2026)
ora_x = datetime.datetime(2026, 11, 12, 13, 54, 30, tzinfo=TZ)
caso("hh: «non ha consegnato» con dato di 6 minuti fa",
     cm.controllo_dato_vecchio("ROSSI Mario non ha consegnato il quiz. Fonte: foglio scaricato alle 13:55; risposte lette fino alle 13:48:57.", ora_x) is not None, True)
caso("hh: «non ha consegnato» senza fonte né ora",
     cm.controllo_dato_vecchio("ROSSI Mario non ha consegnato il quiz.", ora_x) is not None, True)
caso("hh: «non ha consegnato» con dato di 30 secondi fa",
     cm.controllo_dato_vecchio("ROSSI Mario non ha consegnato il quiz (letto dal foglio alle 13:54:05).", ora_x), False)
caso("hh: «non risulta consegnato» nel dato vecchio è la frase giusta",
     cm.controllo_dato_vecchio("ROSSI Mario non risulta consegnato nel dato delle 13:48 (6 minuti fa), può essere cambiato.", ora_x), False)
caso("hh: «non ha consegnato» con «non provato»",
     cm.controllo_dato_vecchio("ROSSI Mario non ha consegnato: non provato, ultimo dato delle 13:40.", ora_x), False)
caso("hh: frase tra virgolette non conta",
     cm.controllo_dato_vecchio("Il messaggio di prima diceva «non ha consegnato» ma era sbagliato.", ora_x), False)
caso("hh: «non hanno ancora fatto il quiz» senza ora",
     cm.controllo_dato_vecchio("Tre allievi non hanno ancora fatto il quiz.", ora_x) is not None, True)
caso("hh: main blocca «non ha consegnato» senza ora", main_con({"last_assistant_message": "Ok.\nROSSI Mario non ha consegnato il quiz."}), True)

# controlli tolti il 04/11/2026: frasi che prima bloccavano e ora passano
for frase in ("Onestamente il cruscotto è lento.", "Il quiz di BIANCHI non è arrivato.", "Report pronto: 2 consegnati su 14.",
              "Fatto.", "Accendo 4 aiutanti per le tre classi.", "Se la scheda è già aperta, salta alla parte B."):
    caso("tolto: «%s» non blocca" % frase, main_con({"last_assistant_message": frase}), False)

caso("main: messaggio con firma in fondo bloccato", main_con({"last_assistant_message": "Ok.\nAltro.\nRicordati la firma entro le 14:05."}), True)
caso("main: stop_hook_active non blocca di nuovo", main_con({"last_assistant_message": "Ok.\nAltro.\nRicordati la firma.", "stop_hook_active": True}), False)
caso("main: subagente non controllato", main_con({"last_assistant_message": "Ok.\nAltro.\nRicordati la firma.", "agent_id": "x"}), False)
r = subprocess.run([sys.executable, os.path.join(H, "controllo-messaggio.py")], input="non json", capture_output=True, text=True)
caso("main: input rotto esce 0 senza output", r.returncode == 0 and not r.stdout, True)

giusti = sum(1 for _, o, a in casi if o == a)
for n, o, a in casi:
    if o != a:
        print("SBAGLIATO:", n, "atteso", a, "ottenuto", o)
print("%d/%d" % (giusti, len(casi)))
