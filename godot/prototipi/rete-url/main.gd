# =====================================================================
# main.gd  -  "Cosa succede in rete quando scrivi un URL?"
# =====================================================================
# COSA FA
#   Mostra, passo dopo passo, il viaggio di una richiesta web:
#   cache, DNS, TCP, TLS, HTTP, risposta, disegno della pagina.
#   Quattro nodi (PC, router, server DNS, server del sito) e dei
#   pacchetti che viaggiano tra loro. In alto c'e' il contatore dei ms.
#
# PONTE LAZARUS -> GODOT
#   Form di Lazarus            ->  Scena (questo file e' attaccato al nodo "Main")
#   TEdit (Edit1.Text)         ->  LineEdit (UrlEdit.text)
#   TButton + Button1Click     ->  Button + segnale "pressed" collegato a una funzione
#   Label.Caption := 'ciao'    ->  Label.text = "ciao"
#   TTimer / animazione a mano ->  Tween (muove le cose da solo, in modo fluido)
#   array of record            ->  Array di Dictionary (qui: la lista dei passi)
#   procedure                  ->  func
# =====================================================================
extends Control

const URL_PREDEFINITO := "https://www.esempio.it/pagina"

# Numeri dei nodi: servono per dire "da dove a dove" viaggia un pacchetto.
const PC := 0
const ROUTER := 1
const DNS := 2
const SITO := 3
const NOMI := ["PC / Browser", "Router", "Server DNS", "Server del sito"]

# Colori dei pacchetti: giallo = domanda, verde = risposta.
const COL_RICHIESTA := Color(1, 0.8, 0.2)
const COL_RISPOSTA := Color(0.5, 0.95, 0.5)

# I nodi disegnati nella scena (come i componenti sul Form).
@onready var nodi: Array = [$Nodi/Pc, $Nodi/Router, $Nodi/Dns, $Nodi/Sito]
@onready var url_edit: LineEdit = $UrlEdit
@onready var btn_avvia: Button = $BtnAvvia
@onready var btn_avanti: Button = $BtnAvanti
@onready var btn_ricomincia: Button = $BtnRicomincia
@onready var lbl_ms: Label = $LblMs
@onready var lbl_ora: Label = $LblOra
@onready var lbl_titolo: Label = $Pannello/LblTitolo
@onready var spiegazione: RichTextLabel = $Pannello/Spiegazione
@onready var pacchetto: ColorRect = $Pacchetto

# Le "variabili globali" del programma (come le var del Form in Lazarus).
var passi: Array = []          # la lista degli 8 passi
var passo_attuale := -1        # -1 = non e' ancora partito
var ms_totali := 0             # millisecondi "veri" accumulati
var ms_mostrati := 0.0         # quelli che si vedono (salgono piano piano)
var occupato := false          # true mentre i pacchetti viaggiano
var tween: Tween

# Pezzi dell'indirizzo (riempiti da analizza_url).
var schema := "https"
var dominio := "www.esempio.it"
var percorso := "/pagina"
var ip := "203.0.113.10"


# ---------------------------------------------------------------------
# PARTENZA  (come FormCreate in Lazarus)
# ---------------------------------------------------------------------
func _ready() -> void:
	# Collego i bottoni alle funzioni: e' il "segnale" (come OnClick).
	btn_avvia.pressed.connect(_on_avvia_pressed)
	btn_avanti.pressed.connect(_on_avanti_pressed)
	btn_ricomincia.pressed.connect(_on_ricomincia_pressed)
	# Premere Invio nella casella equivale a premere Avvia.
	url_edit.text_submitted.connect(func(_t): _on_avvia_pressed())
	ricomincia()


# ---------------------------------------------------------------------
# I BOTTONI  (i gestori di evento)
# ---------------------------------------------------------------------
func _on_avvia_pressed() -> void:
	if occupato:
		return
	analizza_url(url_edit.text)
	costruisci_passi()
	azzera_scena()
	passo_attuale = 0
	esegui_passo()


