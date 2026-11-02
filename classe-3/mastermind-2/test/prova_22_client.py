# Prova: N client in parallelo (thread) contro un server_mastermind GIA' avviato con --via o dopo il Via.
# Uso:  python3 prova_22_client.py PORTA N     (es. 5000 22). Ogni client risolve il Mastermind da solo; devono trovare TUTTI lo stesso codice.
import socket, threading, itertools, time, sys, random
PORT=int(sys.argv[1]); N=int(sys.argv[2]); HOST='127.0.0.1'
def req(line, t=5):
    s=socket.create_connection((HOST,PORT),timeout=t); s.sendall((line+'\n').encode())
    d=b''
    while not d.endswith(b'\n'):
        c=s.recv(200)
        if not c: break
        d+=c
    s.close(); return d.decode().strip()
def fb(a,b):
    e=sum(x==y for x,y in zip(a,b))
    from collections import Counter
    c=sum((Counter(a)&Counter(b)).values()); return e,c-e
res={}; errs=[]
def player(i):
    nome=f'Alunno{i:02d}'
    try:
        cand=[''.join(p) for p in itertools.product('123456',repeat=4)]
        random.shuffle(cand); tent=0
        while True:
            g=cand[0]; r=req(f'GUESS;{nome};{g}').split(';'); tent+=1
            if r[0]=='WIN': res[nome]=(g,tent,r); return
            if r[0]!='RESULT': errs.append((nome,r)); return
            e,s=int(r[1]),int(r[2]); cand=[c for c in cand if fb(c,g)==(e,s)]
    except Exception as ex: errs.append((nome,repr(ex)))
# prima del via?
print('prima del Via:',req('GUESS;Prova;1111'))
# client "cattivi": muto, mezza riga, chiusura brusca
m=socket.create_connection((HOST,PORT)); m2=socket.create_connection((HOST,PORT)); m2.sendall(b'GUESS;Zz;11'); m2.close()
t0=time.time()
th=[threading.Thread(target=player,args=(i,)) for i in range(1,N+1)]
[t.start() for t in th]; [t.join(60) for t in th]
print('tempo totale %.1fs, errori: %s'%(time.time()-t0,errs)); m.close()
print('giocatori che hanno vinto:',len(res),'di',N)
print('stessa combinazione per tutti:',set(v[0] for v in res.values()))
for n in sorted(res)[:3]+sorted(res)[-2:]: print(n,res[n][1],'tentativi',res[n][2])
print('STATO Alunno01:',req('STATO;Alunno01'))
print('STATO ultimo  :',req(f'STATO;Alunno{N:02d}'))
