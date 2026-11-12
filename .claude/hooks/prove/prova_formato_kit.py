#!/usr/bin/env python3
"""Prove del controllo (ff) «formato kit e documenti» di controllo-messaggio.py (12/11/2026).

Uso: python3 /home/user/corso-informatica/.claude/hooks/prove/prova_formato_kit.py
Stampa «N/N» (casi giusti / casi totali) e le righe dei casi sbagliati.
Usa trascrizioni finte in una cartella temporanea: non tocca i repository veri né la memoria vera del controllo.
Regole provate (GUIDA-MESSAGGI 03sexies-03octies): R-A cornice blu intorno a SendUserFile, R-B un solo PDF con i kit
rossi, R-C kit in turno pulito, R-D kit Classroom (rosso in testa, TITOLO e OGGETTO in riquadri, rosso in fondo),
R-E frase vietata nell'oggetto, R-F cornice verde nei messaggi che non sono kit.
"""
import contextlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile

H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = tempfile.mkdtemp()
os.environ["CORSO_STATO_FORMATO"] = ""
spec = importlib.util.spec_from_file_location("cm", os.path.join(H, "controllo-messaggio.py"))
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)
tr = T + "/tr.jsonl"
casi = []
BLU, ROSSO, VERDE = "🟦" * 14, "🟥" * 14, "🟩" * 14
PDF = "/home/user/corso-informatica-riservato/report/x/20261112_Dispensa-1INF-Ora6_v1.2.pdf"


def caso(nome, ottenuto, atteso):
    casi.append((nome, ottenuto, atteso))


def T_(t):
    return ("T", t)


def SUF(f=PDF, forma="files"):
    return ("U", "SendUserFile", {"files": [f]} if forma == "files" else
            {"files": [{"path": f}]} if forma == "oggetti" else {"file_path": f})


def BASH():
    return ("U", "Bash", {"command": "ls"})


_n = [0]


def trascrizione(turni, extra=None):
    """turni = [(testo docente, [blocchi])]. Un blocco per riga, come nella trascrizione vera."""
    righe = []
    for docente, blocchi in turni:
        _n[0] += 1
        righe.append({"type": "user", "uuid": "u%d" % _n[0], "origin": {"kind": "human"}, "message": {"content": docente}})
        for b in blocchi:
            _n[0] += 1
            if b[0] == "T":
                righe.append({"type": "assistant", "uuid": "a%d" % _n[0], "message": {"content": [{"type": "text", "text": b[1]}]}})
            elif b[0] == "N":  # notifica automatica di un agente (non è il docente)
                righe.append({"type": "user", "uuid": "n%d" % _n[0], "origin": {"kind": "task-notification"},
                              "message": {"content": "<task-notification>fatto</task-notification>"}})
            else:
                righe.append({"type": "assistant", "uuid": "a%d" % _n[0], "message": {"content": [
                    {"type": "thinking", "thinking": "..."}]}})
                righe.append({"type": "assistant", "uuid": "b%d" % _n[0], "message": {"content": [
                    {"type": "tool_use", "id": "t%d" % _n[0], "name": b[1], "input": b[2]}]}})
                righe.append({"type": "user", "uuid": "r%d" % _n[0], "message": {"content": [
                    {"type": "tool_result", "tool_use_id": "t%d" % _n[0], "content": "ok"}]}})
    for r in (extra or []):
        righe.append(r)
    with open(tr, "w", encoding="utf-8") as f:
        for r in righe:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def codici(blocchi, docente="dammi il kit", prima=None):
    """Codici di errore del controllo sull'ultimo turno; il messaggio finale è l'ultimo blocco di testo."""
    trascrizione((prima or []) + [(docente, blocchi)])
    finale = [b[1] for b in blocchi if b[0] == "T"]
    eventi, _ = cm.eventi_ultimo_turno(tr)
    return [e[0] for e in cm.analizza_formato(eventi[:-1] if finale and eventi and eventi[-1][0] == "text" else eventi,
                                               finale[-1] if finale else "")]


