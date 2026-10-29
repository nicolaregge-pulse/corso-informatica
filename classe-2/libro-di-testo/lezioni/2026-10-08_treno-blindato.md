# Il treno blindato: squadre e ruoli

**Versione 1.0** — 29/10/2026
*Libro parziale della 2INF: la lezione del 08/10/2026. Fa parte del libro di testo della classe (libro-classe2). Il PDF serve per leggere e stampare; questo MD si dà alla tua AI, che lo spiega nella tua lingua.*

---

### Che cosa abbiamo fatto

1. **Quando:** 08/10/2026, Laboratorio.
2. **Argomenti:** Progetto del treno blindato: squadre con ruoli (CEO, Motore, Personaggi, Scenari, Test qualità), prime Pull Request entrate nel gioco.

### La teoria e l'esercitazione

Giovedì 08/10/2026 · lo costruiamo tutti insieme, come in un'azienda di software

**Il gioco:** sei dentro un vagone. Il treno attraversa boschi, paesi, città, montagne e mare. I cattivi saltano fuori da dietro alberi e case: li tocchi prima che sparino. Il vetro antiproiettile regge 5 colpi.





La mia squadra: cosa fare adesso
Gioca!
Il progetto su GitHub

#### 1. La nostra azienda (organigramma della lavagna)

| Ruolo | Cosa cura | File |
| --- | --- | --- |
| **CEO** | decide le priorità, approva i lavori con il prof, presenta il gioco | — |
| **SCENARI** | gli ambienti e il percorso: bosco, paese, città, montagna, mare | ambienti/\*.json, percorso.json |
| **PERSONAGGI** | i cattivi, le facce della classe, il protagonista | cattivi/pcNN.json, facce.json, protagonista.json |
| **MOTORE FISICA** | velocità del treno, tempi dei cattivi, colpi del vetro, punti | regole.json |
| **TEST QUALITÀ** (la Triade) | provano il gioco su PC e telefono, trovano i difetti, controllano le richieste delle altre squadre | — |
| **TUTTI** | il proprio cattivo | cattivi/pcNN.json |

**Il progetto (lavagna):** si guarda avanti dalla cabina, lungo i binari; i cattivi spuntano dalle finestre delle case, da dietro gli alberi e dai barili. Tre cose da curare: **1) dinamica** (come si muove il gioco), **2) UI** (cosa si vede: vetro, punti, tachimetro), **3) UX** (come ci si sente a giocare).

**Ruoli:** il prof è il **product owner** (decide cosa entra e fa il merge); in ogni squadra c'è un **project manager**, a turno; tutti sono **sviluppatori**; un compagno di un'altra squadra fa la **revisione**.

**Carta e penna:** prima di toccare il computer, ogni squadra scrive su un foglio chi fa cosa (il **backlog**) e disegna il suo pezzo: il cattivo, il paesaggio, il percorso.

#### Le foto della lavagna: usatele per progettare

**Il disegno del gioco:** si guarda avanti dalla cabina, lungo i binari; i cattivi spuntano dalle finestre, dagli alberi e dai barili. 1) Dinamica 2) UI 3) UX.

![Disegno del gioco alla lavagna](../../../docs/2inf-treno/img/lavagna-disegno-del-gioco.jpg)

**Come funziona Gemini** (le parole collegate):

![Mappa delle parole alla lavagna](../../../docs/2inf-treno/img/lavagna-come-funziona-gemini.jpg)

**La copertina con i personaggi** (disegnata con l'IA):

![Copertina del gioco](../../../docs/giochi/treno-blindato/img/copertina.jpg)

**Carta e penna:** ricopia sul quaderno il disegno del gioco e segna con un colore la parte della tua squadra.

#### Come funziona Gemini, il nostro assistente

Gemini ha letto moltissimi testi e ha imparato quali parole stanno insieme. Nella frase «Il **topo** è nella **tana**» collega «topo» a «scappato» e «tana» a «topolino»: quando gli scrivi, sceglie la parola che più probabilmente viene dopo. Per questo **più la tua frase è precisa, più la risposta è utile**. È un assistente: controlla sempre quello che ti risponde.





#### 2. Il tuo cattivo

**Regola:** il cattivo lo inventi tu: niente nomi veri, niente parolacce. Le facce vere sono solo quelle dei compagni maggiorenni che hanno dato la loro foto (le inserisce la squadra Personaggi).

**a) Inventalo con l'IA.** Apri Gemini, incolla questa frase e cambia la parte tra parentesi quadre:

Frase per Gemini

```
Sto creando un videogioco per la scuola. Inventa un cattivo buffo che assalta un treno, in stile cartone animato, non una persona reale. Il mio cattivo è [descrivi: colore, carattere, cosa indossa]. Dammi: un nome di massimo 24 caratteri, un colore in codice esadecimale (come #8a8f98) e una frase che grida di massimo 40 caratteri.
```

**b) Scegli il tuo PC:** — scegli —

Il nome del TUO file

Il tuo cattivo (poi cambia i valori con quelli di Gemini)

```
{
  "nome": "Il Bandito Nebbia",
  "colore": "#8a8f98",
  "occhi": 2,
  "cappello": 1,
  "bocca": 2,
  "velocita": 2,
  "frase": "Fermate quel treno!",
  "immagine": false
}
```

| Campo | Cosa puoi mettere |
| --- | --- |
| occhi | 1, 2 oppure 3 |
| cappello | 0 = niente, 1 = cappello, 2 = bandana sul viso |
| bocca | 0 = denti, 1 = bocca aperta, 2 = zig-zag |
| velocita | 1 = normale, 2 = veloce, 3 = velocissimo |

#### 3. Consegnalo su Classroom

**Si consegna SOLO su Classroom**, nel compito «Il treno blindato»: scrivi nel Documento e allega il disegno o la foto (bottone «Aggiungi o crea» → «File»). Non serve GitHub: gli sviluppatori (il prof con l'intelligenza artificiale) mettono la tua consegna su Git e la fanno entrare nella nuova versione del gioco. Così vedrai il tuo lavoro nel grafico delle versioni.



## Changelog
1. **v1.0 (29/10/2026)**: prima versione, dalle fonti della lezione.
