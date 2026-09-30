# Strumenti di rendering PDF

**Versione 0.1** — 30/09/2026 · uso interno docente (nessun contenuto per i ragazzi)

Script che rendono HTML/Markdown in PDF impaginato. Usati dalla pipeline dei documenti
del corso. Richiedono Node + Playwright/Chromium nell'ambiente (variabile `NODE_PATH`
verso `node_modules`, Chromium via `PW_EXECUTABLE`): non si versionano `node_modules`.

1. `render_doc.js <html> <pdf> "<headerLeft>" "<headerRight>" "<footerLeft>"` — rende un
   HTML in PDF **con header e footer** (numeri di pagina). Margini gestiti dal renderer
   (NON mettere `@page{margin:0}` nell'HTML, azzererebbe i margini).
2. `md2pdf_doc.py <input.md> <output.pdf> [headerLeft] [headerRight] [footerLeft]` —
   converte un Markdown del corso (titoli, liste numerate/gerarchiche, tabelle, `>` box,
   `**grassetto**`, `` `codice` ``, blocchi ``` ```) in HTML impaginato + PDF via render_doc.js.
3. `render_generic.js <html> <pdf>` — rende un HTML in PDF senza header/footer (per schede/moduli).
4. `shot_page.js <html> <png>` — screenshot di una pagina HTML locale (per le anteprime nei libri).
