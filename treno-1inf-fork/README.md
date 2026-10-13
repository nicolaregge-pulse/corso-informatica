# Il treno blindato — versione Godot (v2.0)

**Versione 2.0** — 09/10/2026

1. Cos'è: lo stesso gioco della 1INF (v1.1, HTML) rifatto con il motore **Godot 4.7**. È cambiato il motore, cioè una cosa grossa: per questo il numero passa da 1.x a **2.0** (versione major).
2. Come si apre: Godot portabile → «Importa» → scegli `project.godot` di questa cartella → «Esegui» (F5).
3. Dove si gioca nel browser: `docs/giochi/treno-godot/` (esportato da Godot per il Web).
4. I file:
   1. `treno.gd` — tutto il codice, commentato in italiano (il «battito» `_process`, il «pennello» `_draw`, il clic `_unhandled_input`).
   2. `main.tscn` — la scena: un solo nodo (Node2D) con lo script.
   3. `dati/` — i dati dei ragazzi in file .json: `cattivi.json` (i cattivi della 1INF), `ambienti.json`, `regole.json`, `testi.json`. Per cambiare il gioco basta cambiare i dati.
5. Ponte da Lazarus: Lazarus **reagisce** (aspetta un clic), Godot **pulsa** (`_process` gira circa 60 volte al secondo).