func _on_avanti_pressed() -> void:
	if occupato or passo_attuale < 0 or passo_attuale >= passi.size() - 1:
		return
	passo_attuale += 1
	esegui_passo()


func _on_ricomincia_pressed() -> void:
	if tween:
		tween.kill()
	ricomincia()


# Torna alla situazione iniziale.
func ricomincia() -> void:
	occupato = false
	passo_attuale = -1
	passi = []
	url_edit.text = URL_PREDEFINITO
	azzera_scena()
	lbl_titolo.text = "Benvenuto!"
	spiegazione.text = "Scrivi un indirizzo web nella casella in alto (o lascia quello pronto).\n\nPoi premi [b]Avvia[/b]. Con [b]Avanti[/b] vai al passo dopo.\n\nVedrai cosa fa il computer prima di mostrarti una pagina. Succede in meno di un secondo, ma sono tante cose!"
	aggiorna_bottoni()


# Rimette a posto nodi, contatore e pacchetto.
func azzera_scena() -> void:
	ms_totali = 0
	ms_mostrati = 0.0
	mostra_ms(0.0)
	pacchetto.visible = false
	lbl_ora.text = ""
	for i in range(nodi.size()):
		scrivi_nodo(i, "")
		nodi[i].modulate = Color.WHITE


func aggiorna_bottoni() -> void:
	btn_avvia.disabled = occupato
	btn_avanti.disabled = occupato or passo_attuale < 0 or passo_attuale >= passi.size() - 1
	btn_ricomincia.disabled = false


# ---------------------------------------------------------------------
# L'INDIRIZZO: lo spezzo in schema / dominio / percorso
# Esempio: https://www.esempio.it/pagina  ->  https , www.esempio.it , /pagina
# ---------------------------------------------------------------------
func analizza_url(testo: String) -> void:
	var t := testo.strip_edges()
	if t == "":
		t = URL_PREDEFINITO
	schema = "https"
	if "://" in t:
		var pezzi := t.split("://", false, 1)
		schema = pezzi[0].to_lower()
		t = pezzi[1] if pezzi.size() > 1 else ""
	if schema != "http":
		schema = "https"
	# Da qui in poi: dominio/percorso
	var barra := t.find("/")
	if barra == -1:
		dominio = t
		percorso = "/"
	else:
		dominio = t.substr(0, barra)
		percorso = t.substr(barra)
	dominio = dominio.to_lower()
	if dominio == "":
		dominio = "www.esempio.it"
	# IP di esempio: 203.0.113.x e' un numero riservato agli esempi.
	ip = "203.0.113." + str(10 + abs(dominio.hash()) % 200)


# Restituisce solo la fine del dominio, es. "www.esempio.it" -> "it".
func estensione() -> String:
	var parti := dominio.split(".")
	return parti[parti.size() - 1]