# ---- testi modello (formato 03sexies)
CLASSROOM = ROSSO + "\n**TITOLO**\n```\nG Ora 6: Ripasso della classe\n```\n**OGGETTO**\n```\nBuongiorno. Seguirà il quiz.\n```\n" + BLU + "\n📄 **DISPENSA ALLIEVI ORA 6** ⬇️"
QUIZ = ROSSO + "\n**LINK DEL QUIZ** (account PIAMARTA)\n```\nhttps://docs.google.com/forms/d/x/viewform\n```\n" + BLU + "\n📄 **PDF RISPOSTE ORA 6** ⬇️"
CHIUSURA = BLU + "\n\n" + ROSSO + "\n"
LUNGO = "**Ho letto i dati.** Il quiz dell'ora 1 è stato consegnato da 17 presenti su 19.\nMancano due allievi."

# ================= casi GIUSTI
caso("giusto: kit Classroom (rosso, 🟦+📄, file, 🟦+🟥)", codici([T_(CLASSROOM), SUF(), T_(CHIUSURA)]), [])
caso("giusto: kit quiz con link in riquadro", codici([T_(QUIZ), SUF(), T_(CHIUSURA)]), [])
caso("giusto: documento fuori dai kit (🟦+📄, file, 🟦)", codici([T_("Ecco la dispensa frontale.\n" + BLU + "\n📄 DISPENSA FRONTALE ⬇️"), SUF(), T_(BLU)]), [])
caso("giusto: file con file_path invece di files", codici([T_("Ecco.\n" + BLU + "\n📄 DOC ⬇️"), SUF(forma="path"), T_(BLU)]), [])
caso("giusto: messaggio in cornice verde", codici([T_(VERDE + "\n\n" + LUNGO + "\n\n" + VERDE)]), [])
caso("giusto: immagine .png senza cornice non conta", codici([T_("Ecco lo schermo."), SUF("/tmp/x/schermo.png"), T_(VERDE + "\n" + LUNGO + "\n" + VERDE)]), [])
caso("giusto: strumenti prima di un messaggio che non è un kit", codici([BASH(), T_(VERDE + "\n" + LUNGO + "\n" + VERDE)]), [])
caso("giusto: due documenti non rossi, ognuno con la sua cornice", codici([
    T_("Primo.\n" + BLU + "\n📄 A ⬇️"), SUF("/x/a.pdf"), T_(BLU + "\nSecondo.\n" + BLU + "\n📄 B ⬇️"), SUF("/x/b.pdf"), T_(BLU)]), [])
caso("giusto: risposta breve senza cornice", codici([T_("Annotato.")]), [])
caso("giusto: risposta che comincia con 🔴", codici([T_("🔴 **Serve da te (2 cose):**\n1. Firma.\n2. Un PC rotto, il 7.")]), [])
caso("giusto: risposta di una riga lunga", codici([T_("Fatto, il quiz è nel foglio Fabbrica alla riga 12 e il PDF delle risposte è già nel riservato.")]), [])
caso("giusto: risposta con riga 🟦 in testa", codici([T_(BLU + "\n" + LUNGO)]), [])
caso("giusto: turno vecchio sporco non conta (si parte dall'ultimo messaggio del docente)", codici(
    [T_(CLASSROOM), SUF(), T_(CHIUSURA)], prima=[("prima", [BASH(), BASH(), T_(ROSSO + "\n**TITOLO** x\n**OGGETTO** y")])]), [])

# ================= R-A: documento senza cornice blu
caso("R-A: file preceduto da uno strumento e non da testo", codici([BASH(), SUF(), T_(BLU)]), ["A"])
caso("R-A: testo prima senza 🟦 e 📄", codici([T_("Ecco il PDF."), SUF(), T_(BLU)]), ["A"])
caso("R-A: manca la riga 📄 (solo 🟦)", codici([T_("Ecco.\n" + BLU), SUF(), T_(BLU)]), ["A"])
caso("R-A: testo dopo il file senza 🟦", codici([T_("Ecco.\n" + BLU + "\n📄 DOC ⬇️"), SUF(), T_(VERDE + "\n" + LUNGO + "\n" + VERDE)]), ["A"])
caso("R-A: documento .docx in forma di oggetto", codici([T_("Ecco."), SUF("/x/relazione.docx", "oggetti"), T_(BLU)]), ["A"])
caso("R-A: .xlsx e .csv e .zip contano", [codici([T_("Ecco."), SUF(f), T_(BLU)]) for f in ("/x/a.xlsx", "/x/a.csv", "/x/a.zip")], [["A"]] * 3)
caso("R-A: nessun testo dopo il file", [e[0] for e in cm.analizza_formato(
    [("text", "Ecco.\n" + BLU + "\n📄 DOC ⬇️", "a"), ("tool", "SendUserFile", {"files": [PDF]}, "t")], "")], ["A"])
