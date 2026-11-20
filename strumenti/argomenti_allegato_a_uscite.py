# -*- coding: utf-8 -*-
"""Uscite (xlsx e pdf) della traccia degli argomenti degli Allegati A. Vedi argomenti_allegato_a.py. Pubblico, nessun dato di allievi."""
import datetime as D
from pathlib import Path

import argomenti_allegato_a as A

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule, FormulaRule

CL = A.CLASSI
VERDE, GIALLO, ROSSO, GRIGIO, BLU = "C6EFCE", "FFEB9C", "F8CBAD", "EDEDED", "DDEBF7"
THIN = Side(style="thin", color="BBBBBB")
BORDO = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
INPUT = Font(color="0000FF")
BOLD = Font(bold=True)
FIRST, LAST = 5, 400  # righe dei dati nei fogli di classe


def intest(ws, riga, titoli, larghezze):
    for i, (t, w) in enumerate(zip(titoli, larghezze), 1):
        c = ws.cell(riga, i, t)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="305496")
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = BORDO
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[riga].height = 32


def candidate_voce(st, cl, v):
    c = [r for r in st["lezioni"] if A.vkey(cl, v) in r["voci_candidate"] and not r["voci"]]
    return c


def info_voce(st, cl, v):
    dol, titolo = A.descr_lezioni(st, v)
    if not dol:
        cands = candidate_voce(st, cl, v)
        if cands:
            titolo = "candidata, non confermata: " + " | ".join(
                f"{A.fmt_data(x['data'])} h{x['ora']} «{x['titolo_registro']}»" for x in cands[:3])
    return dol, titolo


