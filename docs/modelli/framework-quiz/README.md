# Modello Framework QUIZ (uso interno, NON per i ragazzi)

Cartella modello della pagina-lezione descritta in `FRAMEWORK-QUIZ.md` (versione 1.0, 04/11/2026). Non si linka da nessuna pagina pubblica di classe; `modello.html` ha `noindex`. Non è una lezione: contiene segnaposto.

1. Copiare la cartella in `docs/anteprima/<classe>-<argomento>-<GG-MM>/` e rinominare `modello.html` in `modulo-1.html`.
2. Sostituire i segnaposto (cerca con `grep -n "{{" modulo-1.html`; deve restare zero): `{{CLASSE}}`, `{{MATERIA}}`, `{{GIORNO}}`, `{{DATA}}`, `{{DATA_ISO}}`, `{{RIGA_CONSEGNA}}`, `{{TITOLO_ORA_IT}}`, `{{TITOLO_ORA_AR}}`, `{{TITOLO_ORA_ZH}}`, `{{N_ORA}}`, `{{SLUG}}`, `{{LINK_CRUSCOTTO}}`, `{{LINK_MONITOR}}`, `{{LINK_CONSEGNA}}`, `{{CHIAVE_QUIZ}}`, `{{QUIZ_ARGOMENTO}}`, `{{QUIZ_N}}`, `{{QUIZ_MINUTI}}`, `{{QUIZ_SOGLIA}}`, `{{INTRO_*}}`, `{{PASSO1_*}}`, `{{PASSO2_*}}`, `{{CODICE_DA_COPIARE}}`, `{{FALLO_TUO_*}}`, `{{QUADERNO_RIGHE}}`, `{{FILE_DA_CONSEGNARE}}`.
3. Sostituire gli schemi di `img/` (sono segnaposto) e aggiungere i passi che servono, uno per azione.
4. In `config.json`: indirizzo del Modulo quiz sotto la chiave scelta, `invio` e `attivo: true`, `ore_sbloccate: 1`.
5. Togliere questo README dalla copia. Prima di pubblicare: capitolo 07 di `FRAMEWORK-QUIZ.md`.
