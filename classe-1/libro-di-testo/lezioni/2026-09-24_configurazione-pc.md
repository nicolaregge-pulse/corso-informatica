# Configurazione di un PC: standard hardware

**Versione 1.0** — 29/10/2026
*Libro parziale della 1INF: la lezione del 24/09/2026. Fa parte del libro di testo della classe (libro-classe1). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 24/09/2026, 3 ore, Tecnologia e Sicurezza.
2. **Argomenti:** Standard hardware: form factor (ATX, microATX, Mini-ITX), slot PCIe, socket Intel e AMD, RAM DDR3/4/5; documento con teoria e immagini consegnato su Classroom; correzione dei compiti.

### In breve · باختصار · 简要

<div class="scheda breve"><p lang="it">I pezzi del PC devono essere compatibili: la stessa misura (form factor), lo stesso socket, lo stesso tipo di RAM.</p><p lang="ar" dir="rtl">يجب أن تكون قطع الحاسوب متوافقة: نفس المقاس، نفس المقبس (socket)، نفس نوع الذاكرة RAM.</p><p lang="zh">电脑零件必须兼容：同样的尺寸（form factor）、同样的插座（socket）、同样类型的内存。</p></div>

### La teoria e l'esercitazione

#### Teoria
1. **Form factor:** grandezza della scheda madre — ATX (grande), microATX (media), Mini-ITX (piccola).
2. **Slot PCIe:** attacchi (x1, x4, x8, x16); il **x16** serve per la **scheda video**.
3. **Socket CPU:** **Intel = LGA** (es. LGA1700), **AMD = AM** (es. AM5); CPU e scheda madre stesso socket.
4. **Processori per marca:** Intel Core **i3/i5/i7/i9**, AMD Ryzen **3/5/7/9**.
5. **Memorie RAM:** **DDR3/DDR4/DDR5**, non intercambiabili (tacca diversa).

#### Il compito
1. Creare un documento in **Google Documenti** che spiega **con parole proprie** i 5 argomenti.
2. Inserire **immagini prese dal web** (almeno una per argomento).
3. **Consegnare** su Google Classroom.

#### Criteri di valutazione
1. **Completezza teoria**: spiegati tutti e 5 gli argomenti.
2. **Parole proprie**: spiegazione personale (prova del nove a voce).
3. **Immagini**: almeno una per argomento.
4. **Consegna**: su Classroom.

