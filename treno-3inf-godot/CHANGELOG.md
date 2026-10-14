# Changelog — Il treno blindato della 3INF su Godot

Fork pulito della **base del prof** su Godot (`treno-prof-godot`, v1.0). Ogni versione dice **cosa cambia e perché**.
I numeri si leggono così: MAJOR.MINOR.PATCH (cambio grosso . aggiunta . correzione di un errore).
Ogni versione si gioca al suo link: `https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-3inf-v2/versioni/<versione>/`
L'ultima versione è sempre a `https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-3inf-v2/`.

## v2.0 — 14/10/2026 12:36 — Il fork pulito della 3INF

1. Perché 2.0 (MAJOR): il treno della 3INF era in HTML (v1.0 … v1.11, in `docs/giochi/treno-3inf/`); ora gira sul motore Godot. Si riparte dalla base del prof, pulita, e le richieste della classe si rifanno una alla volta.
2. Velocità tranquilla della base: `velocita_treno` 0.5 (richiesta del prof: niente velocità esagerate).
3. Motore (`treno.gd`), chiavi nuove: `aumento_per_livello` in `regole.json` (quanto accelera il treno a ogni livello, da 0 a 0.5, normale 0.04); `rocce_varie` negli ambienti (rocce di grandezze da 0.6 a 1.5 volte e toni un po' più chiari o più scuri); `tuta` e `pelle` nei cattivi (colore della tuta al posto della mimetica, colore della pelle).
4. Memoria del browser separata: i record si salvano con i nomi `treno-3inf-v2-...`.

## v2.1 — 14/10/2026 12:37 — Noah: il treno accelera a ogni livello

1. PR di Noah (REGOLE): il treno parte lento (velocita_treno 0.5, come la base) e a ogni livello va un po' più veloce (aumento_per_livello 0.06, cioè +6% per livello). Aumento dolce, richiesto dal prof: niente velocità esagerate.

## v2.2 — 14/10/2026 12:37 — Andrea G.: cielo grigio in città

1. PR di Andrea G. (AMBIENTI): in città il cielo è grigio (cielo_alto #6f767e, cielo_basso #b9bec4). Conflitto risolto: il grigio vale solo per la città, la montagna non si tocca, come avevano chiesto Dani e Ale (montagna serena).

## v2.3 — 14/10/2026 12:37 — Ariel: rocce di grandezze e toni diversi

1. PR di Ariel (AMBIENTI): in montagna le rocce hanno grandezze diverse (da 0.6 a 1.5 volte) e toni un po' più chiari o più scuri (rocce_varie: true, chiave nuova del motore della 3INF).

## v2.4 — 14/10/2026 12:37 — Ariel: l'alieno verde tra i nemici

1. PR di Ariel (CATTIVI): tra i nemici compare l'Alieno verde (cattivi/pc13.json): pelle verde, tuta argento, dice «BLIP BLOP!».

## v2.5 — 14/10/2026 12:37 — David A.: paesaggio meno vuoto

1. PR di David A. (AMBIENTI): in montagna ci sono più rocce, il paesaggio è meno vuoto (densita 3, il massimo).

## v2.6 — 14/10/2026 12:38 — Tomas: il nemico Tuta

1. PR di Tomas (CATTIVI): il nemico Tuta, con la tuta arancione (cattivi/pc31.json), dice «Ehi, ferma il treno!».
