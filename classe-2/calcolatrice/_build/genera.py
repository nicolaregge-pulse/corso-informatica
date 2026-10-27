# -*- coding: utf-8 -*-
"""Dispensa 2INF «La calcolatrice in Lazarus e su GitHub» (27/10/2026) con le foto della lavagna.
Una sola fonte -> MD (classe-2/calcolatrice), pagina online (docs/2inf-calcolatrice/), HTML di stampa per il PDF."""
import html, os
VER = '1.0'; DATA = '27/10/2026'
QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(os.path.dirname(QUI))
PDF = '20261027_Classe-2_v%s_Calcolatrice-Lazarus-GitHub_IT.pdf' % VER
GUIDA = 'https://nicolaregge-pulse.github.io/corso-informatica/2inf-calcolatrice-github/'
COD1 = """procedure TForm1.ButtonPiuClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(StrToInt(Edit1.Text) + StrToInt(Edit2.Text));
end;

procedure TForm1.ButtonPerClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(StrToInt(Edit1.Text) * StrToInt(Edit2.Text));
end;"""
COD2 = """procedure TForm1.ButtonMenoClick(Sender: TObject);
begin
  Edit3.Text := IntToStr(StrToInt(Edit1.Text) - StrToInt(Edit2.Text));
end;

procedure TForm1.ButtonDivClick(Sender: TObject);
begin
  if StrToInt(Edit2.Text) = 0 then
    Edit3.Text := 'Non si divide per zero'
  else
    Edit3.Text := IntToStr(StrToInt(Edit1.Text) div StrToInt(Edit2.Text));
end;"""
ALBERO = "lazarus/\n├── README.md\n├── primo-programma/\n├── salvadanaio/\n└── calcolatrice/\n    ├── calcolatrice.lpi\n    ├── calcolatrice.lpr\n    ├── unit1.pas\n    └── unit1.lfm"
# blocchi: (tipo, contenuto)
S = [
 ('h', '01 La lavagna: la calcolatrice versione 1.0'),
 ('img', ('lavagna-1-calcolatrice-v1.jpg', 'La lavagna di oggi: la finestra della calcolatrice versione 1.0')),
 ('ol', ['La finestra (form) ha tre caselle <b>Edit</b>: N1 (primo numero), N2 (secondo numero) e TOTALE (il risultato).',
         'Ha due bottoni (<b>Button</b>): <b>+</b> (più) e <b>×</b> (per).',
         'Quando premi un bottone, il programma legge N1 e N2, fa il conto e scrive il risultato in TOTALE.']),
 ('h', '02 StrToInt e IntToStr: testo e numeri'),
 ('ol', ['Quello che scrivi in una casella Edit è <b>testo</b>, anche se sono cifre: «12» è come una parola.',
         'Con il testo non si fanno i conti. Prima va trasformato in numero: <b>StrToInt</b> (da testo a numero intero).',
         'Il risultato è un numero. Per scriverlo nella casella va ritrasformato in testo: <b>IntToStr</b> (da numero intero a testo).',
         'Il giro è sempre lo stesso: testo → StrToInt → conto → IntToStr → testo.']),
 ('h', '03 Il codice della versione 1: più e per'),
 ('code', COD1),
 ('ol', ['Edit1 è N1, Edit2 è N2, Edit3 è TOTALE.', 'Il codice di ogni bottone si scrive con un doppio clic sul bottone nel form.', 'Prova con Esegui: 7 + 5 = 12, 7 × 5 = 35.']),
 ('h', '04 La versione 2: meno e divisione intera'),
 ('code', COD2),
 ('ol', ['<b>div</b> è la divisione intera: dà solo la parte intera, senza virgola. 7 div 2 = 3.',
         'Dividere per zero non si può: il programma andrebbe in errore. Per questo prima controlliamo se N2 è 0 (if … then … else).']),
 ('h', '05 Il tuo PC e GitHub'),
 ('img', ('lavagna-2-github.jpg', 'La lavagna: su GitHub vanno i file sorgenti, niente .exe; repository lazarus, cartella calcolatrice; commit spesso')),
 ('ol', ['Quando lavori con Lazarus, il programma sta sul tuo PC, nel disco fisso (HD): lavori <b>in locale</b>.',
         'GitHub è su internet: una copia del progetto che resta al sicuro anche se il PC si rompe.',
         'I due posti non si aggiornano da soli: sei tu a portare i file dal PC a GitHub.',
         'Su GitHub vanno solo i <b>file sorgenti</b>: .lpi, .lpr, .pas, .lfm. Il file calcolatrice.exe NO: Lazarus lo rifà quando premi Esegui.']),
 ('tab', [['Che cosa', 'Dove', 'Quando', 'Come'],
          ['<b>Salvare</b>', 'sul tuo PC (in locale)', 'spessissimo, ogni pochi minuti', 'in Lazarus premi Ctrl + S'],
          ['<b>Commit</b>', 'su GitHub (su internet)', 'ogni volta che una cosa nuova funziona', 'carichi i 4 file e premi «Commit changes»']]),
 ('pre', ALBERO),
 ('h', '06 Su GitHub, passo per passo'),
 ('ol', ['Apri la pagina guidata: <a href="%s">La calcolatrice su GitHub</a>. Ogni passo si apre solo quando quello prima è giusto.' % GUIDA,
         'La prima volta: crea la cartella con «Add file», «Create new file», nome <b>calcolatrice/README.md</b>, «Commit changes».',
         'Poi entra nella cartella calcolatrice: «Add file», «Upload files», «choose your files», scegli SOLO i 4 file con Ctrl, «Commit changes».',
         'Ogni volta che una cosa nuova funziona: Ctrl + S sul PC, poi ricarichi i 4 file su GitHub con un messaggio che dice che cosa hai cambiato (es. «aggiunto il bottone per»).']),
 ('h', '07 La release: v1.0 e v2.0'),
 ('ol', ['Una <b>release</b> è una versione finita e funzionante, con un numero.',
         'Versione 1 (più e per): nel repository lazarus, a destra, «Releases», «Create a new release», «Choose a tag», scrivi <b>v1.0</b>, «Create new tag», titolo «Calcolatrice versione 1», «Publish release».',
         'Versione 2 (anche meno e divisione intera): lo stesso con <b>v2.0</b>.']),
 ('h', '08 Sai spiegarlo?'),
 ('ol', ['A che cosa servono StrToInt e IntToStr?', 'Che differenza c\'è tra salvare con Ctrl + S e fare un commit?', 'Perché su GitHub non mettiamo il file .exe?', 'Che cos\'è la release v1.0?']),
]
e = html.escape
def md_inline(t):
    import re
    t = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r'[\2](\1)', t); t = t.replace('<b>', '**').replace('</b>', '**'); return t