caso("R-A: strumento tra file e testo dopo", codici([T_("Ecco.\n" + BLU + "\n📄 DOC ⬇️"), SUF(), BASH(), T_(BLU)]), ["A"])

# ================= R-B: due PDF con i kit
caso("R-B: due SendUserFile PDF con righe rosse", codici([
    T_(QUIZ), SUF("/x/a.pdf"), T_(BLU + "\n" + ROSSO + "\n**LINK**\n```\nhttps://x.it\n```\n" + BLU + "\n📄 PDF 2 ⬇️"), SUF("/x/b.pdf"), T_(CHIUSURA)]), ["B"])
caso("R-B: due PDF in una sola chiamata con righe rosse", [e[0] for e in cm.analizza_formato(
    [("text", QUIZ, "a"), ("tool", "SendUserFile", {"files": ["/x/a.pdf", "/x/b.pdf"]}, "t"), ("text", CHIUSURA, "b")], CHIUSURA)], ["B"])
caso("R-B: un solo PDF con i kit non scatta", codici([T_(QUIZ), SUF(), T_(CHIUSURA)]), [])

# ================= R-C: kit in turno sporco
caso("R-C: Bash prima del kit Classroom", codici([BASH(), T_(CLASSROOM), SUF(), T_(CHIUSURA)]), ["C"])
caso("R-C: Agent e Read prima del kit quiz", codici([("U", "Agent", {}), ("U", "Read", {}), T_(QUIZ), SUF(), T_(CHIUSURA)]), ["C"])
caso("R-C: una notifica non è il docente, gli strumenti prima contano ancora", codici(
    [BASH(), ("N",), T_(CLASSROOM), SUF(), T_(CHIUSURA)]), ["C"])
caso("R-C: SendUserFile di una dispensa prima del kit non rende sporco", codici(
    [T_("Dispensa.\n" + BLU + "\n📄 DOC ⬇️"), SUF("/x/doc.docx"), T_(BLU + "\n" + ROSSO + "\n**LINK**\n```\nhttps://x.it\n```"), ]), [])

# ================= R-D: kit Classroom
caso("R-D: kit senza riga rossa in testa", codici([T_(VERDE + "\n" + CLASSROOM.split("\n", 1)[1]), SUF(), T_(CHIUSURA)]), ["D1"])
caso("R-D: TITOLO e OGGETTO fuori dai riquadri", codici([T_(ROSSO + "\nTITOLO: G Ora 6: Ripasso\nOGGETTO: Seguirà il quiz.\n" + BLU + "\n📄 DOC ⬇️"), SUF(), T_(CHIUSURA)]), ["D2"])
caso("R-D: testo dopo la riga rossa finale", codici([T_(CLASSROOM), SUF(), T_(CHIUSURA + "Non provato: il quiz.")]), ["D3"])
caso("R-D: chiusura senza riga rossa", codici([T_(CLASSROOM), SUF(), T_(BLU)]), ["D3"])
caso("R-D: righe vuote dopo la riga rossa sono tollerate", codici([T_(CLASSROOM), SUF(), T_(CHIUSURA + "\n\n\n")]), [])
caso("R-D: kit senza file, un solo blocco, finale non rosso", codici([T_(ROSSO + "\n**TITOLO**\n```\nG Ora 6: x\n```\n**OGGETTO**\n```\ny\n```\nGrazie.")]), ["D3"])

# ================= R-E: frase vietata
caso("R-E: «lo facciamo quando lo dico io» nell'oggetto", codici([T_(CLASSROOM.replace("Seguirà il quiz.", "Il quiz di fine ora lo facciamo quando lo dico io.")), SUF(), T_(CHIUSURA)]), ["E"])
caso("R-E: «Seguirà il quiz.» va bene", codici([T_(CLASSROOM), SUF(), T_(CHIUSURA)]), [])

# ================= R-F: messaggio senza cornice verde
caso("R-F: messaggio lungo senza verde", codici([T_(LUNGO)]), ["F"])
caso("R-F: messaggio lungo con verde sopra e sotto", codici([T_(VERDE + "\n" + LUNGO + "\n" + VERDE)]), [])
caso("R-F: sotto i 60 caratteri", codici([T_("Ok.\nAnnotato, lo faccio.")]), [])
caso("R-F: dopo un file la risposta senza verde e senza 🟦", codici([T_("Ecco.\n" + BLU + "\n📄 DOC ⬇️"), SUF(), T_(BLU + "\n"), T_(LUNGO)]), ["F"])

