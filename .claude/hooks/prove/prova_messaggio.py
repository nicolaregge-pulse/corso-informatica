#!/usr/bin/env python3
"""Prove dei controlli aggiunti a controllo-messaggio.py il 28/10/2026 sera (e-r).

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

# (f) promesse di tempi
caso("f: «dovrebbero arrivare entro pochi minuti»", cm.controllo_promessa_tempi("I quiz sono in coda: lo script li pubblica entro pochi minuti."), True)
caso("f: «dovrebbe partire» che non riguarda lo script", cm.controllo_promessa_tempi("Se Godot parte dai PC, anche Eclipse dovrebbe partire."), False)
caso("f: promessa con piano B", cm.controllo_promessa_tempi("Esce entro 5 minuti; intanto il piano B: incolla l'annuncio."), False)
caso("f: frase senza promesse", cm.controllo_promessa_tempi("Il compito è su Classroom (PUBLISHED)."), False)

# (g) voti DIDAweb
STR = "```\n28/10/2026 h 5 | Lazarus | ROSSI MARIO;60\n```"
caso("g: stringa voti senza Disciplina", cm.controllo_voti_senza_disciplina(STR), True)
caso("g: stringa voti con Disciplina", cm.controllo_voti_senza_disciplina("**Disciplina da scegliere: LABORATORIO PROFESSIONALE**\n" + STR), False)
caso("g: data senza ora non è una stringa voti", cm.controllo_voti_senza_disciplina("Lezione del 28/10/2026 alle 9."), False)

# (h) nessuna AI
caso("h: «nessuna AI visibile»", cm.controllo_nessuna_ai("PC 12: nessuna AI visibile."), True)
caso("h: con «tutte le finestre»", cm.controllo_nessuna_ai("PC 12: ho visto tutte le finestre, nessuna AI."), False)
caso("h: AI citata tra virgolette", cm.controllo_nessuna_ai("La regola dice «nessuna AI» nelle verifiche, va bene."), False)

# (i) utente non indicato
caso("i: «utente non indicato»", cm.controllo_utente_non_indicato("PC38: video di pugilato, utente non indicato."), True)
caso("i: con la domanda «chi c'è»", cm.controllo_utente_non_indicato("PC38: utente non indicato. Chi c'è al PC 38?"), False)

# (j) parole inutili
caso("j: «onestamente»", cm.controllo_parole_inutili("Onestamente il cruscotto è lento."), True)
caso("j: frase normale", cm.controllo_parole_inutili("Il cruscotto è lento."), False)

# (k) catene di coordinate
caso("k: catena con · e verbo", cm.controllo_catene_coordinate("1. Account PIAMARTA · finestra arancione · in alto: clicca il «+»"), True)
caso("k: campanelle con · senza verbo", cm.controllo_catene_coordinate("Campanelle: 08:55 · 09:55 · 10:50"), False)

# (l) se / salta
caso("l: «salta alla Parte B»", cm.controllo_se_salta("Se la scheda è già aperta, salta alla parte B."), True)
caso("l: istruzioni lineari", cm.controllo_se_salta("1. Premi Ctrl+T.\n2. Scrivi l'indirizzo."), False)

# (m) firma già fatta
oggi = datetime.datetime.now(TZ).strftime("%d/%m/%Y")
open(pub + "/FIRME-REGISTRO-2026-27.md", "w").write(
    "# 00 Firme\n\n## 01 Oggi %s\n\n1. Ore 08-09, 09-10, 1INF: firmate prima della prima ora.\n2. Ora 11-12, 2INF: firmata.\n" % oggi)
caso("m: promemoria firma con tutto firmato", cm.controllo_firma_gia_fatta("Ricordati di firmare le ore della 2INF."), True)
caso("m: nessun promemoria", cm.controllo_firma_gia_fatta("La 2INF lavora sul quiz."), False)
open(pub + "/FIRME-REGISTRO-2026-27.md", "a").write("3. Ore 12-13, 13-14, 3INF: da firmare.\n")
caso("m: promemoria firma con un'ora da firmare", cm.controllo_firma_gia_fatta("FIRMA: la 3INF va firmata entro le 14:05."), False)
os.remove(pub + "/FIRME-REGISTRO-2026-27.md")
caso("m: file delle firme assente", cm.controllo_firma_gia_fatta("Ricordati di firmare."), False)

# (n) errore da registrare
tr = T + "/tr.jsonl"


def transcript(testo_docente):
    with open(tr, "w") as f:
        f.write(json.dumps({"type": "user", "message": {"content": testo_docente}}) + "\n")
        f.write(json.dumps({"type": "assistant", "message": {"content": [{"type": "text", "text": "ok"}]}}) + "\n")


transcript("Scrivi subito questo errore nel registro degli errori")
caso("n: richiesta di registrare, risposta senza numero", cm.controllo_errore_rimandato("Lo faccio a fine giornata.", {"transcript_path": tr}), True)
caso("n: richiesta di registrare, risposta con #139", cm.controllo_errore_rimandato("Registrato come #139.", {"transcript_path": tr}), False)
transcript("Pubblica il quiz della 2INF")
caso("n: messaggio del docente senza richiesta", cm.controllo_errore_rimandato("Fatto il quiz.", {"transcript_path": tr}), False)

# (o) link al riservato
RIS_URL = "https://github.com/nicolaregge-pulse/corso-informatica-riservato/blob/main/diario/x.md"
caso("o: link al riservato senza profilo personale", cm.controllo_link_riservato("Apri " + RIS_URL), True)
caso("o: link al riservato con finestra personale", cm.controllo_link_riservato("Nella finestra dell'account PERSONALE apri " + RIS_URL), False)
caso("o: script dal riservato", cm.controllo_link_riservato("Account personale: copia da https://github.com/nicolaregge-pulse/corso-informatica-riservato/blob/main/strumenti/automazione-corso.gs"), True)

# (p) indirizzo diretto Apps Script
caso("p: indirizzo /home/projects/", cm.controllo_script_diretto("Apri https://script.google.com/home/projects/1AbC/edit"), True)
caso("p: indirizzo /home", cm.controllo_script_diretto("Apri https://script.google.com/home"), False)

# (q) lungo in lezione
lungo = "\n".join("riga %d" % i for i in range(40))
mer_10 = datetime.datetime(2026, 10, 28, 10, 0, tzinfo=TZ)
mer_18 = datetime.datetime(2026, 10, 28, 18, 0, tzinfo=TZ)
sab_10 = datetime.datetime(2026, 10, 31, 10, 0, tzinfo=TZ)
caso("q: 40 righe mercoledì alle 10", cm.controllo_lungo_in_lezione(lungo, mer_10), True)
caso("q: 40 righe mercoledì alle 18", cm.controllo_lungo_in_lezione(lungo, mer_18), False)
caso("q: 40 righe sabato alle 10", cm.controllo_lungo_in_lezione(lungo, sab_10), False)
caso("q: 40 righe dentro un riquadro alle 10", cm.controllo_lungo_in_lezione("```\n" + lungo + "\n```", mer_10), False)

# (r) non risulta
caso("r: «non ha caricato» senza fonti", cm.controllo_non_risulta("Picco non ha caricato niente."), True)
caso("r: «non ha caricato» dopo il clone", cm.controllo_non_risulta("Ho controllato con il clone del repository: non ha caricato."), False)
caso("r: «non hanno consegnato» letto su Classroom", cm.controllo_non_risulta("Su Classroom non hanno ancora consegnato: 4."), False)
caso("r: «nessuno ha consegnato» senza fonti", cm.controllo_non_risulta("Alle 9:10 nessuno ha consegnato."), True)

# (g) voti sotto 40
caso("g: voto 35 nella stringa", cm.controllo_voti_senza_disciplina("Disciplina: LAB\n28/10/2026 h 5 | x | ROSSI MARIO;35 BIANCHI ANNA;60"), True)
caso("g: voti 40-80 con Disciplina", cm.controllo_voti_senza_disciplina("Disciplina: LAB\n28/10/2026 h 5 | x | ROSSI MARIO;40 BIANCHI ANNA;80"), False)

# (s) «ha copiato»
caso("s: «ha copiato» come certo", cm.controllo_copiato("Il PC 12 ha copiato dal PC 13."), True)
caso("s: al condizionale", cm.controllo_copiato("Sembra che abbia copiato: potrebbe essere lo stesso account, da verificare. Il PC 12 ha copiato?"), False)

# (t) «al tuo avanti»
transcript("PPP fammi il report dei voti")
caso("t: «te lo do al tuo avanti» dopo «fammi»", cm.controllo_avanti("Lo preparo e te lo do al tuo avanti.", {"transcript_path": tr}), True)
transcript("PPP pensavo a una cosa sul quiz")
caso("t: «al tuo avanti» dopo un PPP senza richiesta", cm.controllo_avanti("Annotato, al tuo avanti.", {"transcript_path": tr}), False)

# (u) rimando a riquadri precedenti
caso("u: «usa il riquadro di prima»", cm.controllo_rimando_riquadri("Incolla il testo nel riquadro di prima."), True)
caso("u: riquadro ripetuto", cm.controllo_rimando_riquadri("Incolla questo:\n```\nciao\n```"), False)

# (v) Apps Script senza file
caso("v: Apps Script, Ctrl+V senza file", cm.controllo_file_apps_script("Apri script.google.com/home, clic nel codice, Ctrl+A, Ctrl+V."), True)
caso("v: Apps Script con automazione-corso.gs", cm.controllo_file_apps_script("Apri script.google.com/home, clicca «automazione-corso.gs», Ctrl+A, Ctrl+V."), False)

# main(): blocca una volta sola, non blocca i subagenti, input rotto = exit 0
def main_con(dati):
    sys.stdin = io.StringIO(json.dumps(dati))
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        cm.main()
    return "block" in out.getvalue()


caso("main: messaggio con «onestamente» bloccato", main_con({"last_assistant_message": "Onestamente va."}), True)
caso("main: stop_hook_active non blocca di nuovo", main_con({"last_assistant_message": "Onestamente va.", "stop_hook_active": True}), False)
caso("main: subagente non controllato", main_con({"last_assistant_message": "Onestamente va.", "agent_id": "x"}), False)
r = subprocess.run([sys.executable, os.path.join(H, "controllo-messaggio.py")], input="non json", capture_output=True, text=True)
caso("main: input rotto esce 0 senza output", r.returncode == 0 and not r.stdout, True)

giusti = sum(1 for _, o, a in casi if o == a)
for n, o, a in casi:
    if o != a:
        print("SBAGLIATO:", n, "atteso", a, "ottenuto", o)
print("%d/%d" % (giusti, len(casi)))