md = ['# 00 La calcolatrice in Lazarus e su GitHub', '', '**Versione %s** — %s — Classe 2INF' % (VER, DATA), '']
for t, c in S:
    if t == 'h': md += ['## ' + c, '']
    elif t == 'img': md += ['![%s](%s)' % (c[1], c[0]), '']
    elif t == 'ol': md += ['%d. %s' % (i + 1, md_inline(x)) for i, x in enumerate(c)] + ['']
    elif t in ('code', 'pre'): md += ['```', c, '```', '']
    elif t == 'tab': md += ['| ' + ' | '.join(md_inline(x) for x in c[0]) + ' |', '|' + '---|' * len(c[0])] + ['| ' + ' | '.join(md_inline(x) for x in r) + ' |' for r in c[1:]] + ['']
md += ['## Changelog', '', '1. v1.0 (27/10/2026): prima versione, con le due foto della lavagna.', '']
open(os.path.join(QUI, 'calcolatrice.md'), 'w').write('\n'.join(md))
CSS = '''body{font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:16px;line-height:1.5;color:#1b1f24;background:#fff}
h1{font-size:27px;margin:6px 0 0}h2{font-size:21px;margin:26px 0 8px;break-after:avoid}.ver{color:#555;margin:2px 0 12px}
img{max-width:100%;height:auto;border-radius:8px;border:1px solid #ccd;display:block;margin:8px auto}figure{margin:10px 0;break-inside:avoid}figcaption{text-align:center;color:#555;font-size:14px}
pre{background:#0d1117;color:#e6edf3;border-radius:8px;padding:12px;overflow-x:auto;font-size:15px;break-inside:avoid}
table{width:100%;border-collapse:collapse;font-size:15px}th,td{border:1px solid #ccd;padding:6px 8px;text-align:left;vertical-align:top}th{background:#eef2f7}
.pdf a{display:inline-block;background:#1f6feb;color:#fff;padding:8px 14px;border-radius:8px;text-decoration:none}
@media print{img{max-height:115mm;width:auto}}'''
def corpo(online):
    h = ['<h1>La calcolatrice in Lazarus e su GitHub</h1><p class="ver">Versione %s — %s — Classe 2INF</p>' % (VER, DATA)]
    if online: h.append('<p class="pdf"><a href="%s" download>Scarica il PDF</a></p>' % PDF)
    for t, c in S:
        if t == 'h': h.append('<h2>%s</h2>' % e(c))
        elif t == 'img': h.append('<figure><img src="%s" alt="%s"><figcaption>%s</figcaption></figure>' % (c[0], e(c[1]), e(c[1])))
        elif t == 'ol': h.append('<ol>' + ''.join('<li>%s</li>' % x for x in c) + '</ol>')
        elif t in ('code', 'pre'): h.append('<pre>%s</pre>' % e(c))
        elif t == 'tab': h.append('<table>' + ''.join('<tr>' + ''.join(('<th>%s</th>' if i == 0 else '<td>%s</td>') % x for x in r) + '</tr>' for i, r in enumerate(c)) + '</table>')
    return '\n'.join(h)
pag = '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>La calcolatrice</title><style>%s</style></head><body>%s\n<script src="../assistente/assistente.js" data-pagina="2inf-calcolatrice" data-lingue="it"></script></body></html>' % (CSS, corpo(True))
open(os.path.join(ROOT, 'docs', '2inf-calcolatrice', 'index.html'), 'w').write(pag)
open(os.path.join(ROOT, 'docs', '2inf-calcolatrice', 'stampa.tmp.html'), 'w').write('<!doctype html><html lang="it"><head><meta charset="utf-8"><style>%s</style></head><body>%s</body></html>' % (CSS, corpo(False)))
print(PDF)