# ---------------------------------------------------------------------
# LA LISTA DEI PASSI
# Ogni passo e' un Dictionary (come un record di Pascal):
#   titolo      = titolo mostrato
#   testo       = spiegazione (frasi corte)
#   mosse       = lista dei pacchetti da far viaggiare
# ---------------------------------------------------------------------
func costruisci_passi() -> void:
	var https := (schema == "https")
	passi = []

	# 1 - CACHE DEL BROWSER
	passi.append({
		"titolo": "Passo 1 di 8 - La cache del browser",
		"testo": "Hai scritto [b]%s[/b].\n\nPrima di tutto il browser guarda nella sua [b]cache[/b] (una memoria dove tiene le cose gia' viste).\n\nQuesta e' la prima volta: non c'e' niente. Bisogna partire per il viaggio." % (schema + "://" + dominio + percorso),
		"mosse": [mossa(PC, PC, "cerco in cache...", 1, COL_RICHIESTA, "cache vuota")],
	})

	# 2 - DNS (la rubrica di Internet)
	var mosse_dns: Array = []
	mosse_dns.append(mossa(PC, PC, "cache del sistema", 1, COL_RICHIESTA, "non lo so"))
	mosse_dns += tratta(PC, ROUTER, "IP di " + dominio + "?", 3, COL_RICHIESTA, "cache router: no")
	mosse_dns += tratta(ROUTER, DNS, "chi e' " + dominio + "?", 8, COL_RICHIESTA, "DNS ricorsivo")
	mosse_dns.append(mossa(DNS, DNS, "chiedo al ROOT", 15, COL_RICHIESTA, "root: vai dal ." + estensione()))
	mosse_dns.append(mossa(DNS, DNS, "chiedo al TLD ." + estensione(), 15, COL_RICHIESTA, "TLD: chiedi all'autorevole"))
	mosse_dns.append(mossa(DNS, DNS, "chiedo all'autorevole", 20, COL_RICHIESTA, "trovato: " + ip))
	mosse_dns += tratta(DNS, PC, "IP " + ip, 8, COL_RISPOSTA, "")
	passi.append({
		"titolo": "Passo 2 di 8 - Il DNS: la rubrica di Internet",
		"testo": "I computer usano i [b]numeri[/b] (indirizzi IP), non i nomi. Il [b]DNS[/b] e' la rubrica che trasforma il nome in numero.\n\n[b]1.[/b] Cache del sistema: non lo so.\n[b]2.[/b] Chiedo al router: non lo sa.\n[b]3.[/b] Il DNS ricorsivo fa il giro: [b]root[/b] (radice), poi [b]TLD[/b] (la fine, [b].%s[/b]), poi il server [b]autorevole[/b] di %s.\n[b]4.[/b] Risposta: [b]%s[/b] (un IP di esempio)." % [estensione(), dominio, ip],
		"mosse": mosse_dns,
	})

	# 3 - TCP in tre mosse
	var mosse_tcp: Array = []
	mosse_tcp += tratta(PC, SITO, "SYN", 12, COL_RICHIESTA, "")
	mosse_tcp += tratta(SITO, PC, "SYN-ACK", 12, COL_RISPOSTA, "")
	mosse_tcp += tratta(PC, SITO, "ACK", 12, COL_RICHIESTA, "connessione aperta")
	passi.append({
		"titolo": "Passo 3 di 8 - TCP: la stretta di mano",
		"testo": "Ora conosciamo il numero. Prima di parlare, i due computer si salutano in [b]tre mosse[/b] (si chiama [b]TCP[/b]):\n\n[b]1. SYN[/b] - il PC dice: \"Ci sei?\"\n[b]2. SYN-ACK[/b] - il server risponde: \"Ci sono! E tu?\"\n[b]3. ACK[/b] - il PC dice: \"Ci sono anch'io!\"\n\nOra la linea e' aperta.",
		"mosse": mosse_tcp,
	})

	# 4 - TLS (solo se https)
	if https:
		var mosse_tls: Array = []
		mosse_tls += tratta(PC, SITO, "ClientHello", 10, COL_RICHIESTA, "")
		mosse_tls += tratta(SITO, PC, "certificato", 10, COL_RISPOSTA, "")
		mosse_tls += tratta(PC, SITO, "chiave segreta", 10, COL_RICHIESTA, "")
		mosse_tls += tratta(SITO, PC, "pronti!", 8, COL_RISPOSTA, "")
		mosse_tls.append(mossa(PC, PC, "lucchetto chiuso", 1, COL_RISPOSTA, "LUCCHETTO CHIUSO"))
		passi.append({
			"titolo": "Passo 4 di 8 - TLS: il lucchetto",
			"testo": "L'indirizzo comincia con [b]https[/b]: la comunicazione viene [b]protetta[/b] (si chiama [b]TLS[/b]).\n\n[b]1.[/b] Il PC saluta e dice come vuole cifrare.\n[b]2.[/b] Il sito mostra il suo [b]certificato[/b] (la sua carta d'identita').\n[b]3.[/b] Il PC controlla che sia vera e manda una [b]chiave segreta[/b].\n[b]4.[/b] Da qui in poi tutto e' [b]cifrato[/b]: chi spia vede solo caratteri senza senso.\n\nEcco il [b]lucchetto[/b] nel browser.",
			"mosse": mosse_tls,
		})
	else:
		passi.append({
			"titolo": "Passo 4 di 8 - TLS: qui NON c'e'",
			"testo": "L'indirizzo comincia con [b]http[/b] (senza la s): [b]niente TLS[/b], niente lucchetto.\n\nI dati viaggiano in [b]chiaro[/b]: chi sta in mezzo alla rete puo' leggerli. Il browser avvisa \"Non sicuro\".\n\nProva a cambiare http in https e ricomincia: vedrai la differenza!",
			"mosse": [mossa(PC, PC, "niente lucchetto", 0, COL_RICHIESTA, "NON SICURO (http)")],
		})

	# 5 - Richiesta HTTP GET
	passi.append({
		"titolo": "Passo 5 di 8 - La richiesta HTTP",
		"testo": "Ora il browser chiede la pagina con una richiesta [b]HTTP[/b]:\n\n[b]GET %s[/b]\n[b]Host: %s[/b]\n\n\"GET\" vuol dire \"dammi\". \"Host\" dice a quale sito ci rivolgiamo (un server puo' ospitare tanti siti)." % [percorso, dominio],
		"mosse": tratta(PC, SITO, "GET " + percorso, 14, COL_RICHIESTA, "elaboro la richiesta"),
	})

	# 6 - Risposta HTTP 200
	passi.append({
		"titolo": "Passo 6 di 8 - La risposta: 200 OK",
		"testo": "Il server risponde con un numero: [b]200 OK[/b] = \"tutto bene, eccola\".\n\nDentro la risposta c'e' il testo della pagina, scritto in [b]HTML[/b].\n\nAltri numeri famosi: [b]404[/b] = pagina non trovata, [b]500[/b] = il server ha un guasto.",
		"mosse": tratta(SITO, PC, "200 OK + HTML", 40, COL_RISPOSTA, "pagina spedita"),
	})

	# 7 - Il browser disegna la pagina
	passi.append({
		"titolo": "Passo 7 di 8 - Il browser disegna la pagina",
		"testo": "Il browser legge l'HTML e disegna: titoli, testi, immagini.\n\nSe nella pagina ci sono immagini o stili, ripete il viaggio per prenderli (altre richieste GET).\n\nFinalmente vedi [b]%s[/b] sullo schermo!" % dominio,
		"mosse": [mossa(PC, PC, "disegno la pagina", 60, COL_RISPOSTA, "PAGINA: " + dominio)],
	})

	# 8 - Riepilogo (il testo dei millisecondi si completa a fine passo)
	passi.append({
		"titolo": "Passo 8 di 8 - Riepilogo",
		"testo": "",
		"mosse": [],
	})


