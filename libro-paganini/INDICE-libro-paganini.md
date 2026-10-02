# Libro in dotazione — "Paganini — Tecnico esperto di computer e reti" (INDICE)

**Versione 1.1** — 01/10/2026

*Indice del manuale cartaceo in dotazione alla scuola. Fornito da Nicola (foto).
Serve come riferimento per allineare i materiali del corso alla struttura del libro e
attingere ai suoi questionari. Ogni capitolo ha "Come la vede Cisco" + "Questionari".*

**Dati del libro:** *Tecnico esperto di computer e reti* — Marco Paganini — **in riga
edizioni** (Informatica). Per i corsi "Sistemi e reti – **Cisco IT Essentials 7**".
**Vol. 1 — PC, Windows 10, reti, Cloud.** Edizione 2021.

> **Uso nel corso (PPP, 01/10/2026):** è una **linea guida / stella polare**, ma di
> livello **molto superiore** a quello attuale della Classe 1. Si usa per la **struttura**
> dei moduli e come **miniera di questionari** (190 domande), **adeguando/semplificando**
> sempre al livello dei ragazzi. NON è il libro da far leggere così com'è alla Prima.

---

## Struttura (capitoli e pagine)

1. **I dispositivi elettronici e i loro programmi** — p.21
   1.1 Hardware (22) — icone/immagini apparati: terminali, telefoni, periferiche, apparati di rete; media; "un po' di inglese"
   1.2 Software (28) — vari tipi; la programmazione (compilato o interpretato? per quale piattaforma?)
   1.3 Come la vede Cisco (33) — apparati mobili (laptop, smartphone, tablet/e-reader), indossabili
   1.4 1 Questionario (10 domande) — 39

2. **I PC desktop** — p.41
   2.1 Hardware desktop (41) — componenti base / specializzati; **montare un PC** (case, alimentatore, motherboard, dischi, cablaggi, schede espansione, prova di avvio); smontare/smaltire
   2.2 **Il firmware** (53) — **POST**, **BIOS/UEFI**, fasi del bootstrap
   2.3 Come la vede Cisco (59) — sicurezza; componenti (case, motherboard, CPU+dissipatori, memorie, dischi, NAS/SAN, porte, periferiche I/O, potenziamento); POST/BIOS/CMOS/UEFI
   2.4 4 Questionari (40 domande) — 113

3. **I PC laptop** — p.121
   3.1 Com'è fatto (case, motherboard, batterie, RAM, connessioni, display, tasti funzione)
   3.2 Come si configura (gestione energia)
   3.3 Come la vede Cisco · 3.4 2 Questionari (20 domande)

4. **Il sistema operativo Windows** — p.145
   4.1 Compiti del S.O. (requisiti hardware; gestione dischi: MBR/GPT, file system)
   4.2 Installazione (account/diritti, gestione dispositivi, Sysprep, da rete, unattended, recovery, sequenza di boot, attivazione/aggiornamento/upgrade, backup/migrazione)
   4.3 Interfaccia (versioni Windows, Desktop/Taskbar/Start, Task Manager, Esplora file, Raccolte/Cestino, recupero file EFS/BitLocker, ransomware, applicazioni comuni)
   4.4 Gestione del sistema (Impostazioni, Pannello di controllo, driver/nuovo hardware, nuovi programmi, funzioni amministrative: deframmenta, Registro, Gestione computer)
   4.5 **Sicurezza di Windows** (UAC, Defender Firewall, SmartScreen, criteri locali)
   4.6 **Linea di comando DOS (CLI)** (comandi comuni, CLI Win10, PowerShell)
   4.7 **Reti in Windows** (rete locale, NIC, condivisioni/mappatura, Gruppo di lavoro/Dominio, Internet, Desktop remoto, VPN, OneDrive)
   4.8 Funzioni avanzate per esperti (Systeminfo/Servizi/MMC/Registry, Utilità di pianificazione, Dominio/Criteri di gruppo, Hyper-V)
   4.9 Come la vede Cisco · 4.10 6 Questionari (60 domande)

5. **La rete connette gli apparati** — p.363
   5.1 Introduzione alle reti (363):
     5.1.1 Che cos'è una rete · **5.1.2 Numeri binari ed esadecimali (365)** — *il binario e
     l'esadecimale sono qui, in chiave reti* · 5.1.3 Protocolli e stack (TCP/IP, ISO/OSI) ·
     5.1.4 Segmenti/Pacchetti/Trame/Bit (i livelli, le PDU) · 5.1.5 Indirizzi (MAC, ARP,
     IPv4/IPv6, NAT/DHCP/DNS, porte) · 5.1.6 Apparati intermedi (Hub, Switch, Router, Firewall)
   5.2 Tipologie e topologie (393) — PAN/LAN/WLAN/MAN/WAN; topologie logiche e fisiche
   5.3 Altri concetti (403) — p2p, Client/Server, cablaggi e connettori (coassiale, coppie
     intrecciate, fibra, seriali, **Wi-Fi 802.11**), ICMP
   5.4 Come la vede Cisco (445) — Router ISR, Firewall/IDS/IPS/UTM, QoS, reti WMN, config
     Firewall, UPnP, DMZ, Port Forwarding, MAC filtering, blacklist/whitelist, IoT, SNMP,
     NetFlow, Wireshark
   5.5 5 Questionari (50 domande) — 471

6. **Virtualizzazione e Cloud** — p.481
   6.1 Virtualizzazione = Cloud? (481) · 6.2 La virtualizzazione (484) — principi, hypervisor
   tipo 1 e 2, VM, virtualizzazione della rete · 6.3 Il Cloud (488) · 6.4 Come la vede Cisco
   (490) — Data Center vs Cloud, virtualizzazione lato client, uso del Cloud, i container ·
   6.5 1 Questionario (10 domande)

---

## Come si lega al nostro corso (Classe 1)
1. **Modulo 3 (hardware / configurazione PC)** → capitoli **2 e 3** (desktop, laptop, firmware BIOS/UEFI, montaggio).
2. **Modulo 4 (montaggio + sistema operativo)** → capitolo **4** (Windows: installazione, interfaccia, sicurezza, CLI).
3. **Modulo 2 (reti)** → capitolo **5** (reti) + 4.7 (reti in Windows).
4. **Cloud/virtualizzazione** (anni successivi) → capitolo **6**.
5. **Software/programmazione** (Modulo 1, ponte verso Lazarus) → capitolo **1.2**.

## Note utili
1. **Binario ed esadecimale ci sono** (cap. **5.1.2**), ma **in chiave reti** e a livello alto:
   NON c'è una "base bit e byte" per principianti. Quella la costruiamo noi (scheda dedicata),
   molto più semplice, e poi si aggancia al libro più avanti. Il libro parte dai dispositivi,
   presuppone già delle basi → per la Prima va sempre **semplificato**.
2. **Tanti questionari pronti** (10+40+20+60+50+10 = 190 domande): ottima miniera per i nostri
   quiz su Google Moduli (hardware, Windows, reti).
3. "Come la vede Cisco" = taglio professionale/certificazione: utile per lo sbocco lavorativo.
