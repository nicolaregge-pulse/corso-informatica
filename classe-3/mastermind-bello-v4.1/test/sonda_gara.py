# SONDA per la prova della gara: parla con il server con righe di testo vere (come farebbe un client),
# SENZA essere un giocatore nuovo: usa solo nomi di giocatori che ci sono gia'.
#  - durante la gara: ogni 0,7 secondi chiede STATO;<nome> e scrive tutta la risposta (piu' righe) in trace.txt
#  - quando compare il file "sonda_stop": fa la domanda finale per ogni nome e scrive sonda_finale.txt
# Uso: python3 sonda_gara.py porta cartella nome_per_il_trace nome1 nome2 ...
import socket, sys, time, os
PORT = int(sys.argv[1]); OUT = sys.argv[2]; NOME = sys.argv[3]; NOMI = sys.argv[4:]
def chiedi(riga, t=3):
    s = socket.create_connection(('127.0.0.1', PORT), timeout=t)
    s.sendall((riga + '\n').encode())
    d = b''
    try:
        while True:
            c = s.recv(500)
            if not c: break
            d += c
    except Exception:
        pass
    s.close()
    return d.decode().strip()
tr = open(os.path.join(OUT, 'trace.txt'), 'w')
while not os.path.exists(os.path.join(OUT, 'sonda_stop')):
    try:
        r = chiedi('STATO;' + NOME)
        tr.write('%.2f|%s\n' % (time.time(), r.replace('\n', ' // '))); tr.flush()
    except Exception as e:
        tr.write('ERRORE %r\n' % (e,)); tr.flush()
    time.sleep(0.7)
tr.close()
fin = open(os.path.join(OUT, 'sonda_finale.txt'), 'w')
for n in NOMI:
    try:
        fin.write('%s|%s\n' % (n, chiedi('STATO;' + n).replace('\n', ' // ')))
    except Exception as e:
        fin.write('%s|ERRORE %r\n' % (n, e))
# un client VECCHIO (v4.0.1) legge solo la prima riga: simuliamo chi chiude subito dopo la prima riga
s = socket.create_connection(('127.0.0.1', PORT), timeout=3)
s.sendall(b'STATO;' + NOMI[0].encode() + b'\n')
prima = b''
while not prima.endswith(b'\n'):
    c = s.recv(1)
    if not c: break
    prima += c
s.close()
fin.write('PRIMA_RIGA|%s\n' % prima.decode().strip())
fin.close()
