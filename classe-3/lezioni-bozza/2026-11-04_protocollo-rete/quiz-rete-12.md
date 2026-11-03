# Quiz di rete: il protocollo del Mastermind (12 domande)

Soglia KPI: 8 su 12. La risposta giusta è la prima di ogni elenco (nel Modulo le risposte si mescolano).

1. Su quale porta ascolta il server del Mastermind?
   - GIUSTA: 5050
   - sbagliata: 80
   - sbagliata: 21
   - sbagliata: 1234

2. Quale riga manda il client per chiedere "come va la partita?" (il nome è Sara)?
   - GIUSTA: STATO;Sara
   - sbagliata: GUESS;Sara;STATO
   - sbagliata: WAIT;Sara
   - sbagliata: RESULT;Sara

3. Il Prof non ha ancora premuto Via. Sara manda GUESS;Sara;1234. Che cosa risponde il server?
   - GIUSTA: WAIT
   - sbagliata: WIN;Sara;1;0;1;1;1;1
   - sbagliata: RESULT;4;0;1;0;0;0;0
   - sbagliata: STATO;GIOCO;0;0;0;0;0

4. Il server risponde RESULT;2;1;4;0;3;3;7. Quanti piolini neri e quanti bianchi?
   - GIUSTA: 2 neri e 1 bianco
   - sbagliata: 1 nero e 2 bianchi
   - sbagliata: 4 neri e 0 bianchi
   - sbagliata: 0 neri e 4 bianchi

5. Nella stessa riga RESULT;2;1;4;0;3;3;7 il campo "posto" vale 0. Che cosa vuol dire?
   - GIUSTA: Non hai ancora finito: non hai ancora un posto in classifica
   - sbagliata: Sei arrivato ultimo
   - sbagliata: Il server ha sbagliato
   - sbagliata: Hai vinto con 0 tentativi

6. Il server risponde WIN;Sara;5;62;2;4;3;8. Quanti tentativi e quanti secondi?
   - GIUSTA: 5 tentativi e 62 secondi
   - sbagliata: 62 tentativi e 5 secondi
   - sbagliata: 2 tentativi e 4 secondi
   - sbagliata: 3 tentativi e 8 secondi

7. Sara scrive per errore GUESS;Sara;1237. Che cosa risponde il server?
   - GIUSTA: ERR;codice non valido (servono 4 cifre da 1 a 6)
   - sbagliata: WAIT
   - sbagliata: RESULT;4;0;1;0;0;0;0
   - sbagliata: WIN;Sara;1;0;1;1;1;1

8. Nella riga RESULT;1;2;5;0;3;4;9 il primo campo (RESULT) è il numero 0. Quale numero ha il campo dei bianchi?
   - GIUSTA: 2
   - sbagliata: 1
   - sbagliata: 3
   - sbagliata: 0

9. Il codice segreto è 1123 e il tentativo è 1211. Quanti neri e quanti bianchi risponde il server?
   - GIUSTA: 1 nero e 2 bianchi
   - sbagliata: 2 neri e 1 bianco
   - sbagliata: 0 neri e 4 bianchi
   - sbagliata: 3 neri e 0 bianchi

10. Ogni quanto tempo il client chiede STATO al server, anche se nessuno preme niente?
   - GIUSTA: Ogni 3 secondi
   - sbagliata: Mai
   - sbagliata: Solo quando si preme Prova
   - sbagliata: Ogni ora

11. Quando arriva una riga RESULT, che cosa fa la UnitRete per avvisare la finestra?
   - GIUSTA: Fa partire l'evento OnRisultato, come un click su un bottone
   - sbagliata: Disegna lei i piolini sulla tavola
   - sbagliata: Chiude il programma
   - sbagliata: Scrive nella finestra con Forms

12. Quale unit contiene i socket e il protocollo, e NON conosce nessuna finestra?
   - GIUSTA: UnitRete
   - sbagliata: UnitInterfaccia
   - sbagliata: UnitServer
   - sbagliata: DisegnoMastermind