# Crea una "mossa": un pacchetto che va da un nodo a un altro.
# (e' un Dictionary, come un record: da, a, etichetta, ms, colore, stato)
func mossa(da: int, a: int, etichetta: String, ms: int, colore: Color, stato: String) -> Dictionary:
	return {"da": da, "a": a, "etichetta": etichetta, "ms": ms, "colore": colore, "stato": stato}


# Tutto passa dal router: se PC e SITO si parlano, il pacchetto fa
# due salti (PC -> router -> sito). Questa funzione crea i salti.
func tratta(da: int, a: int, etichetta: String, ms: int, colore: Color, stato: String) -> Array:
	if da == ROUTER or a == ROUTER:
		return [mossa(da, a, etichetta, ms, colore, stato)]
	var meta := int(ms / 2)
	return [
		mossa(da, ROUTER, etichetta, meta, colore, ""),
		mossa(ROUTER, a, etichetta, ms - meta, colore, stato),
	]


# ---------------------------------------------------------------------
# L'ANIMAZIONE: eseguo tutte le mosse del passo, una dopo l'altra
# ---------------------------------------------------------------------
func esegui_passo() -> void:
	var p: Dictionary = passi[passo_attuale]
	lbl_titolo.text = p["titolo"]
	if passo_attuale == passi.size() - 1:
		spiegazione.text = riepilogo()
	else:
		spiegazione.text = p["testo"]
	occupato = true
	aggiorna_bottoni()

	# Il Tween e' una "catena di azioni" che Godot esegue da solo nel tempo.
	tween = create_tween()
	for m in p["mosse"]:
		tween.tween_callback(inizio_mossa.bind(m))
		if m["da"] == m["a"]:
			tween.tween_interval(1.0)                      # pacchetto fermo: aspetto
		else:
			var fine: Vector2 = centro(m["a"]) - pacchetto.size / 2
			tween.tween_property(pacchetto, "position", fine, 0.9)
		tween.tween_callback(fine_mossa.bind(m))
	tween.tween_callback(fine_passo)