# ================= il controllo non scatta dove non deve + main
def main_con(dati, env=None):
    sys.stdin = io.StringIO(json.dumps(dati))
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        cm.main()
    return out.getvalue()


trascrizione([("dammi", [T_(LUNGO)])])
caso("main: messaggio senza verde blocca e dice cosa fare", ("cornice verde" in main_con({"last_assistant_message": LUNGO, "transcript_path": tr})), True)
caso("main: subagente non controllato", "block" in main_con({"last_assistant_message": LUNGO, "transcript_path": tr, "agent_id": "x"}), False)
caso("main: stop_hook_active non blocca di nuovo", "block" in main_con({"last_assistant_message": LUNGO, "transcript_path": tr, "stop_hook_active": True}), False)
caso("main: notifica senza testo per il docente", "block" in main_con({"last_assistant_message": "", "transcript_path": tr}), False)
trascrizione([("dammi", [BASH(), T_(CLASSROOM), SUF(), T_(CHIUSURA)])])
caso("main: kit in turno sporco blocca", "turno sporco" in main_con({"last_assistant_message": CHIUSURA, "transcript_path": tr}), True)
trascrizione([("dammi", [T_(CLASSROOM), SUF(), T_(CHIUSURA)])])
caso("main: kit giusto non blocca", "block" in main_con({"last_assistant_message": CHIUSURA, "transcript_path": tr}), False)
trascrizione([("dammi", [T_("Ecco.\n" + BLU + "\n📄 DOC ⬇️"), SUF(), T_(BLU)])], extra=[
    {"type": "assistant", "isSidechain": True, "uuid": "s1", "message": {"content": [{"type": "tool_use", "id": "z", "name": "SendUserFile", "input": {"files": ["/x/y.pdf"]}}]}}])
caso("main: il lavoro dei sottoagenti (isSidechain) non conta", "block" in main_con({"last_assistant_message": BLU, "transcript_path": tr}), False)
# il messaggio finale non ancora nella trascrizione: si usa last_assistant_message
trascrizione([("dammi", [T_("Ecco.\n" + BLU + "\n📄 DOC ⬇️"), SUF()])])
caso("main: finale non ancora scritto nella trascrizione, ma giusto", "block" in main_con({"last_assistant_message": BLU, "transcript_path": tr}), False)
caso("main: finale non ancora scritto nella trascrizione, e sbagliato", "block" in main_con({"last_assistant_message": LUNGO, "transcript_path": tr}), True)
caso("main: nessuna trascrizione, messaggio giusto", "block" in main_con({"last_assistant_message": VERDE + "\n" + LUNGO + "\n" + VERDE}), False)
caso("main: trascrizione illeggibile non rompe", "block" in main_con({"last_assistant_message": "Ok.", "transcript_path": T + "/non-esiste.jsonl"}), False)

# memoria: lo stesso errore non si segnala due volte nello stesso turno, un turno nuovo sì
cm.STATO_FORMATO = T + "/stato.json"
trascrizione([("dammi", [BASH(), SUF(), T_(BLU)])])
d = {"transcript_path": tr}
caso("memoria: primo giro segnala", cm.controllo_formato(BLU, d) is not None, True)
caso("memoria: secondo giro nello stesso turno tace", cm.controllo_formato(BLU, d) is not None, False)
trascrizione([("ancora", [BASH(), SUF(), T_(BLU)])])
caso("memoria: turno nuovo segnala di nuovo", cm.controllo_formato(BLU, {"transcript_path": tr}) is not None, True)
cm.STATO_FORMATO = ""

# processo vero: legge lo stdin, scrive il JSON di blocco, esce 0
trascrizione([("dammi", [T_(LUNGO)])])
env = dict(os.environ, CORSO_STATO_FORMATO="")
r = subprocess.run([sys.executable, os.path.join(H, "controllo-messaggio.py")], capture_output=True, text=True, env=env,
                   input=json.dumps({"last_assistant_message": LUNGO, "transcript_path": tr}))
caso("processo: esce 0 e scrive decision block", r.returncode == 0 and '"decision": "block"' in r.stdout, True)

giusti = sum(1 for _, o, a in casi if o == a)
for n, o, a in casi:
    if o != a:
        print("SBAGLIATO:", n, "atteso", a, "ottenuto", o)
print("%d/%d" % (giusti, len(casi)))