def scrivi_xlsx(st, path, versione):
    wb = Workbook()
    # ---------------- Leggimi e fonti
    ws = wb.active
    ws.title = "Leggimi e fonti"
    ws.column_dimensions["A"].width = 150
    righe = [
        (f"Traccia degli argomenti degli Allegati A 2026/27 - v{versione}", BOLD),
        (f"Generata il {D.datetime.now().strftime('%d/%m/%Y %H:%M')} con strumenti/argomenti_allegato_a.py. File del RISERVATO (nessun nome di allievo). Il dato vero e' dati/allegato-a-traccia/stato-traccia.json.", None),
        ("", None),
        ("Che cosa e'", BOLD),
        ("Tutte le voci che Regge ha nell'Allegato A di 1INF, 2INF, 3INF, 4TI (parte «Regge» del Word del 02/11/2026), con lo stato FATTO / PARZIALE / DA FARE, la cronologia delle ore svolte, il residuo di ore e la scala del tempo dal grafico. NON e' un calendario: la colonna «Settimana/data prevista (docente)» e' vuota, la riempie il docente.", None),
        ("Numerazione: l'Allegato A non ha numeri. «n. voce» e' un numero progressivo per classe, nell'ordine del file; «Comp.» e' la competenza come scritta nell'Allegato A. Una voce che compare in piu' competenze (per esempio «Regolamento del laboratorio» in Comp. 12 e 13) e' una riga per ogni occorrenza, senza fonderle: nei conteggi del Riepilogo le righe sono occorrenze.", None),
        ("", None),
        ("Regole di stato (R7: niente indovinare)", BOLD),
        ("Gli stati sono SOLO due: FATTO e DA FARE (decisione del docente, 20/11/2026: lo stato PARZIALE non esiste piu').", None),
        ("FATTO: la voce e' FATTO nello stato dell'Allegato A (confermata dal docente o con ora firmata sul registro). Se la fonte non dice data e ora, la colonna «Da confermare» dice che l'abbinamento alla lezione e' da confermare dal docente.", None),
        ("DA FARE: nessuna lezione abbinata. Quando la nota dice «da confermare» e' scritta nella colonna «Da confermare».", None),
        ("Voce divisa: una voce parziale e' divisa in DUE RIGHE della traccia, con lo stesso numero e suffisso «a» (FATTA: parte svolta, con data, ora e titolo del registro) e «b» (DA FARE: che cosa manca). E' la stessa voce dell'Allegato A, il cui testo non cambia: nessuna voce e' aggiunta (R5.2). Nei conteggi le due righe valgono 2 righe.", None),
        ("Da chiedere al docente: quando non e' provato quale parte e' stata svolta la voce NON e' divisa, resta DA FARE e va nel foglio «Da chiedere al docente» con una domanda breve (R7.6).", None),
        ("Materia: presa dalla lezione del registro DIDAweb abbinata; per le voci numerate di Sicurezza (Comp. 14) e' Sicurezza professionale; per 3INF e 4TI e' l'unica materia dell'incarico (Laboratorio professionale); in tutti gli altri casi «da assegnare (docente)». Non e' mai indovinata.", None),
        ("Sicurezza: il titolo sul registro lo mette la direzione e fa fede il registro (R5.2bis, doppia modalita' Dichiarato/Registro): il titolo di una lezione puo' non coincidere con il numero dell'ora dell'Allegato A. Qui lo stato Dichiarato resta quello gia' confermato; i titoli del registro sono in «Cronologia».", None),
        ("Ore fatte: una riga di Argomenti del registro = un'ora (anche con argomento vuoto). Fonte: DIDAweb letto il 19/11/2026 ore 10:22-10:25 (239 ore, come la stima del grafico). Le ore dopo il 19/11 entrano solo con il comando «segna».", None),
        ("Ore previste: dall'incarico (dati/docente/ORE-DOCENZA-2026-27-v1.0.md), non provate sul contratto. 1INF Impresa simulata (lab): «150 + 48» come nel PDF, qui sommato 198 (la somma 343 della 1INF lo conta); il significato del 48 e' da confermare dal docente.", None),
        ("4TI: nell'incarico c'e' solo Laboratorio professionale. «Informatica» non compare negli Allegati A di Regge per la 4TI (ALLEGATO-A-4TI-VOCI-INFORMATICA-DI-BASE-v1.1.md: nessuna voce con quel titolo nel Word): non provato che esista una materia Informatica per la 4TI.", None),
        ("Allegato A: dopo il 30/10 si puo' solo TOGLIERE, mai aggiungere (R5.2). Questo file non aggiunge voci: le «candidate» sono solo suggerimenti di abbinamento tra una lezione del registro e una voce gia' esistente, da confermare dal docente.", None),
        ("", None),
        ("Fonti (file e versione)", BOLD),
    ]
    for k, v in st["fonti"].items():
        righe.append((f"{k}: {v}", None))
    righe += [("", None), ("Fogli", BOLD),
              ("Riepilogo (formule su fogli di classe e Cronologia) | 1INF, 2INF, 3INF, 4TI (tutte le voci) | Cronologia (tutte le ore svolte) | Svolto fuori Allegato A (ore senza voce abbinata) | Scala del tempo (periodi, ore a settimana, vacanze e stage)", None),
              ("", None), ("Registro delle versioni", BOLD)]
    for e in st["eventi"]:
        t = {"inizializza": "creato dalle fonti", "rigenera": "rigenerato", "segna": f"segnato: {e.get('classe','')} {e.get('materia','')} n.{e.get('n_voce','')} «{e.get('voce','')}» {A.fmt_data(e['data']) if e.get('data') else ''} h{e.get('ora','')} {e.get('durata','')} h"}.get(e["tipo"], e["tipo"])
        righe.append((f"{e['ts'].replace('T', ' ')}  {t}", None))
    for i, (t, f) in enumerate(righe, 1):
        c = ws.cell(i, 1, t)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if f:
            c.font = f

    # ---------------- fogli di classe
    for cl in CL:
        w = wb.create_sheet(cl)
        w.cell(1, 1, f"{A.NOME_CLASSE[cl]}: tutte le voci dell'Allegato A (parte Regge) - v{versione}").font = Font(bold=True, size=13)
        w.cell(2, 1, "Stato: FATTO / PARZIALE / DA FARE. «Da confermare» = abbinamento o dato dubbio: lo conferma il docente. Ultima colonna: la riempie il docente (nessun calendario proposto).")
        intest(w, 4, ["n. voce", "Comp.", "Modulo (Allegato A)", "Voce / argomento (testo dell'Allegato A)", "Materia", "Stato", "Data / ora / durata",
                      "Titolo del registro DIDAweb", "Fonte", "Da confermare / da chiedere", "Settimana/data prevista (docente)", "Parte (voce divisa)"],
               [7, 7, 34, 52, 24, 11, 34, 44, 42, 46, 22, 40])
        for i, v in enumerate(st["classi"][cl]):
            r = FIRST + i
            dol, titolo = info_voce(st, cl, v)
            fonte = v["fonte"] or ("svolto-2026-27.json / stato-allegato-a.json" if v["stato"] == "FATTO" else "nessuna lezione abbinata (stato-allegato-a.json)")
            if v["materia_fonte"]:
                fonte += f" | materia: {v['materia_fonte']}"
            dc = v["da_confermare_nota"] if v["da_confermare"] else ""
            if v["da_confermare"] and v["stato"] != "FATTO" and not v.get("da_chiedere"):
                dc = dc.replace("da confermare: ", "", 1) if dc.startswith("da confermare: ") else dc
                dc = "da confermare dal docente: " + dc if dc else "da confermare dal docente"
            parte = ""
            if v.get("parte") == "a":
                parte = f"a: FATTA, parte svolta: {v['parte_testo']}"
            elif v.get("parte") == "b":
                parte = f"b: DA FARE, manca: {v['manca']}"
            vals = [A.etichetta(v) if v.get("parte") else v["n"], int(v["comp"]), v["modulo"], v["testo"], v["materia"], v["stato"], dol, titolo, fonte, dc, "", parte]
            for j, x in enumerate(vals, 1):
                c = w.cell(r, j, x)
                c.alignment = Alignment(wrap_text=True, vertical="top")
                c.border = BORDO
            w.cell(r, 11).font = INPUT
        n = len(st["classi"][cl])
        rng = f"F{FIRST}:F{FIRST+n-1}"
        w.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"FATTO"'], fill=PatternFill("solid", bgColor=VERDE, fgColor=VERDE)))
        w.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"DA FARE"'], fill=PatternFill("solid", bgColor=ROSSO, fgColor=ROSSO)))
        w.freeze_panes = "E5"
        w.auto_filter.ref = f"A4:L{FIRST+n-1}"

    # ---------------- Da chiedere al docente
    wq = wb.create_sheet("Da chiedere al docente")
    wq.cell(1, 1, f"Da chiedere al docente: voci dove non e' provato che cosa e' stato fatto - v{versione}").font = Font(bold=True, size=13)
    wq.cell(2, 1, "Restano DA FARE finche' il docente risponde (R7.6: niente indovinare). Dopo la risposta: comando «segna» (con --parte se e' fatta solo una parte).")
    intest(wq, 4, ["Classe", "n. voce", "Comp.", "Voce (testo dell'Allegato A)", "Domanda breve", "Lezioni del registro vicine (DIDAweb)", "Risposta del docente"], [8, 8, 7, 50, 70, 60, 30])
    qr = FIRST
    for cl in CL:
        for v in st["classi"][cl]:
            if not v.get("da_chiedere"):
                continue
            dol, tit = info_voce(st, cl, v)
            vals = [cl, v["n"], int(v["comp"]), v["testo"], v["da_chiedere"], (dol + " | " + tit).strip(" |"), ""]
            for j, x in enumerate(vals, 1):
                c = wq.cell(qr, j, x)
                c.alignment = Alignment(wrap_text=True, vertical="top")
                c.border = BORDO
            wq.cell(qr, 7).font = INPUT
            qr += 1
    wq.freeze_panes = "A5"

    # ---------------- Cronologia
    wc = wb.create_sheet("Cronologia")
    wc.cell(1, 1, f"Cronologia: tutte le ore svolte, in ordine di data (DIDAweb letto il 19/11/2026 e ore segnate dopo) - v{versione}").font = Font(bold=True, size=13)
    wc.cell(2, 1, "Una riga = un'ora del registro. «Voce abbinata»: dallo stato dell'Allegato A. «Candidata»: suggerimento non confermato.")
    intest(wc, 4, ["Classe", "Materia", "Data", "Ora (h)", "Durata (h)", "Titolo del registro DIDAweb", "Voce abbinata (n. e testo)", "Abbinamento", "Fonte"],
           [8, 26, 12, 8, 10, 56, 64, 26, 38])
    cr = FIRST
    for r in st["lezioni"]:
        cl = r["classe"]
        def nome(ids):
            out = []
            for k in ids:
                v = A.trova_voce(st, k)
                out.append(f"n.{A.etichetta(v)} (Comp. {v['comp']}) {v['testo']}" + (f" [{v['parte_testo']}]" if v.get("parte") else ""))
            return "; ".join(out)
        if r["voci"]:
            ab, tipo = nome(r["voci"]), "abbinata"
        elif r["voci_dubbie"]:
            ab, tipo = nome(r["voci_dubbie"]), "da confermare dal docente"
        elif r["voci_candidate"]:
            ab, tipo = nome(r["voci_candidate"][:2]), "candidata, non confermata"
        else:
            ab, tipo = "", "nessuna voce (vedi Svolto fuori Allegato A)"
        vals = [cl, r["materia"], D.date.fromisoformat(r["data"]), r["ora"], r["durata"], r["titolo_registro"], ab, tipo, r["fonte"]]
        for j, x in enumerate(vals, 1):
            c = wc.cell(cr, j, x)
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = BORDO
        wc.cell(cr, 3).number_format = "DD/MM/YYYY"
        cr += 1
    CR_LAST = cr - 1
    wc.freeze_panes = "A5"
    wc.auto_filter.ref = f"A4:I{CR_LAST}"

    # ---------------- Svolto fuori Allegato A
    wf = wb.create_sheet("Svolto fuori Allegato A")
    wf.cell(1, 1, f"Svolto fuori Allegato A: ore del registro senza voce abbinata - v{versione}").font = Font(bold=True, size=13)
    wf.cell(2, 1, "Non e' provato che siano davvero fuori dall'Allegato A: sono ore per cui nessun abbinamento e' registrato. Il docente conferma (R7.6). Le candidate sono suggerimenti.")
    intest(wf, 4, ["Classe", "Materia", "Data", "Ora (h)", "Durata (h)", "Titolo del registro DIDAweb", "Voce candidata (da confermare dal docente)", "Nota"],
           [8, 26, 12, 8, 10, 56, 64, 50])
    fr = FIRST
    for r in st["lezioni"]:
        if r["voci"] or r["voci_dubbie"]:
            continue
        cands = []
        for k in r["voci_candidate"][:2]:
            v = A.trova_voce(st, k)
            cands.append(f"n.{A.etichetta(v)} (Comp. {v['comp']}) {v['testo']}")
        nota = "nessun abbinamento registrato"
        if r["materia"] == "Sicurezza professionale":
            nota = "Sicurezza: il titolo lo mette la direzione, fa fede il registro (R5.2bis); abbinamento all'ora dell'Allegato A da confermare dal docente"
        if r["titolo_registro"].startswith("(vuoto"):
            nota = "argomento vuoto sul registro: lo mette la direzione, non si scrive"
        vals = [r["classe"], r["materia"], D.date.fromisoformat(r["data"]), r["ora"], r["durata"], r["titolo_registro"], "; ".join(cands), nota]
        for j, x in enumerate(vals, 1):
            c = wf.cell(fr, j, x)
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = BORDO
        wf.cell(fr, 3).number_format = "DD/MM/YYYY"
        fr += 1
    wf.freeze_panes = "A5"
    wf.auto_filter.ref = f"A4:H{max(fr-1, 5)}"

    # ---------------- Scala del tempo
    wt = wb.create_sheet("Scala del tempo")
    wt.cell(1, 1, "Scala del tempo dal grafico «ORE DI DOCENZA 2026/27 - ore fatte e previsioni a settimana» (19/11/2026)").font = Font(bold=True, size=13)
    wt.cell(2, 1, "Ipotesi modificabile del docente (celle blu = dati del grafico). Le settimane effettive e le ore disponibili sono MIO calcolo (giorni feriali senza i festivi / 5 x ore a settimana), non provato contro il grafico. Nessun calendario proposto.")
    intest(wt, 4, ["Periodo", "Dal", "Al", "Giorni feriali (senza festivi)", "Settimane effettive", "1INFspe ore/sett.", "2INFspe ore/sett.", "3INFspe ore/sett.", "4TI ore/sett.", "Totale ore/sett.", "Ore disponibili 1INF", "Ore disponibili 2INF", "Ore disponibili 3INF", "Ore disponibili 4TI", "Totale ore disponibili", "Note"],
           [26, 12, 12, 14, 12, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 60])
    # elenco festivi (una data per riga) a destra
    wt.cell(4, 18, "Giorni festivi / ferie (feriali)").font = BOLD
    wt.column_dimensions["R"].width = 16
    wt.column_dimensions["S"].width = 34
    hol = []
    for f in st["festivi"]:
        d = D.date.fromisoformat(f["dal"])
        while d <= D.date.fromisoformat(f["al"]):
            if d.weekday() < 5:
                hol.append((d, f["nome"]))
            d += D.timedelta(1)
    for i, (d, n) in enumerate(hol):
        wt.cell(5 + i, 18, d).number_format = "DD/MM/YYYY"
        wt.cell(5 + i, 19, n)
    H0, H1 = 5, 4 + len(hol)
    for i, p in enumerate(st["periodi"]):
        r = 5 + i
        wt.cell(r, 1, p["nome"])
        wt.cell(r, 2, D.date.fromisoformat(p["dal"])).number_format = "DD/MM/YYYY"
        wt.cell(r, 3, D.date.fromisoformat(p["al"])).number_format = "DD/MM/YYYY"
        wt.cell(r, 4, f"=NETWORKDAYS(B{r},C{r},$R${H0}:$R${H1})")
        wt.cell(r, 5, f"=D{r}/5").number_format = "0.0"
        for j, cl in enumerate(CL):
            c = wt.cell(r, 6 + j, p["ore_sett"][cl])
            c.font = INPUT
            wt.cell(r, 11 + j, f"=E{r}*{get_column_letter(6+j)}{r}").number_format = "0.0"
        wt.cell(r, 10, f"=SUM(F{r}:I{r})").number_format = "0.0"
        wt.cell(r, 15, f"=SUM(K{r}:N{r})").number_format = "0.0"
        wt.cell(r, 16, p["nota"])
    rt = 5 + len(st["periodi"])
    wt.cell(rt, 1, "Totale da qui al 04/06/2027").font = BOLD
    for col in [4, 5] + list(range(11, 16)):
        L = get_column_letter(col)
        wt.cell(rt, col, f"=SUM({L}5:{L}{rt-1})").number_format = "0.0"
        wt.cell(rt, col).font = BOLD
    wt.cell(rt + 2, 1, "Dal grafico").font = BOLD
    dati = [("Totale incarico (ore)", A.TOTALE_INCARICO), ("Ore fatte al 19/11/2026 (stima del grafico)", A.ORE_FATTE_GRAFICO),
            ("Ore residue secondo il grafico (totale - fatte)", f"=B{rt+3}-B{rt+4}"),
            ("Ore fatte finora, per settimana (stima del grafico)", A.ORE_FATTE_SETT),
            ("Ore a settimana previste (costanti: le classi presenti assorbono le ore di chi e' in stage)", A.ORE_SETT_TOTALE),
            ("Scarto tra ore residue del grafico e ore disponibili calcolate qui (non provato: il grafico usa le sue settimane)", f"=B{rt+5}-O{rt}")]
    for i, (k, v) in enumerate(dati):
        wt.cell(rt + 3 + i, 1, k).alignment = Alignment(wrap_text=True)
        c = wt.cell(rt + 3 + i, 2, v)
        if not isinstance(v, str):
            c.font = INPUT
        c.number_format = "0.0"
    wt.column_dimensions["A"].width = 60
    r0 = rt + 3 + len(dati) + 1
    wt.cell(r0, 1, "Vacanze, festivi e stage (ipotesi del grafico)").font = BOLD
    stage = ["Ferie di Natale 24/12/2026 - 06/01/2027", "Pasqua 25/03 - 29/03/2027", "Festivi 7-8/12/2026 e 2/06/2027",
             "3INFspe in stage dal 23/11/2026 al 18/02/2027, rientra il 19/02/2027", "2INFspe in stage dal 19/02/2027 al 21/05/2027 (finisce 2 settimane prima della fine)"]
    for i, t in enumerate(stage):
        wt.cell(r0 + 1 + i, 1, t)
    wt.freeze_panes = "A5"
    SC_TOT = rt  # riga dei totali
    SC_ROWS = {cl: get_column_letter(11 + j) for j, cl in enumerate(CL)}

    # ---------------- Riepilogo (formule)
    wr = wb.create_sheet("Riepilogo", 1)
    wr.cell(1, 1, f"Riepilogo per classe e materia - v{versione}").font = Font(bold=True, size=13)
    wr.cell(2, 1, "Formule su fogli di classe (righe di voci) e Cronologia (ore). Una voce divisa a/b vale 2 righe. «da assegnare»: materia non provata (decide il docente). Ore previste: incarico (blu).")
    intest(wr, 4, ["Classe", "Materia", "Righe di voci", "Fatte", "Da fare", "Ore previste", "Ore fatte", "Ore residue", "% ore fatte", "Note"],
           [10, 30, 12, 9, 10, 12, 10, 12, 10, 70])
    r = 5
    righe_cl = {}
    CRN = CR_LAST + 300
    for cl in CL:
        first = r
        for mat in A.MATERIE[cl] + [A.DA_ASSEGNARE]:
            rngE = f"'{cl}'!$E${FIRST}:$E${LAST}"
            rngF = f"'{cl}'!$F${FIRST}:$F${LAST}"
            wr.cell(r, 1, cl)
            wr.cell(r, 2, mat)
            wr.cell(r, 3, f'=COUNTIFS({rngE},$B{r})')
            wr.cell(r, 4, f'=COUNTIFS({rngE},$B{r},{rngF},"FATTO")')
            wr.cell(r, 5, f'=COUNTIFS({rngE},$B{r},{rngF},"DA FARE")')
            if mat != A.DA_ASSEGNARE:
                prev, nota = A.ORE_PREVISTE[(cl, mat)]
                wr.cell(r, 6, prev).font = INPUT
                wr.cell(r, 7, f"=SUMIFS(Cronologia!$E$5:$E${CRN},Cronologia!$A$5:$A${CRN},$A{r},Cronologia!$B$5:$B${CRN},$B{r})")
                wr.cell(r, 8, f"=F{r}-G{r}")
                wr.cell(r, 9, f"=IF(F{r}>0,G{r}/F{r},0)").number_format = "0.0%"
                wr.cell(r, 10, nota)
            else:
                wr.cell(r, 10, "voci senza materia provata: il docente le assegna alla materia (nessun dato di ore)")
            r += 1
        wr.cell(r, 1, cl).font = BOLD
        wr.cell(r, 2, f"Totale {A.NOME_CLASSE[cl]}").font = BOLD
        for col in range(3, 9):
            L = get_column_letter(col)
            wr.cell(r, col, f"=SUM({L}{first}:{L}{r-1})").font = BOLD
        wr.cell(r, 9, f"=IF(F{r}>0,G{r}/F{r},0)").number_format = "0.0%"
        for col in range(1, 11):
            wr.cell(r, col).fill = PatternFill("solid", fgColor=BLU)
        righe_cl[cl] = r
        r += 2
    wr.cell(r, 2, "TOTALE (4 classi)").font = BOLD
    for col in range(3, 9):
        L = get_column_letter(col)
        wr.cell(r, col, "=" + "+".join(f"{L}{righe_cl[c]}" for c in CL)).font = BOLD
    wr.cell(r, 9, f"=IF(F{r}>0,G{r}/F{r},0)").number_format = "0.0%"
    wr.cell(r, 10, f"Incarico 784 h; ore fatte secondo il grafico {A.ORE_FATTE_GRAFICO} h (al 19/11): deve coincidere con «Ore fatte» finche' non si segnano ore nuove.")
    r += 3
    wr.cell(r, 1, "Residuo di ore rispetto alle ore disponibili nel grafico (per classe; il grafico da' le ore per classe, non per materia)").font = Font(bold=True, size=12)
    r += 1
    intest_r = r
    for i, t in enumerate(["Classe", "", "Ore previste (incarico)", "Ore fatte", "Ore residue", "Disponibili 23/11-18/02", "Disponibili 19/02-21/05", "Disponibili 24/05-04/06", "Totale disponibili", "Disponibili - residue (negativo = piu' ore previste che disponibili; ipotesi, non provato)"], 1):
        c = wr.cell(r, i, t)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="305496")
        c.alignment = Alignment(wrap_text=True)
    wr.row_dimensions[r].height = 44
    for j, cl in enumerate(CL):
        r += 1
        rc = righe_cl[cl]
        L = SC_ROWS[cl]
        wr.cell(r, 1, cl)
        wr.cell(r, 3, f"=F{rc}")
        wr.cell(r, 4, f"=G{rc}")
        wr.cell(r, 5, f"=C{r}-D{r}")
        for k in range(3):
            wr.cell(r, 6 + k, f"='Scala del tempo'!{L}{5+k}").number_format = "0.0"
        wr.cell(r, 9, f"=SUM(F{r}:H{r})").number_format = "0.0"
        wr.cell(r, 10, f"=I{r}-E{r}").number_format = "0.0"
    wr.freeze_panes = "A5"
    for rr in wr.iter_rows(min_row=5, max_row=r):
        for c in rr:
            if c.row != intest_r:
                c.alignment = Alignment(wrap_text=True, vertical="top")
    for rr in range(5, r + 1):
        for col in (7, 8):
            wr.cell(rr, col).number_format = "0.0"
    wb.save(path)