#### Teoria
1. **Rivedere insieme gli errori tipici** della configurazione: componenti dimenticati (spesso l'alimentatore), doppioni di RAM/SSD, totale non calcolato.
2. **Come si corregge un lavoro:** si guarda cosa manca, si aggiunge, si ricontrolla il totale.
3. **Migliorare è normale:** un lavoro si consegna, si riceve un riscontro e si migliora — come fanno i professionisti.

#### Il compito
1. Correggere e **completare** il proprio documento di configurazione con le indicazioni ricevute.
2. Ricontrollare compatibilità, presenza di tutti i componenti e totale.

#### Criteri di valutazione
1. **Correzione**: sistema gli errori segnalati.
2. **Completezza**: il lavoro finale ha tutti i componenti e il totale.

*Classe 1 — Informatica. Scheda docente + appunti per i ragazzi sugli standard
hardware: form factor (AT/ATX/microATX/Mini-ITX), slot PCIe (x1/x4/x8/x16),
socket della CPU (Intel LGA vs AMD PGA/AM5), tipi di RAM (DDR3/DDR4/DDR5, DIMM
vs SO-DIMM). I PDF (`20260924_Classe-1-PerTutti_v1.0_Standard-Configurazione-PC_IT/AR/ZH.pdf`)
contengono i disegni con le forme in proporzione reale, nelle 3 lingue; questo
`.md` è la fonte versionata e serve anche all'AI dei ragazzi per spiegare/tradurre.*

> Nota: i disegni (Fig. 1–4) sono nei file `standard-hardware-it/ar/zh.html` → PDF. Qui
> sono descritti a parole così che l'AI possa spiegarli in un'altra lingua.

---

#### Idea guida

Dentro un computer i pezzi devono **combaciare**: una scheda madre entra solo in
certi case, una CPU entra solo in un certo socket, una RAM entra solo nel suo
slot. Per farli combaciare, nel mondo ci si è messi d'accordo su **misure e forme
comuni**: sono gli **standard**. Ne vediamo quattro: form factor, slot PCIe,
socket, tipi di RAM.

> [BLU] Carta e penna: prima di guardare lo schermo, ognuno disegna a mano un
> rettangolo "scheda madre" e ci segna dove va la CPU (socket), dove le RAM (slot
> lunghi e stretti) e dove la scheda video (slot PCIe x16). Poi confronta con
> quello vero.

#### 1. Form factor — la taglia della scheda madre

**Form factor** = la misura standard della scheda madre. Decide anche quale
**case** ("cassone") serve: una scheda grande non entra in un case piccolo.

1. **ATX** — 305 × 244 mm. Il più diffuso: PC desktop e da gioco (schede "ATX"
   ASUS, MSI, Gigabyte, ASRock). Ha più slot (fino a 4 RAM, più PCIe).
2. **microATX (mATX)** — 244 × 244 mm. PC compatti ed economici, uffici.
3. **Mini-ITX** — 170 × 170 mm. Mini-PC, PC da salotto (HTPC): pochi slot.
4. **E-ATX** — 305 × 330 mm. Workstation e fascia alta, moltissimi slot.
5. **AT / Baby-AT** — storico (anni '80–'90, IBM): non più in commercio, solo
   cultura generale.

> [GIALLO] Da ricordare: ATX è lo standard "normale"; le altre sono variazioni.
> Più piccola = meno spazio = meno slot.

#### 2. Slot PCIe — dove si infilano le schede aggiuntive

**PCIe** (PCI Express) è lo slot per le **schede di espansione**, prima fra tutte
la **scheda video** (GPU). Il numero dice quante "corsie" (linee di dati) ha: più
corsie = più veloce. Una scheda corta entra anche in uno slot più lungo.
Lunghezze reali:

1. **PCIe x16** — 89 mm, 16 corsie: **scheda video** (NVIDIA GeForce, AMD Radeon).
2. **PCIe x8** — 56 mm, 8 corsie: RAID, schede di rete veloci, seconda GPU.
3. **PCIe x4** — 39 mm, 4 corsie: adattatori per SSD **NVMe**, controller.
4. **PCIe x1** — 25 mm, 1 corsia: schede di rete, audio, USB, acquisizione video.

> [BLU] Versioni PCIe: oltre alla lunghezza c'è la generazione 3.0 → 4.0 → 5.0.
> Ad ogni salto la banda raddoppia, ma la forma dello slot resta uguale
> (compatibili). **M.2** è invece un piccolo slot dedicato agli SSD NVMe: usa le
> corsie PCIe ma ha una forma tutta sua.

#### 3. Socket — dove si appoggia la CPU

Il **socket** è lo "zoccolo" sulla scheda madre dove si mette la **CPU**. Ogni
socket ha un nome e accetta solo certe CPU. Due famiglie, con una differenza
fisica:

1. **Intel — LGA** (Land Grid Array): i **pin sono nel socket**; la CPU ha
   contatti piatti.
2. **AMD — PGA** (Pin Grid Array): i **pin sono sulla CPU**. (Attenzione: **AM5**
   di AMD è invece **LGA**, come Intel.)

Nomi (socket → CPU che accetta):

1. **Intel LGA1700** — Intel Core 12ª · 13ª · 14ª gen (i3/i5/i7/i9).
2. **Intel LGA1851** — Intel Core Ultra (serie 2).
3. **AMD AM4** (PGA) — Ryzen serie 1000 → 5000.
4. **AMD AM5** (LGA) — Ryzen serie 7000 e 9000.
5. **Intel LGA4677 / AMD SP5** — server e workstation (Xeon, EPYC).

> [ROSSO] Attenzione: il numero nel nome (1700, 1851, AM4…) è legato ai
> **contatti**, non è "quanto è potente". CPU e scheda madre si comprano **sempre
> in coppia**, controllando che il socket sia lo stesso. Il triangolino "pin 1"
> in un angolo indica il verso giusto di inserimento.

#### 4. Tipi di RAM — DDR3, DDR4, DDR5

La **RAM** è la memoria di lavoro: le "bacchette" (moduli) negli slot lunghi
vicino alla CPU. Ogni generazione ha la **tacca (chiave) in una posizione
diversa**: così è impossibile metterla nello slot sbagliato. La scheda madre
supporta **una** sola generazione.

1. **DDR3** — 240 pin, 1,5 V. Es. DDR3-1600 (PC3-12800). PC vecchi.
2. **DDR4** — 288 pin, 1,2 V. Es. DDR4-3200 (PC4-25600). Standard recente.
3. **DDR5** — 288 pin, 1,1 V. Es. DDR5-5600 / 6000. Attuale (Corsair Vengeance,
   Kingston Fury, Crucial).
4. **SO-DIMM** — più corta: è la RAM dei **portatili** (stessa sigla + "SO-DIMM").

> [GIALLO] DDR4 e DDR5 hanno tutte e due 288 pin, ma la tacca è in un punto
> diverso e la scheda madre ne supporta una sola: non sono intercambiabili. La
> RAM da desktop (DIMM, lunga) è diversa da quella del portatile (SO-DIMM, corta).

#### 5. Riepilogo — cosa deve combaciare con cosa

1. **Case ⟷ scheda madre**: stesso form factor (ATX, microATX, Mini-ITX).
2. **Scheda madre ⟷ CPU**: stesso socket (LGA1700, AM5…).
3. **Scheda madre ⟷ RAM**: stessa generazione (DDR4 con DDR4, DDR5 con DDR5).
4. **Scheda video ⟷ scheda madre**: slot PCIe x16.

> [BLU] La prova del nove (saperlo spiegare): ogni ragazzo racconta a voce, con
> parole sue, "Perché non posso mettere una CPU AMD su una scheda Intel? Perché
> una DDR5 non entra in uno slot DDR4?". Se lo sa spiegare, ha capito davvero.

> [GIALLO] Collegamento al compito: questi standard sono i controlli che fa
> PCPartPicker quando montiamo il PC (attività "Costruisci il PC"): avvisa se
> socket, RAM o form factor non combaciano. Ora sappiamo perché lo fa.

#### Schema alla lavagna (fatto in classe)

Lo stesso contenuto è stato disegnato a mano alla lavagna durante la lezione del
24/09/2026 (metodo "carta e penna"): SLOT schede (PCIe con la tacca), SLOT RAM
(piedini + tacca), SOCKET CPU (il processore che si ribalta + i pin sotto),
GRANDEZZA MB/CASE → AT, ATX, mini-ATX. Foto: `immagini/20260924_Classe-1-PerTutti_Lavagna-Configurazione-PC.jpg`.


## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