# Centro di un nodo (serve per sapere dove mettere il pacchetto).
func centro(i: int) -> Vector2:
	var n: Control = nodi[i]
	return n.position + n.size / 2


func inizio_mossa(m: Dictionary) -> void:
	lbl_ora.text = "Ora: " + m["etichetta"]
	pacchetto.color = m["colore"]
	pacchetto.get_node("Testo").text = m["etichetta"]
	pacchetto.position = centro(m["da"]) - pacchetto.size / 2
	pacchetto.visible = true
	if m["da"] == m["a"]:
		# Il nodo "lampeggia" per far capire che sta lavorando.
		var lamp := create_tween()
		lamp.tween_property(nodi[m["a"]], "modulate", Color(1.6, 1.6, 0.8), 0.3)
		lamp.tween_property(nodi[m["a"]], "modulate", Color.WHITE, 0.3)


func fine_mossa(m: Dictionary) -> void:
	pacchetto.visible = false
	ms_totali += m["ms"]
	# Il contatore sale piano piano fino al nuovo valore.
	var conta := create_tween()
	conta.tween_method(mostra_ms, ms_mostrati, float(ms_totali), 0.4)
	ms_mostrati = ms_totali
	if m["stato"] != "":
		scrivi_nodo(m["a"], m["stato"])


func fine_passo() -> void:
	occupato = false
	aggiorna_bottoni()
	if passo_attuale < passi.size() - 1:
		lbl_ora.text = "Premi Avanti per il passo successivo."
	else:
		lbl_ora.text = "Finito! Cambia l'indirizzo e premi Ricomincia + Avvia."


# Scrive il contatore dei millisecondi.
func mostra_ms(valore: float) -> void:
	lbl_ms.text = "Tempo: %d ms" % int(valore)


# Scrive nome + stato dentro il nodo (come Label.Caption).
func scrivi_nodo(i: int, stato: String) -> void:
	var testo: String = NOMI[i]
	if i == SITO and dominio != "":
		testo += "\n" + dominio
	if stato != "":
		testo += "\n[" + stato + "]"
	nodi[i].get_node("Testo").text = testo


func riepilogo() -> String:
	var lucchetto := "SI' (https)" if schema == "https" else "NO (http)"
	var t := "Ecco il viaggio completo di [b]%s[/b]:\n\n" % (schema + "://" + dominio + percorso)
	t += "[b]1.[/b] Cache del browser: vuota\n"
	t += "[b]2.[/b] DNS: %s = %s\n" % [dominio, ip]
	t += "[b]3.[/b] TCP: SYN, SYN-ACK, ACK\n"
	t += "[b]4.[/b] TLS (lucchetto): %s\n" % lucchetto
	t += "[b]5.[/b] GET %s\n" % percorso
	t += "[b]6.[/b] 200 OK + HTML\n"
	t += "[b]7.[/b] Pagina disegnata\n\n"
	t += "Tempo (di esempio): circa [b]%d ms[/b]. Meno di un battito di ciglia!" % ms_totali
	return t
