"""Prepara la faccia di un personaggio per il Treno su Godot.

Uso: python3 strumenti/testa_personaggio.py ORIGINALE.png USCITA.png [x1,y1,x2,y2]
(il riquadro della testa si può dare a mano, misurato sull'originale con una griglia)
1. trova la faccia (OpenCV; per i disegni anime usa il riconoscitore "anime" se c'è, altrimenti il centro alto);
2. ritaglia un quadrato centrato sulla faccia, con un po' di margine per capelli e mento;
3. ridimensiona a 256 x 294 e taglia la forma: testa ovale + collo; fuori è trasparente.
"""
import sys, os
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFilter

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
g = cv2.cvtColor(np.array(im.convert("RGB")), cv2.COLOR_RGB2GRAY)
facce = []
riq = [int(v) for v in sys.argv[3].split(",")] if len(sys.argv) > 3 else None
for nome in ([] if riq or not hasattr(cv2, "CascadeClassifier") else ["haarcascade_frontalface_default.xml", "haarcascade_frontalface_alt2.xml", "haarcascade_profileface.xml"]):
    c = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades, nome))
    facce = list(c.detectMultiScale(g, 1.05, 3, minSize=(20, 20)))
    if facce:
        break
W, H = im.size
if riq:
    box = tuple(riq)
elif facce:
    x, y, w, h = max(facce, key=lambda f: f[2] * f[3])
    cx, cy, lato = x + w / 2, y + h * 0.45, w * 1.55
if not riq and not facce:
    cx, cy, lato = W / 2, H * 0.2, min(W, H) * 0.5
if not riq:
    box = (int(cx - lato / 2), int(cy - lato * 0.62), int(cx + lato / 2), int(cy + lato * 0.62))
print("facce trovate:", len(facce), "ritaglio:", box)
t = im.crop(box).resize((256, 294), Image.LANCZOS)
m = Image.new("L", t.size, 0); d = ImageDraw.Draw(m)
d.ellipse((22, 0, 234, 252), fill=255)
d.polygon([(96, 205), (160, 205), (152, 294), (104, 294)], fill=255)
t.putalpha(m.filter(ImageFilter.GaussianBlur(2)))
t.save(out)
