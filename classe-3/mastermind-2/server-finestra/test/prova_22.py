# 22 client veri che parlano con la finestra (simulata): collegano con STATO, aspettano il Via,
# giocano con strategia di eliminazione. Piu' un client muto, uno a meta' riga, uno con codice sbagliato.
import socket, threading, itertools, time, sys, random
from collections import Counter
PORT=int(sys.argv[1]); N=int(sys.argv[2]); MARC=sys.argv[3]; HOST='127.0.0.1'
def req(line, t=8):
    s=socket.create_connection((HOST,PORT),timeout=t); s.sendall((line+'\n').encode())
    d=b''
    while not d.endswith(b'\n'):
        c=s.recv(200)
        if not c: break
        d+=c
    s.close(); return d.decode().strip()
def fb(a,b):
    e=sum(x==y for x,y in zip(a,b)); c=sum((Counter(a)&Counter(b)).values()); return e,c-e
res={}; errs=[]; lat=[]
def player(i):
    nome=f'Alunno{i:02d}'
    try:
        while not req(f'STATO;{nome}').startswith('STATO;GIOCO'): time.sleep(0.3)
        cand=[''.join(p) for p in itertools.product('123456',repeat=4)]
        random.shuffle(cand); tent=0
        while True:
            g=cand[0]; t=time.time(); r=req(f'GUESS;{nome};{g}'); lat.append(time.time()-t); r=r.split(';'); tent+=1
            if r[0]=='WIN': res[nome]=(g,tent,r); return
            if r[0]!='RESULT': errs.append((nome,r)); return
            e,s=int(r[1]),int(r[2]); cand=[c for c in cand if fb(c,g)==(e,s)]
    except Exception as ex: errs.append((nome,repr(ex)))
print('prima del Via, GUESS:',req('GUESS;Anticipo;1111'))
m=socket.create_connection((HOST,PORT)); m2=socket.create_connection((HOST,PORT)); m2.sendall(b'GUESS;Zz;11'); m2.close()
print('codice sbagliato:',req('GUESS;Sbaglio;99'))
th=[threading.Thread(target=player,args=(i,)) for i in range(1,N+1)]
t0=time.time()
[t.start() for t in th]; [t.join(100) for t in th]
print('tempo totale %.1fs, errori: %s'%(time.time()-t0,errs))
print('vinto: %d di %d; combinazioni diverse: %s'%(len(res),N,set(v[0] for v in res.values())))
print('latenza risposta: max %.2fs, media %.3fs su %d richieste'%(max(lat),sum(lat)/len(lat),len(lat)))
m.close(); open(MARC,'w').write('ok')
