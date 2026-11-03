from playwright.sync_api import sync_playwright
EXE='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
import sys
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=EXE,args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1000,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+sys.argv[1]); pg.wait_for_timeout(300)
    pg.fill('#nome','Sara')
    pg.click('button:has-text("Manda STATO")'); pg.click('button:has-text("Manda GUESS")')  # WAIT con 0 colori -> messaggio
    for i in (1,2,3,4):
        pg.click('.pgb >> nth=%d'%(i-1))
    pg.click('button:has-text("Manda GUESS")')
    pg.click('button:has-text("Via!")')
    for i in (1,2,3,4): pg.click('.pgb >> nth=%d'%(i-1))
    pg.click('button:has-text("Manda GUESS")')
    pg.fill('#libera','GUESS;Sara;1237'); pg.click('button:has-text("Manda questa riga")')
    pg.fill('#libera','CIAO'); pg.click('button:has-text("Manda questa riga")')
    # forza vittoria: prova tutte le combinazioni via JS
    pg.evaluate("""()=>{for(let a=1;a<=6;a++)for(let b=1;b<=6;b++)for(let c=1;c<=6;c++)for(let d=1;d<=6;d++){ if(document.getElementById('fatto').style.display==='block')return; PF.sc=[a,b,c,d]; PF.prova(); }}""")
    print('conta:',pg.inner_text('#conta'),'errori',errs)
    pg.locator('.sim').scroll_into_view_if_needed(); pg.screenshot(path=sys.argv[2],full_page=False)
    pg.goto('file://'+sys.argv[1].replace('lezione','ora2')); pg.screenshot(path=sys.argv[2].replace('.png','_o2.png'))
    b.close()
