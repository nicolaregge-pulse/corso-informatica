import sys
from playwright.sync_api import sync_playwright
EXE='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
f=sys.argv[1]; out=sys.argv[2]; steps=[int(x) for x in sys.argv[3].split(',')]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=EXE,args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1100,'height':1000})
    errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
    pg.goto('file://'+f); pg.wait_for_timeout(300)
    cur=0
    for st in steps:
        while cur<st: pg.click('#bA'); cur+=1; pg.wait_for_timeout(1300)
        pg.screenshot(path=f'{out}_{st}.png')
    print('errori:',errs)
    b.close()