# ------------------------------------------------------------------ PDF
def scrivi_pdf(st, path, versione):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak, KeepTogether

    pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
    sN = ParagraphStyle("n", fontName="DV", fontSize=7.4, leading=9)
    sB = ParagraphStyle("b", parent=sN, fontName="DVB")
    sH = ParagraphStyle("h", fontName="DVB", fontSize=14, leading=17, spaceAfter=3)
    sH2 = ParagraphStyle("h2", fontName="DVB", fontSize=10.5, leading=13, spaceBefore=6, spaceAfter=2)
    sS = ParagraphStyle("s", parent=sN, fontSize=7.6, leading=9.6)
    sW = ParagraphStyle("w", parent=sB, textColor=colors.white)

    doc = SimpleDocTemplate(str(path), pagesize=landscape(A4), leftMargin=10 * mm, rightMargin=10 * mm, topMargin=10 * mm, bottomMargin=11 * mm,
                            title=f"Traccia argomenti Allegati A 2026/27 v{versione}", author="Claude Code per il docente")

    def foot(c, d):
        c.setFont("DV", 7)
        c.drawString(10 * mm, 6 * mm, f"Traccia argomenti Allegati A 2026/27 v{versione} - RISERVATO (nessun nome di allievo) - generata {D.datetime.now().strftime('%d/%m/%Y %H:%M')}")
        c.drawRightString(287 * mm, 6 * mm, f"pag. {d.page}")

    el = []
    ore_prev = {(c, m): o for (c, m), (o, _) in A.ORE_PREVISTE.items()}

    # ---- pagina 1: riepilogo
    el.append(Paragraph(f"Argomenti degli Allegati A 2026/27: riepilogo (v{versione})", sH))
    el.append(Paragraph(f"Righe = occorrenze nell'Allegato A (parte Regge); una voce divisa a/b vale 2 righe. Stati: FATTO e DA FARE. Ore fatte dal registro DIDAweb letto il 19/11/2026 e dalle ore segnate dopo. Ore previste dall'incarico (784 h, non provate sul contratto). "
                        f"«da assegnare»: materia non provata, la assegna il docente. Nessun calendario proposto: la scala del tempo e' dal grafico del 19/11.", sS))
    el.append(Spacer(1, 3))
    head = [Paragraph(t, sW) for t in ["Classe", "Materia", "Righe", "Fatte", "Da fare", "Ore prev.", "Ore fatte", "Ore resid.", "%"]]
    data = [head]
    stl = [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#305496")), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
           ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]
    tot = [0] * 6
    for cl in CL:
        ct = [0] * 6
        for mat in A.MATERIE[cl] + [A.DA_ASSEGNARE]:
            vs = [v for v in st["classi"][cl] if v["materia"] == mat]
            n, f, d = len(vs), sum(v["stato"] == "FATTO" for v in vs), sum(v["stato"] == "DA FARE" for v in vs)
            if mat != A.DA_ASSEGNARE:
                pr, fa = ore_prev[(cl, mat)], A.ore_fatte(st, cl, mat)
                row = [cl, mat, n, f, d, f"{pr:g}", f"{fa:g}", f"{pr-fa:g}", f"{fa/pr*100:.0f}%"]
                add = [n, f, d, pr, fa, pr - fa]
            else:
                row = [cl, "voci con materia " + mat, n, f, d, "", "", "", ""]
                add = [n, f, d, 0, 0, 0]
            ct = [x + y for x, y in zip(ct, add)]
            data.append([Paragraph(str(x), sN) for x in row])
        data.append([Paragraph(x, sB) for x in [cl, f"Totale {A.NOME_CLASSE[cl]}", str(ct[0]), str(ct[1]), str(ct[2]), f"{ct[3]:g}", f"{ct[4]:g}", f"{ct[5]:g}", f"{ct[4]/ct[3]*100:.0f}%"]])
        stl.append(("BACKGROUND", (0, len(data) - 1), (-1, len(data) - 1), colors.HexColor("#DDEBF7")))
        tot = [x + y for x, y in zip(tot, ct)]
    data.append([Paragraph(x, sB) for x in ["", "TOTALE", str(tot[0]), str(tot[1]), str(tot[2]), f"{tot[3]:g}", f"{tot[4]:g}", f"{tot[5]:g}", f"{tot[4]/tot[3]*100:.0f}%"]])
    cw = [18, 125, 17, 17, 17, 22, 22, 22, 17]
    t = Table(data, colWidths=[x * mm for x in cw], repeatRows=1)
    t.setStyle(TableStyle(stl))
    el.append(t)
    el.append(Spacer(1, 4))
    # scala del tempo
    el.append(Paragraph("Ore disponibili dal grafico (ore a settimana x settimane effettive, mio calcolo, non provato)", sH2))
    hol = []
    for f in st["festivi"]:
        d0 = D.date.fromisoformat(f["dal"]);
        while d0 <= D.date.fromisoformat(f["al"]):
            hol.append(d0); d0 += D.timedelta(1)
    hd = [Paragraph(t_, sW) for t_ in ["Periodo", "Sett. effettive", "1INF", "2INF", "3INF", "4TI", "Tot. disponibili", "Note"]]
    sd = [hd]
    tl = [0] * 5
    for p in st["periodi"]:
        gg = A.giorni_lavorativi(p["dal"], p["al"], st["festivi"])
        w = gg / 5
        disp = [w * p["ore_sett"][c] for c in CL]
        tl = [a + b for a, b in zip(tl, disp + [sum(disp)])]
        sd.append([Paragraph(x, sN) for x in [p["nome"], f"{w:.1f}"] + [f"{x:.0f} ({p['ore_sett'][c]:g}/sett.)" for x, c in zip(disp, CL)] + [f"{sum(disp):.0f}", p["nota"]]])
    sd.append([Paragraph(x, sB) for x in ["Totale", ""] + [f"{x:.0f}" for x in tl]] + [Paragraph("", sN)])
    t2 = Table(sd, colWidths=[x * mm for x in [40, 18, 30, 30, 30, 30, 22, 77]], repeatRows=1)
    t2.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#305496")), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]))
    el.append(t2)
    el.append(Paragraph(f"Grafico: incarico {A.TOTALE_INCARICO} h, fatte al 19/11 {A.ORE_FATTE_GRAFICO} h, residue {A.TOTALE_INCARICO - A.ORE_FATTE_GRAFICO} h; ferie Natale 24/12-06/01, Pasqua 25-29/03/2027, festivi 7-8/12 e 2/06; "
                        f"3INFspe in stage 23/11-18/02; 2INFspe in stage 19/02-21/05. Ipotesi modificabile del docente.", sS))

    # ---- liste Da fare per classe e materia
    for cl in CL:
        el.append(PageBreak())
        el.append(Paragraph(f"{A.NOME_CLASSE[cl]}: voci da fare (e parziali)", sH))
        el.append(Paragraph("Colonna «Settimana/data prevista» lasciata vuota: la riempie il docente. «?» = da confermare dal docente. n. = numero della voce per il comando «segna» (29b = parte da fare di una voce divisa).", sS))
        for mat in A.MATERIE[cl] + [A.DA_ASSEGNARE]:
            vs = [v for v in st["classi"][cl] if v["materia"] == mat and v["stato"] != "FATTO"]
            allv = [v for v in st["classi"][cl] if v["materia"] == mat]
            titolo = mat if mat != A.DA_ASSEGNARE else "Materia da assegnare (docente): voci senza lezione abbinata"
            if mat != A.DA_ASSEGNARE:
                pr, fa = ore_prev[(cl, mat)], A.ore_fatte(st, cl, mat)
                titolo += f" - {len(vs)} righe da fare su {len(allv)}; ore: previste {pr:g}, fatte {fa:g}, residue {pr-fa:g}"
            else:
                titolo += f" - {len(vs)} voci"
            blocco = [Paragraph(titolo, sH2)]
            if not vs:
                blocco.append(Paragraph("Nessuna voce da fare.", sN))
                el.append(KeepTogether(blocco))
                continue
            rows = [[Paragraph(x, sW) for x in ["n.", "Comp.", "Voce / argomento", "Stato", "Nota / da confermare", "Settimana/data prevista (docente)"]]]
            for v in vs:
                nota = v["da_confermare_nota"] if v["da_confermare"] else v["nota"]
                rows.append([Paragraph(A.etichetta(v), sN), Paragraph(v["comp"], sN), Paragraph(v["testo"], sN), Paragraph(v["stato"] + (" ?" if v["da_confermare"] else ""), sN),
                             Paragraph(nota or "", sN), Paragraph("", sN)])
            tb = Table(rows, colWidths=[x * mm for x in [10, 13, 104, 20, 86, 44]], repeatRows=1)
            ts = [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#305496")), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                  ("TOPPADDING", (0, 0), (-1, -1), 1.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2)]
            for i, v in enumerate(vs, 1):
                if v.get("da_chiedere"):
                    ts.append(("BACKGROUND", (3, i), (3, i), colors.HexColor("#FFEB9C")))
            tb.setStyle(TableStyle(ts))
            blocco.append(tb)
            el.append(KeepTogether(blocco[:2]))
            el.extend(blocco[2:])
    el.append(PageBreak())
    el.append(Paragraph("Da chiedere al docente: voci dove non e' provato che cosa e' stato fatto", sH))
    el.append(Paragraph("Restano DA FARE finche' il docente risponde (R7.6). Una domanda per gruppo di voci.", sS))
    rows = [[Paragraph(x, sW) for x in ["Classe", "n.", "Comp.", "Voce", "Domanda breve"]]]
    for cl in CL:
        for v in st["classi"][cl]:
            if v.get("da_chiedere"):
                rows.append([Paragraph(cl, sN), Paragraph(str(v["n"]), sN), Paragraph(v["comp"], sN), Paragraph(v["testo"], sN), Paragraph(v["da_chiedere"], sN)])
    if len(rows) > 1:
        tq = Table(rows, colWidths=[x * mm for x in [14, 10, 12, 70, 171]], repeatRows=1)
        tq.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#305496")), ("GRID", (0, 0), (-1, -1), 0.3, colors.grey), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5)]))
        el.append(tq)
    else:
        el.append(Paragraph("Nessuna domanda aperta.", sN))
    doc.build(el, onFirstPage=foot, onLaterPages=foot)


def scrivi_pdf_competenza(st, path, versione):
    """PDF per competenza: tutte le voci di ogni classe, raggruppate per Competenza, con stato (FATTO / DA FARE)."""
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
    n = ParagraphStyle("n", fontName="DV", fontSize=7.8, leading=9.6)
    h1 = ParagraphStyle("h1", fontName="DVB", fontSize=15, leading=18, spaceAfter=4)
    h2 = ParagraphStyle("h2", fontName="DVB", fontSize=12, leading=15, spaceAfter=3)
    h3 = ParagraphStyle("h3", fontName="DVB", fontSize=9.5, leading=12, spaceBefore=6, spaceAfter=2)
    col = {"FATTO": colors.HexColor("#c6efce"), "DA FARE": colors.HexColor("#ffc7ce")}
    el = [Paragraph("Allegato A 2026-27: voci per classe e competenza (parte del docente)", h1),
          Paragraph(f"Versione {versione} - {D.date.today().strftime('%d/%m/%Y')}. RISERVATO (nessun nome di allievo). Fonte: ARGOMENTI-ALLEGATO-A-TRACCIA-2026-27-v{versione} (DIDAweb letto il 19/11/2026 e ore segnate dopo). "
                    "Verde = fatto, rosso = da fare (stati solo due). Una voce divisa (n. con «a» e «b») e' la stessa voce dell'Allegato A: «a» e' la parte svolta, «b» quella che manca. Le voci sono per occorrenza; nessuna voce aggiunta.", n)]

    def key(x):
        try:
            return float(x)
        except ValueError:
            return 99
    for cl in CL:
        rows = st["classi"][cl]
        comps = sorted({v["comp"] for v in rows}, key=key)
        el += [PageBreak(), Paragraph(f"{cl}: {len(rows)} righe", h2)]
        for c in comps:
            rs = [v for v in rows if v["comp"] == c]
            f = sum(v["stato"] == "FATTO" for v in rs)
            el.append(Paragraph(f"Competenza {c}: {len(rs)} righe - fatte {f}, da fare {len(rs) - f}", h3))
            data = [["n.", "Modulo", "Voce", "Stato", "Data / ora / durata, parte, domanda"]]
            for v in rs:
                dol, _ = A.descr_lezioni(st, v)
                extra = []
                if dol:
                    extra.append(dol)
                if v.get("parte") == "a":
                    extra.append("parte svolta: " + v["parte_testo"])
                if v.get("parte") == "b":
                    extra.append("manca: " + v["manca"])
                if v.get("da_chiedere"):
                    extra.append("DA CHIEDERE: " + v["da_chiedere"])
                data.append([A.etichetta(v), Paragraph(v["modulo"] or "", n), Paragraph(v["testo"], n), v["stato"], Paragraph("<br/>".join(extra), n)])
            t = Table(data, colWidths=[24, 200, 245, 52, 290], repeatRows=1)
            ts = [("GRID", (0, 0), (-1, -1), .3, colors.grey), ("FONTNAME", (0, 0), (-1, -1), "DV"), ("FONTSIZE", (0, 0), (-1, -1), 7.8),
                  ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey), ("VALIGN", (0, 0), (-1, -1), "TOP")]
            for i, v in enumerate(rs, 1):
                ts.append(("BACKGROUND", (3, i), (3, i), col.get(v["stato"], colors.white)))
            t.setStyle(TableStyle(ts))
            el += [t, Spacer(1, 4)]
    SimpleDocTemplate(str(path), pagesize=landscape(A4), leftMargin=20, rightMargin=20, topMargin=20, bottomMargin=20,
                      title=f"Allegato A per competenza v{versione}").build(el)
