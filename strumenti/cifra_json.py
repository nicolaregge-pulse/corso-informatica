#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scrive un JSON CIFRATO per le pagine del docente (19/10/2026, privacy dei minori).
Tutto ciò che ha nomi o voti e sta in docs/ (repository pubblico) si scrive così: {"cifrato":1,"salt","iter","iv","ct"}.
AES-GCM, chiave dalla password dell'area docente con PBKDF2-SHA256 (la stessa del monitor dal vivo).
La password NON sta qui: si legge dal repository riservato (config/compito-unico-docente.json).
Il cruscotto (docs/avanzamento/index.html) decifra nel browser con il codice che il docente scrive.
Uso da Python:  from cifra_json import scrivi;  scrivi(percorso, oggetto)
"""
import base64, json, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

CONF = "/home/user/corso-informatica-riservato/config/compito-unico-docente.json"
ITER = 150000
_cache = {}


def _chiave(salt):
    pw = json.load(open(CONF, encoding="utf-8"))["password"]
    k = (pw, salt)
    if k not in _cache:
        _cache[k] = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(pw.encode("utf-8"))
    return _cache[k]


SALT = b"cruscotto-docente-v1"   # fisso: una sola derivazione per pagina nel browser


def cifra(obj):
    iv = os.urandom(12)
    ct = AESGCM(_chiave(SALT)).encrypt(iv, json.dumps(obj, ensure_ascii=False).encode("utf-8"), None)
    b = lambda x: base64.b64encode(x).decode()
    return {"cifrato": 1, "salt": b(SALT), "iter": ITER, "iv": b(iv), "ct": b(ct)}


def decifra(d):
    b = base64.b64decode
    return json.loads(AESGCM(_chiave(b(d["salt"]))).decrypt(b(d["iv"]), b(d["ct"]), None))


def leggi(percorso):
    try:
        d = json.load(open(percorso, encoding="utf-8"))
    except Exception:
        return None
    return decifra(d) if isinstance(d, dict) and d.get("cifrato") else d


def scrivi(percorso, obj):
    os.makedirs(os.path.dirname(percorso), exist_ok=True)
    json.dump(cifra(obj), open(percorso, "w", encoding="utf-8"))
