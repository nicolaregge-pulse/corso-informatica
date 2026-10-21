# -*- coding: utf-8 -*-
"""Registro del fuori compito (21/10/2026, Nicola): per classe e per allievo, quante volte non fa il lavoro assegnato,
con data, ora, che cosa faceva e la foto del giro di Veyon. Legge dal riservato dati/<classe>-veyon-<AAAAMMGG>.json
(le osservazioni: [ora, cosa, fuori]) e dati/<classe>-veyon-giri-<AAAAMMGG>.json (ora -> screenshot di Veyon).
Scrive docs/avanzamento/fuori-compito.json CIFRATO (nomi e schermate di minori), con le foto ridotte dentro.
Uso: python3 strumenti/fuori_compito.py"""
import base64, glob, io, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from cifra_json import scrivi
from PIL import Image
RIS = "/home/user/corso-informatica-riservato"
oss, foto = [], {}
for f in sorted(glob.glob(RIS + "/dati/*-veyon-2*.json")):
    m = re.match(r"(.+)-veyon-(\d{8})\.json$", os.path.basename(f))
    if not m:
        continue
    classe, g = m.group(1).upper(), m.group(2)
    data = g[:4] + "-" + g[4:6] + "-" + g[6:]
    giri = {}
    gf = RIS + "/dati/" + m.group(1) + "-veyon-giri-" + g + ".json"
    if os.path.exists(gf):
        giri = json.load(open(gf))
    for nome, lista in json.load(open(f)).get("veyon", {}).items():
        for ora, cosa, fuori in lista:
            if not fuori:
                continue
            k = data + " " + ora
            if ora in giri and k not in foto and os.path.exists(RIS + "/" + giri[ora]):
                im = Image.open(RIS + "/" + giri[ora]).convert("RGB"); im.thumbnail((1100, 1100))
                b = io.BytesIO(); im.save(b, "JPEG", quality=70); foto[k] = base64.b64encode(b.getvalue()).decode()
            oss.append({"classe": classe, "data": data, "ora": ora, "nome": nome, "cosa": cosa, "foto": k if k in foto else ""})
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "avanzamento", "fuori-compito.json")
scrivi(out, {"oss": oss, "foto": foto})
print(len(oss), "osservazioni,", len(foto), "foto")
