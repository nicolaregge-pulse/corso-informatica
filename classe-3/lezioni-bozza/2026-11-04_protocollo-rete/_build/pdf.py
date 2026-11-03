import sys
from playwright.sync_api import sync_playwright
EXE='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
src,out=sys.argv[1],sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=EXE,args=['--no-sandbox']); pg=b.new_page()
    pg.goto('file://'+src); pg.wait_for_timeout(300)
    pg.pdf(path=out,format='A4',landscape=True,print_background=True,prefer_css_page_size=True)
    b.close()
