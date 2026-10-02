# Scheda sintetica — Lezione frontale: I DATI IN BINARIO (3 ore · Classe 1INF)

**Versione 0.1** — 02/10/2026 · *Materiale DOCENTE (italiano). Canovaccio per la spiegazione
frontale alla lavagna (regola §2.22). Dispensa e compiti per i ragazzi (trilingui) li genero DOPO,
seguendo le TUE foto della lavagna (§2.17-2.18). Principio §2.24: sovradimensionare + NUCLEO base
per tutti + EXTRA per chi finisce prima.*

> Filo delle 3 ore: **tutto nel computer è numeri in binario** — i numeri, le lettere, i colori,
> e tutto "pesa" in byte. Una vittoria mostrabile diversa a ogni ora: **un numero · il tuo nome ·
> un colore**.

---

## ORA 1 — Decimale → Binario

### Concetto (1 frase)
Ieri da binario a decimale (leggevamo la griglia). Oggi **l'inverso**: dato un numero normale, lo
scriviamo in 0 e 1. Stesso disegno, al contrario.

### Metodo delle caselle (consigliato — stessa griglia di ieri)
1. Scrivi i valori: **128 64 32 16 8 4 2 1**.
2. Da **sinistra (128)**: "ci sta nel numero?" **Sì → 1** e togli quel valore (tieni il resto);
   **No → 0** e vai avanti.
3. Fino alla casella 1. Gli 0/1 letti da sinistra = il numero binario.
4. Ricorda gli **0 davanti**: 8 caselle (5 = `00000101`, non `101`).

### Esempi alla lavagna (facile → medio)
1. **13** = 8+4+1 → `00001101`
2. **78** = 64+8+4+2 → `01001110`  *(è quello di ieri: bell'aggancio)*
3. **200** = 128+64+8 → `11001000`

### Vinci subito · Fallo tuo · Mostralo
1. **Vinci subito:** `5` → `00000101` (30 secondi, prima vittoria).
2. **Fallo tuo:** converti **la tua età** o il **giorno del compleanno**.
3. **Mostralo:** uno scrive un numero in binario, il compagno lo decifra.

### Errori da prevenire (dillo PRIMA)
Dimenticare gli 0 davanti · non aggiornare il resto dopo un 1 · confondere "leggere" (ieri) con
"costruire" (oggi).

### Nucleo base / Extra (§2.24)
- **Base (tutti):** numeri **fino a 31** (bastano 5 caselle).
- **Extra (veloci):** numeri **fino a 255**; oppure il metodo **divisioni successive per 2**
  (dividi per 2, scrivi i resti, leggi dal basso) come secondo metodo.

---

## ORA 2 — ASCII: il tuo nome in binario

### Concetto
Nel computer **anche le lettere sono numeri**: ogni carattere ha un codice (**ASCII**). Per
scrivere una lettera in binario: **lettera → suo numero → binario** (col metodo dell'Ora 1!).

### Mini-tabella (maiuscole)
`A=65 B=66 C=67 D=68 E=69 F=70 G=71 H=72 I=73 J=74 K=75 L=76 M=77 N=78 O=79 P=80 Q=81 R=82 S=83 T=84 U=85 V=86 W=87 X=88 Y=89 Z=90`
- **minuscole = MAIUSCOLA + 32** (a=97, b=98 …) · **spazio = 32** · **cifre '0'..'9' = 48..57**.

### Esempio
`A` = 65 = `01000001`. La parola `CIAO` = C(67) I(73) A(65) O(79).

### Vinci subito · Fallo tuo · Mostralo
1. **Vinci subito:** una lettera (es. la tua iniziale).
2. **Fallo tuo:** scrivi il **TUO nome** in binario (ogni lettera un byte).
3. **Mostralo:** scambia col compagno e **decifra** il suo nome.

### Errori da prevenire
Maiuscole ≠ minuscole (A=65, a=97) · lo spazio è un carattere (32) · ricordare gli 0 davanti.

### Nucleo base / Extra (§2.24)
- **Base:** iniziali o nome **corto in MAIUSCOLO** (tabella data).
- **Extra:** nome **+ cognome**, con **minuscole** e **spazio**; oppure una parola/frase propria.

---

## ORA 3a — Colori in codice (RGB, senza esadecimale)

### Concetto
Ogni colore sullo schermo è fatto di **3 numeri**: **R**osso, **V**erde (Green), **B**lu — ognuno
da **0 a 255** (cioè **1 byte = 8 bit** a testa). Un colore = **3 byte = 24 bit**.

### Esempi (colori "puri")
`rosso = 255,0,0` · `verde = 0,255,0` · `blu = 0,0,255` · `bianco = 255,255,255` ·
`nero = 0,0,0` · `giallo = 255,255,0`.

### Vinci subito · Fallo tuo · Mostralo
1. **Vinci subito:** indovina/scrivi il rosso puro (255,0,0).
2. **Fallo tuo:** ognuno sceglie il **suo colore preferito** e scrive i 3 numeri (si può provare
   con un selettore colori online: si vede subito il colore cambiare).
3. **Mostralo:** indovina il colore dai 3 numeri del compagno.

### Nucleo base / Extra (§2.24)
- **Base:** colori puri (solo 0 o 255).
- **Extra:** colori **mescolati** (es. arancione 255,165,0; viola 128,0,128) e **convertire in
  binario** uno dei tre numeri.

---

## ORA 3b — Quanto pesa? (i multipli, pratico e concreto) ⭐

### Concetto
Ripasso: **1 byte = 8 bit**; **1 KB ≈ 1000 byte**, **1 MB ≈ 1000 KB**, **1 GB ≈ 1000 MB**
(in realtà 1024, ma per i conti a mente va bene 1000). Le cose "pesano" in questi.

### Ordini di grandezza (da scrivere alla lavagna)
- 1 lettera = **1 byte** · una pagina di testo ≈ **pochi KB**.
- 1 **foto** del telefono ≈ **3–5 MB**.
- 1 **canzone** (MP3) ≈ **4–5 MB** (circa 1 MB al minuto).
- 1 **film** ≈ **1–5 GB** (in alta qualità anche di più).

### Il conto chiave — "quante foto in una chiavetta da 16 GB?"
16 GB ≈ **16.000 MB**. Una foto ≈ **4 MB** → 16.000 ÷ 4 = **~4.000 foto**.
- Canzoni: 16.000 ÷ 4 ≈ **~4.000 canzoni**.
- Film: 16.000 ÷ 4.000 (un film ~4 GB) ≈ **~4 film** (o di più se più leggeri).

### Vinci subito · Fallo tuo · Mostralo
1. **Vinci subito:** "quante foto in 1 GB?" (1.000 ÷ 4 ≈ 250).
2. **Fallo tuo:** quante **tue** foto stanno nel **tuo** telefono/chiavetta.
3. **Mostralo:** stima quanto pesa (e quante ne stanno) del tuo film/album preferito.

### Nucleo base / Extra (§2.24)
- **Base:** la tabella dei pesi + il conto guidato delle foto in 16 GB.
- **Extra:** altri tagli (32/64/128 GB), canzoni e film, conversioni GB↔MB a mano.

---

## Nota finale (per me, Claude)
Dopo le tue foto della lavagna genero, per i ragazzi: **dispensa trilingue** (con le foto),
**compito** con la **stessa grafica**, **pubblicazione su Classroom con scadenza**; poi, dalle
consegne, **libro individuale + griglie + report**. Tutto **sovradimensionato** con base + extra
(§2.24), carta e penna sempre.
