extends Node2D
## IL TRENO BLINDATO — base del prof. Nicola Regge — versione 1.0, su Godot 4.7
##
## Da dove viene: è il gioco della classe 2INF (versione HTML 0.31, «Gli uccelli nel cielo»)
## rifatto con il motore Godot. È cambiato il motore, una cosa grossa: per questo la versione
## è 1.0 (versione «major»). Da questa base ogni classe parte con un suo ramo.
##
## Ponte da Lazarus:
##   Lazarus REAGISCE: il programma aspetta un clic (Button1Click) e poi risponde.
##   Godot PULSA: _process(delta) gira da solo circa 60 volte al secondo e muove tutto.
##   I «pennelli» (le funzioni disegna_...) ridipingono la scena a ogni giro.
##
## I pezzi della classe stanno nella cartella dati/ in file .json (come nella versione HTML):
##   regole.json, percorso.json, protagonista.json, testi.json, suoni.json, facce.json,
##   ambienti/*.json, cattivi/pc01.json ... pc40.json, img/personaggi/personaggi.json
## Si cambia il gioco cambiando i dati, senza toccare questo codice.
## Un file con un errore non blocca il gioco: viene segnalato nella schermata iniziale.

const Memoria = preload("res://memoria.gd")
const Strato = preload("res://strato.gd")
const Suoni = preload("res://suoni.gd")
const Schermate = preload("res://schermate.gd")

const DATI := "res://dati/"
const ZF := 18.0   # distanza più lontana che si vede (l'orizzonte)
const ZN := 1.0    # distanza più vicina (il vetro della cabina)
const MISURE := {"alberi": [2.0, 4.5], "case": [3.4, 2.8], "palazzi": [3.4, 8.0], "rocce": [3.0, 1.9], "onde": [3.0, 0.5]}
const CASUALI := ["#8be04e", "#ff6fb1", "#6fd3ff", "#ffb347", "#b48cff", "#ff5e57"]
const ORO := Color("#ffd34d")

# ---------- valori di partenza (se un file manca o ha un errore, si usano questi) ----------
var R := {"vetro": 5, "velocita_treno": 1.0, "secondi_prima_di_sparare": 2.2, "cattivi_per_livello": 10, "punti_per_cattivo": 10}
var PERC := {"ambienti": ["bosco", "case", "citta", "montagna", "mare"], "secondi_per_ambiente": 20.0}
var AMB_BASE := {
	"bosco": {"nome": "Bosco", "cielo_alto": "#7ec8f0", "cielo_basso": "#cfeefc", "lontano": "#4f8a5b", "terra": "#3e7a3a", "oggetti": "alberi", "colore_oggetti": "#2d6b34", "densita": 3, "rottami": false},
	"case": {"nome": "Paese", "cielo_alto": "#f6b36b", "cielo_basso": "#fde3b8", "lontano": "#9a8a7a", "terra": "#8fae5a", "oggetti": "case", "colore_oggetti": "#d9734e", "densita": 2, "rottami": false},
	"citta": {"nome": "Città", "cielo_alto": "#1b2350", "cielo_basso": "#5a3a6e", "lontano": "#2a2f66", "terra": "#2b2b33", "oggetti": "palazzi", "colore_oggetti": "#3d4580", "densita": 3, "rottami": false},
	"montagna": {"nome": "Montagna", "cielo_alto": "#5aa0e0", "cielo_basso": "#dceefa", "lontano": "#8c97a8", "terra": "#6d7d52", "oggetti": "rocce", "colore_oggetti": "#7d7468", "densita": 2, "rottami": false},
	"mare": {"nome": "Mare", "cielo_alto": "#3fa9e8", "cielo_basso": "#bfe8ff", "lontano": "#2b7fb8", "terra": "#e8d49a", "oggetti": "onde", "colore_oggetti": "#1f6ea8", "densita": 2, "rottami": false}}
var AMB := {}
var PROT := {"nome": "Il macchinista", "giacca": "#1f6fa5", "capelli": "#2b1a10"}
var TX := {"titolo": "IL TRENO BLINDATO", "sottotitolo": "Il treno attraversa boschi, paesi e montagne. I cattivi saltano fuori da dietro alberi e case: toccali prima che sparino. Il vetro regge {vetro} colpi!",
	"fine": "IL VETRO È ANDATO IN PEZZI!", "record": "NUOVO RECORD!", "livello": "LIVELLO", "frasi": [],
	"lodi": ["Grande! Hai portato il treno in salvo.", "Che riflessi, macchinista!", "I cattivi non ti fermano: riparti?"]}
var SU := {"volume": 0.6, "note_vittoria": [392, 523, 659, 784]}
var VERSIONE := {"versione": "1.0", "nome": "base del prof · su Godot", "titolo": "Il treno blindato — base del prof. Nicola Regge"}
var CATTIVI := []      # i cattivi della classe (cattivi/pcNN.json)
var ERRORI := []       # i file da sistemare
var SQUADRE := []      # chi ha fatto cosa (campo «autori» dei file)
var FACCE := []        # le facce scelte su questo dispositivo (Facce della classe)
var FACCE_WEB := []    # le facce della classe pubblicate nel gioco (facce.json)
var PERSONAGGI := []   # la galleria «I personaggi»
var RECORD_CLASSE := []
var COPERTINA: Texture2D = null

# ---------- lo stato ----------
var S = null           # la partita in corso (null = nessuna partita)
var DEMO = null        # il treno che corre dietro ai menu
var PAUSA := false
var COCCI := []        # i pezzi di vetro che cadono
var CONF := []         # i coriandoli
var UCC := []          # gli uccelli nel cielo
var GOCCE := []        # la pioggia
var W := 1280.0
var H := 720.0
var partita_n := 0     # numero della partita (serve ai «timer» per non sbagliare partita)
var alfa := 1.0        # trasparenza del cattivo che cade
var MIMETICA: ImageTexture
var MIRINO: Image
var FONT := {}

var mem := Memoria.new()
var suoni: Node
var ui: CanvasLayer
var strato_finestra: Control   # il vetro: tutto quello che c'è fuori si vede solo qui dentro
var strato_paesaggio: Node2D
var strato_cabina: Node2D
var strato_sopra: Node2D
var prova := false     # modalità di controllo automatico (indirizzo con ?prova)
var prova_t := 0.0


func _ready() -> void:
	randomize()
	if OS.has_feature("web"):
		# nel browser 1 punto del gioco = 1 pixel CSS (come la versione HTML), anche sui telefoni
		get_window().content_scale_factor = max(1.0, DisplayServer.screen_get_scale())
		prova = str(JavaScriptBridge.eval("location.search", true)).contains("prova")
	if "prova" in OS.get_cmdline_user_args():
		prova = true   # controllo automatico dal terminale: godot --headless -- prova
	AMB = AMB_BASE.duplicate(true)
	carica_tutto()
	prepara_disegno()
	suoni = Suoni.new()
	add_child(suoni)
	suoni.prepara(SU.volume, SU.note_vittoria)
	ui = Schermate.new()
	ui.gioco = self
	add_child(ui)
	carica_facce()
	DEMO = nuova_scena()
	rs()
	ui.prepara_schermate()


func rs() -> void:
	var s := get_viewport_rect().size
	W = s.x
	H = s.y


# =====================================================================
#   I DATI DELLA CLASSE (letti dai file .json)
# =====================================================================
func num(v, mi: float, ma: float, def: float) -> float:
	if v is int or v is float:
		return clamp(float(v), mi, ma)
	if v is String and v.is_valid_float():
		return clamp(v.to_float(), mi, ma)
	return def


func colore(v, def: String) -> String:
	var re := RegEx.create_from_string("^#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$")
	return v if v is String and re.search(v) != null else def


## Legge un file .json. Se non c'è: null (non è un errore). Se è scritto male: lo segna in ERRORI.
func leggi_json(nome: String):
	var percorso := DATI + nome
	if not FileAccess.file_exists(percorso):
		return null
	var testo := FileAccess.get_file_as_string(percorso)
	# una virgola in più prima di } o ] è un errore per il browser (la versione HTML non legge il file): lo segnaliamo anche qui
	var virgola := RegEx.create_from_string(",\\s*[}\\]]").search(testo)
	if virgola != null:
		ERRORI.append(nome + ": errore di scrittura (una virgola in più prima di } o ]) alla riga %d" % (testo.substr(0, virgola.get_start()).count("\n") + 1))
		return null
	var j := JSON.new()
	if j.parse(testo) != OK:
		ERRORI.append(nome + ": errore di scrittura (una virgola o una virgoletta?) alla riga %d" % j.get_error_line())
		return null
	if not j.data is Dictionary:
		ERRORI.append(nome + ": il file deve iniziare con { e finire con }")
		return null
	return j.data


func segna(sq: String, aut) -> void:
	var lista := []
	if aut is Array:
		for a in aut.slice(0, 8):
			lista.append(str(a))
	SQUADRE.append({"sq": sq, "aut": lista})


func immagine(percorso: String) -> Texture2D:
	if ResourceLoader.exists(percorso):
		var t = load(percorso)
		if t is Texture2D:
			return t
	return null


func carica_tutto() -> void:
	var d = leggi_json("versione.json")
	if d:
		for k in ["versione", "nome", "titolo"]:
			if d.get(k) is String:
				VERSIONE[k] = d[k]
	d = leggi_json("regole.json")
	if d:
		R.vetro = int(num(d.get("vetro"), 1, 12, R.vetro))
		R.velocita_treno = num(d.get("velocita_treno"), 0.5, 3, R.velocita_treno)
		R.secondi_prima_di_sparare = num(d.get("secondi_prima_di_sparare"), 0.8, 5, R.secondi_prima_di_sparare)
		R.cattivi_per_livello = int(num(d.get("cattivi_per_livello"), 3, 50, R.cattivi_per_livello))
		R.punti_per_cattivo = int(num(d.get("punti_per_cattivo"), 1, 1000, R.punti_per_cattivo))
		segna("Squadra PERCORSO e REGOLE", d.get("autori"))
	d = leggi_json("percorso.json")
	if d:
		if d.get("ambienti") is Array:
			var a := []
			for x in d.ambienti:
				if x is String and AMB_BASE.has(x):
					a.append(x)
			if a.size() > 0:
				PERC.ambienti = a
		PERC.secondi_per_ambiente = num(d.get("secondi_per_ambiente"), 5, 120, PERC.secondi_per_ambiente)
	d = leggi_json("protagonista.json")
	if d:
		if d.get("nome") is String and d.nome.strip_edges() != "":
			PROT.nome = d.nome.substr(0, 24)
		PROT.giacca = colore(d.get("giacca"), PROT.giacca)
		PROT.capelli = colore(d.get("capelli"), PROT.capelli)
		segna("Squadra PROTAGONISTA e TESTI", d.get("autori"))
	d = leggi_json("testi.json")
	if d:
		for k in ["titolo", "sottotitolo", "fine", "record", "livello"]:
			if d.get(k) is String and d[k].strip_edges() != "":
				TX[k] = d[k].substr(0, 160)
		if d.get("frasi_cattivi") is Array:
			TX.frasi = d.frasi_cattivi.filter(func(x): return x is String).map(func(x): return x.substr(0, 40))
		if d.get("lodi") is Array and d.lodi.size() > 0:
			TX.lodi = d.lodi.filter(func(x): return x is String).map(func(x): return x.substr(0, 120))
	TX.sottotitolo = TX.sottotitolo.replace("{vetro}", str(R.vetro))
	d = leggi_json("facce.json")
	if d and d.get("facce") is Array:
		var armi = d.get("armi", {})
		var re := RegEx.create_from_string("^[a-z0-9-]+\\.(jpg|png)$")
		for n in d.facce.slice(0, 40):
			if not (n is String and re.search(n.to_lower())):
				continue
			var t := immagine(DATI + "facce/" + n)
			if t:
				FACCE_WEB.append({"tex": t, "arma": "ak" if armi is Dictionary and armi.get(n) == "ak" else ""})
			else:
				ERRORI.append("facce/" + n + ": immagine non trovata")
	d = leggi_json("suoni.json")
	if d:
		SU.volume = num(d.get("volume"), 0, 1, SU.volume)
		if d.get("note_vittoria") is Array and d.note_vittoria.size() > 0:
			SU.note_vittoria = d.note_vittoria.slice(0, 8).map(func(f): return num(f, 80, 3000, 440))
		segna("Squadra SUONI", d.get("autori"))
	for k in AMB_BASE:
		d = leggi_json("ambienti/" + k + ".json")
		if not d:
			continue
		var a: Dictionary = AMB[k]
		if d.get("nome") is String and d.nome.strip_edges() != "":
			a.nome = d.nome.substr(0, 20)
		for c in ["cielo_alto", "cielo_basso", "lontano", "terra", "colore_oggetti"]:
			a[c] = colore(d.get(c), a[c])
		if d.get("oggetti") in ["alberi", "case", "palazzi", "rocce", "onde"]:
			a.oggetti = d.oggetti
		a.densita = int(num(d.get("densita"), 1, 3, a.densita))
		a.rottami = d.get("rottami") == true
		segna("Ambiente " + a.nome, d.get("autori"))
	# un cattivo per ogni PC: cattivi/pc01.json ... pc40.json
	for n in range(1, 41):
		var pc := "pc%02d" % n
		d = leggi_json("cattivi/" + pc + ".json")
		if not d:
			continue
		var c := {"pc": n, "nome": str(d.get("nome", "Senza nome")).substr(0, 24), "colore": colore(d.get("colore"), "#8be04e"),
			"occhi": int(num(d.get("occhi"), 1, 3, 2)), "cappello": int(num(d.get("cappello"), 0, 2, 0)), "bocca": int(num(d.get("bocca"), 0, 2, 0)),
			"velocita": int(num(d.get("velocita"), 1, 3, 1)), "frase": str(d.get("frase", "")).substr(0, 40), "img": null, "arma": ""}
		if d.get("immagine") == true:
			c.img = immagine(DATI + "cattivi/" + pc + ".png")
			if c.img == null:
				ERRORI.append(pc + ".png: immagine non trovata")
		CATTIVI.append(c)
	# la galleria dei personaggi e il record della classe
	d = leggi_json("img/personaggi/personaggi.json")
	if d and d.get("personaggi") is Array:
		var re := RegEx.create_from_string("^[a-z0-9-]+\\.(jpg|png)$")
		for p in d.personaggi:
			if p is Dictionary and p.get("file") is String and re.search(p.file.to_lower()):
				PERSONAGGI.append({"tex": immagine(DATI + "img/personaggi/" + p.file), "nome": str(p.get("nome", "")), "ruolo": str(p.get("ruolo", ""))})
	d = leggi_json("record-classe.json")
	if d and d.get("record") is Array:
		for x in d.record.slice(0, 10):
			if x is Dictionary and x.get("squadra") is String and (x.get("punti") is int or x.get("punti") is float):
				RECORD_CLASSE.append({"squadra": x.squadra, "punti": int(x.punti)})
	COPERTINA = immagine(DATI + "img/copertina.jpg")


## Facce della classe scelte su questo dispositivo (restano solo qui, mai in rete).
func carica_facce() -> void:
	FACCE.clear()
	for u in mem.foto():
		if u is String:
			var t := mem.texture_da_dataurl(u)
			if t:
				FACCE.append({"tex": t, "arma": ""})


func tutte_facce() -> Array:
	return FACCE + FACCE_WEB


# =====================================================================
#   LA CABINA: si guarda AVANTI lungo i binari (progetto della 2INF: lavagna dell'08/10)
# =====================================================================
func finestra() -> Rect2:
	var m: float = max(10.0, min(W, H) * 0.03)
	return Rect2(m, 36.0, W - 2.0 * m, H * 0.72 - 36.0)


func vista() -> Dictionary:
	var f := finestra()
	# k = quanto sono grandi le cose. v1.0: sul telefono in verticale si usa l'altezza del vetro, così i cattivi non sono minuscoli
	return {"f": f, "hz": f.position.y + f.size.y * 0.42, "bot": f.end.y, "vx": W / 2.0, "k": max(f.size.x, f.size.y) * 0.16}


## Prospettiva: una cosa a distanza z sembra grande 1/z. X = quanto è a destra o a sinistra dei binari.
## Restituisce x, y sullo schermo e u = quanto è grande «1 metro» a quella distanza.
func proj(V: Dictionary, X: float, z: float) -> Vector3:
	var s := ZN / z
	return Vector3(V.vx + X * V.k * s, V.hz + (V.bot - V.hz) * s, V.k * s)


# =====================================================================
#   IL GIOCO
# =====================================================================
func nuova_scena() -> Dictionary:
	var s := {"t": 0.0, "punti": 0, "abbattuti": 0, "livello": 1, "combo": 0, "vetro": R.vetro, "vetroMax": R.vetro, "colpi_presi": 0,
		"crepe": [], "cattivi": [], "part": [], "testi": [], "prossimo": 1.6, "scossa": 0.0, "flash": 0.0, "flashRosso": 0.0, "fine": false,
		"km": 0.0, "amb": 0, "ambT": 0.0, "oggetti": [], "dist": 0.0, "prossimoOgg": 0.0, "ritmo": 0.0,
		"spari": 0, "sfera": null, "sferaT": 0.0, "x2": 0.0, "sx": 0.0, "sy": 0.0}
	var z := ZF
	while z > 2.0:
		s.oggetti.append(nuovo_oggetto(s, z))
		z -= 1.3
	return s


func nuova_partita() -> void:
	partita_n += 1
	S = nuova_scena()
	annuncia_ambiente()


func ambiente(s = null) -> Dictionary:
	if s == null:
		s = S
	return AMB[PERC.ambienti[s.amb % PERC.ambienti.size()]]


func annuncia_ambiente() -> void:
	if S == null:
		return
	S.testi.append({"x": W / 2.0, "y": H * 0.22, "s": ambiente().nome.to_upper(), "t": 0.0, "big": true, "fumetto": false})
	suoni.suona("fischio")


func rnd(a: float, b: float) -> float:
	return randf_range(a, b)


func nuovo_oggetto(s: Dictionary, z: float) -> Dictionary:
	var a := ambiente(s)
	var lato := -1.0 if randf() < 0.5 else 1.0
	var tipo: String = a.oggetti
	var m: Array = MISURE[tipo]
	if a.rottami and randf() < 0.3:
		return {"X": lato * rnd(1.7, 2.6), "z": z, "tipo": "rottame", "col": Color("#5b5f66"), "w": rnd(1.2, 1.8), "h": rnd(0.6, 0.9), "lato": lato, "fumo": rnd(0, 6), "cattivo": false}
	if randf() < 0.18:
		return {"X": lato * rnd(1.6, 1.9), "z": z, "tipo": "barile", "col": Color("#8a4b2a"), "w": 0.7, "h": 1.0, "lato": lato, "cattivo": false}
	return {"X": lato * rnd(2.2, 4.6), "z": z, "tipo": tipo, "col": Color(a.colore_oggetti), "w": m[0] * rnd(0.8, 1.2), "h": m[1] * rnd(0.8, 1.25), "lato": lato,
		"tetto": [Color("#8a2f22"), Color("#6b3a24"), Color("#a0432c")].pick_random(), "cattivo": false}


func nuovo_cattivo() -> void:
	# v0.17 (PR di Luca B.): i cattivi nascono più lontano, non troppo vicino
	var cand: Array = S.oggetti.filter(func(o): return o.z > 5 and o.z < 9 and o.tipo != "onde" and not o.cattivo)
	var base: Dictionary
	if CATTIVI.size() > 0:
		base = CATTIVI.pick_random()
	else:
		base = {"nome": "", "colore": CASUALI.pick_random(), "occhi": randi_range(1, 3), "cappello": randi_range(0, 2), "bocca": randi_range(0, 2), "velocita": 1, "frase": "", "img": null, "arma": ""}
	var fc := tutte_facce()
	if fc.size() > 0 and randf() < 0.65:
		var f: Dictionary = fc.pick_random()
		base = base.duplicate()
		base.img = f.tex
		base.arma = f.arma
	var o
	if cand.size() > 0:
		o = cand.pick_random()
	else:
		o = nuovo_oggetto(S, rnd(6, 8))
		o.tipo = "barile"
		o.X = [-1.0, 1.0].pick_random() * 1.7
		o.w = 0.7
		o.h = 1.0
		o.col = Color("#8a4b2a")
		S.oggetti.append(o)
	# v0.4 (audit degli investitori): il personaggio intero è NASCOSTO dietro l'oggetto e scivola fuori di lato, verso i binari
	var dx: float = -o.lato * (o.w * 0.5 + 0.62)
	# v0.15 (PR di Antonio M.): la difficoltà cresce di più a ogni livello
	var tempo: float = max(0.75, (R.secondi_prima_di_sparare - (S.livello - 1) * 0.3) / (1.0 + (base.velocita - 1) * 0.2))
	o.cattivo = true
	S.cattivi.append({"o": o, "dx": dx, "t": 0.0, "entra": 0.75, "tempo": tempo, "b": base, "fase": "entra", "morto": 0.0,
		"x": 0.0, "y": 0.0, "r": 10.0, "u": 10.0, "piedi": 0.0, "k": 0.0, "preciso": false})


func colpito(c: Dictionary) -> void:
	c.fase = "colpito"
	c.morto = 0.0
	S.abbattuti += 1
	S.combo += 1
	# v0.24 (PR di Luciano C.): più vai avanti, più punti vale ogni cattivo (+50% a ogni livello)
	var p: int = roundi(R.punti_per_cattivo * (1.0 + (S.livello - 1) * 0.5)) + min(40, S.combo * 2)
	if S.x2 > 0:
		p *= 2
	S.punti += p
	suoni.suona("pop")
	S.testi.append({"x": c.x, "y": c.y - c.r, "s": "+%d%s" % [p, (" COMBO x%d" % S.combo) if S.combo > 2 else ""], "t": 0.0, "big": false, "fumetto": false})
	# v0.18 (PR di Ney V. ed Egor M.): BANG! e lampo rosso
	S.testi.append({"x": c.x, "y": c.y - c.r * 2.6, "s": "BANG!", "t": 0.0, "big": true, "fumetto": false})
	# v0.25 (PR di Giorgio A.): colpo preciso in testa = 50 punti bonus
	if c.preciso:
		S.punti += 50
		S.testi.append({"x": c.x, "y": c.y - c.r * 4, "s": "COLPO PRECISO +50", "t": 0.0, "big": false, "fumetto": false})
	S.flashRosso = 0.12
	for i in 22:
		var a := rnd(0, 7)
		var v := rnd(80, 380)
		S.part.append({"x": c.x, "y": c.y, "vx": cos(a) * v, "vy": sin(a) * v, "t": 0.0, "c": Color("#3a3a3a") if i % 3 != 0 else Color("#ffcc33"), "r": rnd(2, 6), "mira": false})
	if S.abbattuti % R.cattivi_per_livello == 0:
		S.livello += 1
		# v0.13 (PR di Ney V. e Alejandro G.): nuovo livello = nuovo scenario
		S.amb += 1
		S.ambT = 0.0
		dopo(0.7, annuncia_ambiente)
		suoni.suona("vittoria")
		S.testi.append({"x": W / 2.0, "y": H * 0.32, "s": "%s %d!" % [TX.livello, S.livello], "t": 0.0, "big": true, "fumetto": false})
		coriandoli(60)


## Il cattivo spara: il vetro si crepa.
func spara(c: Dictionary) -> void:
	c.fase = "spara"
	c.morto = 0.0
	S.combo = 0
	suoni.suona("sparo")
	S.flash = 0.18
	S.scossa = 0.35
	S.vetro -= 1
	S.colpi_presi += 1
	var fr: String = c.b.frase
	if fr == "" and TX.frasi.size() > 0:
		fr = TX.frasi.pick_random()
	if fr != "":
		S.testi.append({"x": c.x, "y": c.y - c.r - 10, "s": "«" + fr + "»", "t": 0.0, "big": false, "fumetto": true})
	S.crepe.append(crea_crepa(S.colpi_presi, S.vetroMax + 1))
	dopo(0.09, func(): suoni.suona("crepa"))
	# v0.14 (PR di Egor M.): quando il vetro si spacca non si muore subito, c'è ancora 1 colpo da incassare
	if S.vetro == 0:
		S.testi.append({"x": W / 2.0, "y": H * 0.3, "s": "VETRO ROTTO! ULTIMO COLPO!", "t": 0.0, "big": true, "fumetto": false})
		suoni.suona("rotto")
	if S.vetro < 0:
		S.vetro = 0
		S.fine = true
		dopo(0.25, func():
			suoni.suona("rotto")
			frantuma())
		dopo(1.7, fine)


## Fa una cosa tra qualche secondo (come setTimeout in JavaScript), solo se la partita è ancora la stessa.
func dopo(secondi: float, cosa: Callable) -> void:
	var n := partita_n
	get_tree().create_timer(secondi).timeout.connect(func():
		if n == partita_n:
			cosa.call())


## v1.0 (richiesta del prof): il vetro si crepa DAL BORDO VERSO IL CENTRO.
## Il primo colpo crepa un angolo; ogni colpo dopo arriva un po' più vicino al centro,
## così il centro del finestrino resta pulito il più a lungo possibile.
## n = numero del colpo (1, 2, 3...), totale = quanti colpi regge il vetro (+ l'ultimo colpo).
func crea_crepa(n: int, totale: int) -> Dictionary:
	var f := finestra()
	var c := f.get_center()
	var hw := f.size.x / 2.0
	var hh := f.size.y / 2.0
	var p := 0.0 if totale <= 1 else float(n - 1) / float(totale - 1)   # 0 = primo colpo, 1 = ultimo
	var rho: float = lerp(0.97, 0.25, pow(p, 1.5))   # quanto è lontano dal centro (1 = sul bordo): si avvicina piano, poi più in fretta
	# l'angolo: i primi 4 colpi negli angoli, poi lontano dalle crepe già fatte
	var usati: Array = S.crepe.map(func(k): return k.ang)
	var angoli_vetro := [atan2(-hh, -hw), atan2(-hh, hw), atan2(hh, hw), atan2(hh, -hw)]
	var migliore := 0.0
	var distanza := -1.0
	for prova_n in 16:
		var a: float = (angoli_vetro.pick_random() + rnd(-0.1, 0.1)) if n <= 4 else rnd(-PI, PI)
		var md := 10.0
		for u in usati:
			md = min(md, abs(angle_difference(a, u)))
		if md > distanza:
			distanza = md
			migliore = a
	var d := Vector2(cos(migliore), sin(migliore))
	var t: float = min(hw / max(0.001, abs(d.x)), hh / max(0.001, abs(d.y)))
	var bordo := c + d * t
	var punto := c + d * t * rho
	punto.x = clamp(punto.x, f.position.x + 8, f.end.x - 8)
	punto.y = clamp(punto.y, f.position.y + 8, f.end.y - 8)
	var dentro := (c - punto).normalized()
	var lungo: float = max(f.size.x, f.size.y) * lerp(0.08, 0.16, p)
	var linee := []
	var rami := []
	var nl := randi_range(8, 12)
	for i in nl:
		var a := float(i) / nl * TAU + rnd(-0.2, 0.2)
		var verso := Vector2(cos(a), sin(a)).dot(dentro)   # > 0: la crepa andrebbe verso il centro
		var l: float = lungo * rnd(0.6, 1.2) * (1.0 - 0.75 * max(0.0, verso))
		var q := punto
		var seg := PackedVector2Array([q])
		for j in 6:
			a += rnd(-0.35, 0.35)
			q += Vector2(cos(a), sin(a)) * l / 6.0
			seg.append(q)
			if j == 2 and randf() < 0.6:
				# un ramo piccolo che parte da metà crepa
				var ar: float = a + [-0.7, 0.7].pick_random()
				var qr := q
				var sr := PackedVector2Array([qr])
				for k in 3:
					ar += rnd(-0.3, 0.3)
					qr += Vector2(cos(ar), sin(ar)) * l * 0.12
					sr.append(qr)
				rami.append(sr)
		linee.append(seg)
	var anelli := []
	for k in range(1, 4):
		anelli.append(rnd(6, 11) * k * lerp(0.8, 1.3, p))
	# schegge: piccoli pezzi saltati via vicino alla cornice (solo per i colpi vicino al bordo)
	var schegge := []
	if rho > 0.6:
		var lungo_bordo := Vector2(-d.y, d.x)
		for k in randi_range(3, 5):
			var b := bordo + lungo_bordo * rnd(-26, 26) + dentro * rnd(0, 6)
			var s := rnd(3, 8)
			var r0 := rnd(0, TAU)
			schegge.append(PackedVector2Array([b + Vector2(cos(r0), sin(r0)) * s, b + Vector2(cos(r0 + 2.2), sin(r0 + 2.2)) * s * 0.8, b + Vector2(cos(r0 + 4.1), sin(r0 + 4.1)) * s * 0.6]))
	return {"x": punto.x, "y": punto.y, "ang": migliore, "linee": linee, "rami": rami, "anelli": anelli, "schegge": schegge}


func frantuma() -> void:
	var f := finestra()
	for i in 70:
		COCCI.append({"x": rnd(f.position.x, f.end.x), "y": rnd(f.position.y, f.end.y), "vx": rnd(-120, 120), "vy": rnd(-200, 50), "r": rnd(0, 6), "vr": rnd(-4, 4), "s": rnd(20, 70)})


func coriandoli(n: int) -> void:
	var colori := [ORO, Color("#2f9e57"), Color("#e0413a"), Color("#1f6fa5"), Color("#ff6fb1"), Color.WHITE]
	for i in n:
		CONF.append({"x": rnd(0, W), "y": -10.0, "vx": rnd(-60, 60), "vy": rnd(120, 300), "r": rnd(0, 6), "vr": rnd(-6, 6), "c": colori.pick_random()})


func fine() -> void:
	if S == null:
		return
	ui.fine_partita(S)
	S = null


func parti() -> void:
	nuova_partita()
	ui.mostra("")


# ---------------- il tocco / il clic (qui il gioco «reagisce», come in Lazarus) ----------------
func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventScreenTouch and event.pressed:
		tocca(event.position)
	elif event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT and event.device != InputEvent.DEVICE_ID_EMULATION:
		tocca(event.position)
	elif event is InputEventKey and event.pressed and not event.echo:
		if (event.keycode == KEY_P or event.keycode == KEY_ESCAPE) and S != null and not S.fine:
			pausa()


func tocca(pos: Vector2) -> void:
	if S == null or S.fine or PAUSA or ui.sopra_un_bottone(pos):
		return
	get_viewport().set_input_as_handled()
	suoni.suona("colpo")
	S.spari += 1
	# v0.30 (PR di Francesco M.): la sfera d'oro dà punti x2 per 10 secondi
	if S.sfera != null and pos.distance_to(Vector2(S.sfera.x, S.sfera.y)) < 30:
		S.sfera = null
		S.x2 = 10.0
		S.testi.append({"x": pos.x, "y": pos.y, "s": "PUNTI x2!", "t": 0.0, "big": true, "fumetto": false})
		suoni.suona("vittoria")
		return
	S.part.append({"x": pos.x, "y": pos.y, "vx": 0.0, "vy": 0.0, "t": 0.0, "c": ORO, "r": 18.0, "mira": true})
	var best = null
	var bd := 1e9
	for c in S.cattivi:
		if c.fase != "entra" and c.fase != "attende":
			continue
		var d := pos.distance_to(Vector2(c.x, c.y))
		var nel_corpo: bool = abs(pos.x - c.x) < c.u * 0.38 and pos.y > c.y and pos.y < c.piedi
		# v1.0: almeno 22 punti di tolleranza intorno alla testa, perché sul telefono il dito è meno preciso del mouse
		if (d < max(c.r * 1.35, 22.0) or nel_corpo) and d < bd:
			bd = d
			best = c
	if best != null:
		best.preciso = bd < best.r * 0.8
		colpito(best)


# v0.23 (PR di Lina A.): il bottone Pausa (anche con il tasto P o Esc)
func pausa(v = null) -> void:
	PAUSA = (not PAUSA) if v == null else bool(v)
	ui.aggiorna_pausa(PAUSA)


# =====================================================================
#   IL «BATTITO»: gira circa 60 volte al secondo
# =====================================================================
func _process(delta: float) -> void:
	rs()
	var dt: float = min(0.05, delta)
	var gioca: bool = S != null and not S.fine
	ui.bottone_pausa(gioca)
	if not gioca and PAUSA:
		pausa(false)
	if PAUSA:
		dt = 0.0
	if S != null:
		if not S.fine:
			S.t += dt
			S.km += dt * R.velocita_treno * 0.4
			S.ambT += dt
			if S.ambT > PERC.secondi_per_ambiente:
				S.ambT = 0.0
				S.amb += 1
				annuncia_ambiente()
			S.prossimo -= dt
			if S.prossimo <= 0:
				nuovo_cattivo()
				if S.livello > 3 and randf() < 0.3:
					nuovo_cattivo()
				S.prossimo = max(0.45, 1.6 - (S.livello - 1) * 0.18) * rnd(0.7, 1.2)
		for c in S.cattivi.duplicate():
			c.t += dt
			if c.fase == "entra":
				if c.t >= c.entra:
					c.fase = "attende"
			elif c.fase == "attende":
				if S != null and not S.fine and (c.t > c.entra + c.tempo or c.o.z < 2.6):
					spara(c)
			else:
				c.morto += dt
		var via := func(c): return (c.fase == "colpito" and c.morto > 0.85) or (c.fase == "spara" and c.morto > 0.6) or c.o.z < ZN * 0.7
		for c in S.cattivi:
			if via.call(c):
				c.o.cattivo = false
		S.cattivi = S.cattivi.filter(func(c): return not via.call(c))
		# lo scossone quando il vetro viene colpito, e il dondolio del treno
		S.sx = rnd(-1, 1) * S.scossa * 28 if S.scossa > 0 else 0.0
		S.sy = (rnd(-1, 1) * S.scossa * 28 if S.scossa > 0 else 0.0) + sin(S.t * 18) * 1.2
		S.scossa = max(0.0, S.scossa - dt)
		muovi_paesaggio(S, dt, not S.fine)
		posiziona_cattivi()
		for p in S.part:
			p.t += dt
			p.x += p.vx * dt
			p.y += p.vy * dt
			p.vy += 600 * dt
		S.part = S.part.filter(func(p): return p.t < (0.25 if p.mira else 0.7))
		for t in S.testi:
			t.t += dt
		S.testi = S.testi.filter(func(t): return t.t < 1.4)
		# v0.30 (PR di Francesco M.): la sfera d'oro (rara) dà punti x2 per 10 secondi
		if not S.fine and not PAUSA:
			S.sferaT += dt
			if S.sfera == null and S.sferaT > 18 and randf() < dt * 0.08:
				var ff := finestra()
				S.sfera = {"x": ff.position.x + ff.size.x * (0.2 + randf() * 0.6), "y": ff.position.y + ff.size.y * (0.2 + randf() * 0.4), "t": 0.0}
				S.sferaT = 0.0
			if S.sfera != null:
				S.sfera.t += dt
				if S.sfera.t > 4:
					S.sfera = null
			if S.x2 > 0:
				S.x2 -= dt
	else:
		# dietro ai menu il treno corre da solo, senza cattivi
		DEMO.ambT += dt
		if DEMO.ambT > PERC.secondi_per_ambiente:
			DEMO.ambT = 0.0
			DEMO.amb += 1
		DEMO.t += dt
		DEMO.sy = sin(DEMO.t * 18) * 1.2
		muovi_paesaggio(DEMO, dt, true)
	if S != null:
		S.flash = max(0.0, S.flash - dt)
		S.flashRosso = max(0.0, S.flashRosso - dt)
	muovi_cielo(dt)
	for c in COCCI:
		c.x += c.vx * dt
		c.y += c.vy * dt
		c.vy += 900 * dt
		c.r += c.vr * dt
	COCCI = COCCI.filter(func(c): return c.y < H + 80)
	for c in CONF:
		c.x += c.vx * dt
		c.y += c.vy * dt
		c.r += c.vr * dt
	CONF = CONF.filter(func(c): return c.y < H + 20)
	# gli strati del disegno: il vetro (con quello che c'è fuori), la cabina, le scritte sopra
	var sc = S if S != null else DEMO
	var f := finestra()
	strato_finestra.position = f.position + Vector2(sc.sx, sc.sy)
	strato_finestra.size = f.size
	strato_paesaggio.position = -f.position
	strato_cabina.position = Vector2(sc.sx, sc.sy)
	strato_paesaggio.queue_redraw()
	strato_cabina.queue_redraw()
	strato_sopra.queue_redraw()
	if prova:
		pubblica_prova(delta)


## Il treno avanza: gli oggetti vengono incontro, ne arrivano di nuovi all'orizzonte.
func muovi_paesaggio(s: Dictionary, dt: float, avanza: bool) -> void:
	var a := ambiente(s)
	var v: float = 6 * R.velocita_treno * (1 + s.livello * 0.04)
	if avanza:
		s.dist += v * dt
		s.prossimoOgg -= dt
		if s.prossimoOgg <= 0:
			s.oggetti.append(nuovo_oggetto(s, ZF))
			s.prossimoOgg = rnd(0.12, 0.28) * [1.6, 1.0, 0.7][a.densita - 1] / R.velocita_treno
	for o in s.oggetti:
		o.z -= v * dt
	s.oggetti = s.oggetti.filter(func(o): return o.z > ZN * 0.7)
	s.oggetti.sort_custom(func(x, y): return x.z > y.z)
	if s == S:
		s.ritmo += dt * v / 6
		if s.ritmo > 0.45:
			s.ritmo = 0.0
			suoni.suona("sferraglia")


## Dove si trova ogni cattivo sullo schermo (dipende da quanto è lontano il suo nascondiglio).
func posiziona_cattivi() -> void:
	var V := vista()
	for c in S.cattivi:
		var o = c.o
		var k: float = min(1.0, c.t / c.entra) if c.fase == "entra" else 1.0
		k = 1 - (1 - k) * (1 - k)
		var Q := proj(V, o.X + c.dx * k, o.z)
		var su: float = (1 - k) * 0.55 if c.fase == "entra" else 0.0
		c.u = Q.z * 1.7
		c.r = max(9.0, 0.24 * c.u)
		c.piedi = Q.y
		c.x = Q.x
		c.y = Q.y - (1.62 - su) * c.u
		c.k = k


## v0.31 (PR di Francesco M.): uccelli che passano nel cielo. v0.26: la pioggia.
func muovi_cielo(dt: float) -> void:
	if UCC.size() < 5 and randf() < dt * 0.25:
		UCC.append({"x": -0.05, "y": 0.08 + randf() * 0.35, "v": 0.05 + randf() * 0.06, "a": randf() * 6, "s": 0.7 + randf() * 0.6})
	for u in UCC:
		u.x += u.v * dt
		u.a += dt * 9
	UCC = UCC.filter(func(u): return u.x < 1.05)
	if S != null and S.livello >= 3:
		var n := 220 if S.livello >= 4 else 120
		while GOCCE.size() < n:
			GOCCE.append({"x": randf(), "y": randf(), "v": 0.9 + randf() * 0.6})
		for i in n:
			var q = GOCCE[i]
			q.y += q.v * dt * 1.4
			q.x -= dt * 0.12
			if q.y > 1:
				q.y = 0.0
				q.x = randf() * 1.1


# =====================================================================
#   IL DISEGNO (i «pennelli»)
# =====================================================================
func prepara_disegno() -> void:
	# i caratteri: lo stesso font di Godot, più o meno «grassetto»
	for peso in [600, 700, 800, 900]:
		var fv := FontVariation.new()
		fv.base_font = ThemeDB.fallback_font
		fv.variation_embolden = {600: 0.0, 700: 0.25, 800: 0.5, 900: 0.8}[peso]
		FONT[peso] = fv
	MIMETICA = crea_mimetica()
	MIRINO = crea_mirino()
	strato_finestra = Control.new()
	strato_finestra.clip_contents = true
	strato_finestra.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(strato_finestra)
	strato_paesaggio = Strato.new()
	strato_paesaggio.texture_repeat = CanvasItem.TEXTURE_REPEAT_ENABLED
	strato_paesaggio.disegna = disegna_finestra
	strato_finestra.add_child(strato_paesaggio)
	strato_cabina = Strato.new()
	strato_cabina.disegna = disegna_cabina
	add_child(strato_cabina)
	strato_sopra = Strato.new()
	strato_sopra.disegna = disegna_sopra
	add_child(strato_sopra)


## v0.8 (indicazione del prof): la stoffa mimetica degli omini, una piastrella 48 x 48 che si ripete.
func crea_mimetica() -> ImageTexture:
	var im := Image.create(48, 48, false, Image.FORMAT_RGBA8)
	im.fill(Color("#5b6b3a"))
	var macchie := [[Color("#3d4a28"), 9], [Color("#8a7a4e"), 7], [Color("#2b2b1e"), 6]]
	for j in macchie.size():
		for i in macchie[j][1]:
			var x := float((i * 17 + j * 11) % 48)
			var y := float((i * 29 + j * 7) % 48)
			var rx: float = 4.0 + (i * 7 + j) % 6
			var ry: float = 3.0 + (i * 5 + j * 3) % 5
			var rot: float = (i + j) * 0.7
			for py in 48:
				for px in 48:
					var dx := fposmod(px + 0.5 - x + 24.0, 48.0) - 24.0
					var dy := fposmod(py + 0.5 - y + 24.0, 48.0) - 24.0
					var u := dx * cos(rot) + dy * sin(rot)
					var w := -dx * sin(rot) + dy * cos(rot)
					if (u / rx) * (u / rx) + (w / ry) * (w / ry) <= 1.0:
						im.set_pixel(px, py, macchie[j][0])
	return ImageTexture.create_from_image(im)


## v0.19 (PR di Ney V.): il puntatore del mouse è un mirino rosso.
func crea_mirino() -> Image:
	var im := Image.create(40, 40, false, Image.FORMAT_RGBA8)
	var rosso := Color("#ff2a2a")
	for py in 40:
		for px in 40:
			var d := Vector2(px + 0.5 - 20, py + 0.5 - 20)
			var l := d.length()
			var tacca: bool = (abs(d.x) < 1.5 and (abs(d.y) > 9 and abs(d.y) < 19)) or (abs(d.y) < 1.5 and (abs(d.x) > 9 and abs(d.x) < 19))
			if abs(l - 13) < 1.5 or l < 2.5 or tacca:
				im.set_pixel(px, py, rosso)
	return im


func mirino(attivo: bool) -> void:
	if attivo:
		Input.set_custom_mouse_cursor(MIRINO, Input.CURSOR_ARROW, Vector2(20, 20))
	else:
		Input.set_custom_mouse_cursor(null)


# ---------- piccoli aiuti per disegnare ----------
func A(c: Color) -> Color:
	return Color(c.r, c.g, c.b, c.a * alfa)


func testo(g: CanvasItem, s: String, x: float, y: float, size: int, col: Color, peso := 800, allinea := "left") -> void:
	var f: Font = FONT[peso]
	var w := f.get_string_size(s, HORIZONTAL_ALIGNMENT_LEFT, -1, size).x
	var x0 := x if allinea == "left" else (x - w / 2.0 if allinea == "center" else x - w)
	g.draw_string(f, Vector2(x0, y), s, HORIZONTAL_ALIGNMENT_LEFT, -1, size, col)


func larghezza(s: String, size: int, peso := 800) -> float:
	return FONT[peso].get_string_size(s, HORIZONTAL_ALIGNMENT_LEFT, -1, size).x


func ellisse(c: Vector2, rx: float, ry: float, da := 0.0, a := TAU, n := 28) -> PackedVector2Array:
	var p := PackedVector2Array()
	for i in n + 1:
		var t := da + (a - da) * i / n
		p.append(c + Vector2(cos(t) * rx, sin(t) * ry))
	return p


## Curva «quadratica» (come quadraticCurveTo del canvas): da p0 a p2, tirata verso p1.
func curva(p0: Vector2, p1: Vector2, p2: Vector2, n := 8) -> PackedVector2Array:
	var p := PackedVector2Array()
	for i in n + 1:
		var t := float(i) / n
		p.append(p0 * (1 - t) * (1 - t) + p1 * 2 * t * (1 - t) + p2 * t * t)
	return p


## Un poligono riempito con la stoffa mimetica.
func mim_poligono(g: CanvasItem, pts: PackedVector2Array) -> void:
	var uv := PackedVector2Array()
	for q in pts:
		uv.append(q / 48.0)
	g.draw_colored_polygon(pts, A(Color.WHITE), uv, MIMETICA)


## Una linea spessa con le punte arrotondate, di stoffa mimetica (gambe e braccia).
func mim_linea(g: CanvasItem, pts: Array, w: float) -> void:
	for i in pts.size() - 1:
		var a: Vector2 = pts[i]
		var b: Vector2 = pts[i + 1]
		var n := (b - a).orthogonal().normalized() * w / 2.0
		mim_poligono(g, PackedVector2Array([a + n, b + n, b - n, a - n]))
	for q in pts:
		mim_poligono(g, ellisse(q, w / 2.0, w / 2.0, 0.0, TAU, 12))


# ---------- strato 1: il vetro e quello che si vede fuori ----------
func disegna_finestra(g: CanvasItem) -> void:
	var sc = S if S != null else DEMO
	paesaggio(g, sc)
	vetro(g, sc)


func paesaggio(g: CanvasItem, s: Dictionary) -> void:
	var V := vista()
	var f: Rect2 = V.f
	var a := ambiente(s)
	var hz: float = V.hz
	var bot: float = V.bot
	# il cielo sfumato
	var ca := Color(a.cielo_alto)
	var cb := Color(a.cielo_basso)
	g.draw_polygon(PackedVector2Array([f.position, Vector2(f.end.x, f.position.y), Vector2(f.end.x, hz + 1), Vector2(f.position.x, hz + 1)]), PackedColorArray([ca, ca, cb, cb]))
	uccelli(g, f, hz)
	# le colline lontane
	var coll := PackedVector2Array([Vector2(f.position.x, hz)])
	for i in 13:
		var xx := f.position.x + i * f.size.x / 12.0
		coll.append(Vector2(xx, hz - f.size.y * (0.05 + 0.09 * abs(sin(i * 1.7 + s.dist * 0.003)))))
	coll.append(Vector2(f.end.x, hz))
	g.draw_colored_polygon(coll, Color(a.lontano))
	g.draw_rect(Rect2(f.position.x, hz, f.size.x, bot - hz), Color(a.terra))
	# massicciata e binari
	var p1 := proj(V, -1.3, ZF)
	var p2 := proj(V, 1.3, ZF)
	var p3 := proj(V, 1.3, ZN * 0.9)
	var p4 := proj(V, -1.3, ZN * 0.9)
	g.draw_colored_polygon(PackedVector2Array([Vector2(p1.x, p1.y), Vector2(p2.x, p2.y), Vector2(p3.x, p3.y), Vector2(p4.x, p4.y)]), Color("#6d665c"))
	var z: float = ZN * 0.9 + (1 - fmod(s.dist, 1.0))
	while z < ZF:
		var l := proj(V, -1.1, z)
		var r := proj(V, 1.1, z)
		g.draw_line(Vector2(l.x, l.y), Vector2(r.x, r.y), Color("#4a3324"), max(1.0, 0.18 * l.z))
		z += 1.0
	for X in [-0.75, 0.75]:
		var A1 := proj(V, X, ZF)
		var B1 := proj(V, X, ZN * 0.9)
		# v0.27 (PR di Katherine A.): binari gialli
		g.draw_line(Vector2(A1.x, A1.y), Vector2(B1.x, B1.y), ORO, 3.0)
	# gli oggetti, dal più lontano al più vicino
	var fuori := []
	for o in s.oggetti:
		if o.z < ZN * 0.7:
			continue
		if s == S:
			for c in S.cattivi:
				if is_same(c.o, o):
					# mentre esce, il cattivo è dietro al suo nascondiglio
					if c.fase == "entra":
						disegna_cattivo(g, c)
					else:
						fuori.append(c)
		disegna_oggetto(g, o, proj(V, o.X, o.z))
	# v0.20 (PR di Egor M.): il cattivo uscito dal nascondiglio si disegna sopra a tutti gli oggetti, così si vede sempre
	for c in fuori:
		disegna_cattivo(g, c)
	meteo(g, f, s)


func disegna_oggetto(g: CanvasItem, o: Dictionary, P: Vector3) -> void:
	var x := P.x
	var b := P.y
	var w: float = o.w * P.z
	var h: float = o.h * P.z
	var col: Color = o.col
	match o.tipo:
		"alberi":
			g.draw_rect(Rect2(x - w * 0.08, b - h * 0.35, w * 0.16, h * 0.35), Color("#5a3b22"))
			g.draw_colored_polygon(PackedVector2Array([Vector2(x - w / 2, b - h * 0.3), Vector2(x, b - h), Vector2(x + w / 2, b - h * 0.3)]), col)
			g.draw_colored_polygon(PackedVector2Array([Vector2(x - w * 0.42, b - h * 0.55), Vector2(x, b - h * 1.08), Vector2(x + w * 0.42, b - h * 0.55)]), col)
		"case":
			g.draw_rect(Rect2(x - w / 2, b - h, w, h), col)
			g.draw_colored_polygon(PackedVector2Array([Vector2(x - w * 0.58, b - h), Vector2(x, b - h * 1.5), Vector2(x + w * 0.58, b - h)]), o.tetto)
			g.draw_rect(Rect2(x - w * 0.32 - o.lato * w * 0.15 + w * 0.17, b - h * 0.72, w * 0.3, h * 0.3), Color("#3a2a1c"))
			g.draw_rect(Rect2(x + o.lato * w * 0.25 - w * 0.08, b - h * 0.7, w * 0.16, h * 0.22), Color("#ffe39a"))
			g.draw_rect(Rect2(x - w * 0.08, b - h * 0.38, w * 0.16, h * 0.38), Color("#5a3b22"))
		"palazzi":
			g.draw_rect(Rect2(x - w / 2, b - h, w, h), col)
			var st: float = max(6.0, P.z * 0.5)
			# v0.21 (PR di Luca B.): le finestre accese restano sempre le stesse (prima lampeggiavano)
			var sem := int(o.w * 97 + o.h * 31)
			var ri := 0
			var yy := b - h + st
			while yy < b - st:
				var ci := 0
				var xx := x - w / 2 + st * 0.6
				while xx < x + w / 2 - st * 0.6:
					if (ri * 7 + ci * 13 + sem) % 4 == 0:
						g.draw_rect(Rect2(xx, yy, st * 0.5, st * 0.6), Color(1, 0.86, 0.47, 0.6))
					xx += st * 1.2
					ci += 1
				yy += st * 1.4
				ri += 1
		"rocce":
			g.draw_colored_polygon(PackedVector2Array([Vector2(x - w / 2, b), Vector2(x - w * 0.3, b - h * 0.8), Vector2(x, b - h), Vector2(x + w * 0.35, b - h * 0.7), Vector2(x + w / 2, b)]), col)
		"rottame":
			g.draw_colored_polygon(PackedVector2Array([Vector2(x - w / 2, b), Vector2(x - w * 0.35, b - h * 0.7), Vector2(x - w * 0.1, b - h * 0.45), Vector2(x + w * 0.05, b - h), Vector2(x + w * 0.3, b - h * 0.55), Vector2(x + w / 2, b - h * 0.3), Vector2(x + w / 2, b)]), Color("#3a3d42"))
			var lw: float = max(1.0, P.z * 0.06)
			g.draw_line(Vector2(x - w * 0.3, b - h * 0.3), Vector2(x + w * 0.3, b - h * 0.2), Color("#8a4b2a"), lw)
			g.draw_line(Vector2(x - w * 0.05, b - h * 0.75), Vector2(x + w * 0.15, b - h * 0.35), Color("#8a4b2a"), lw)
			var tf := fmod(Time.get_ticks_msec() / 600.0 + o.fumo, 3.0)
			g.draw_circle(Vector2(x + w * 0.05, b - h - tf * h * 0.6), w * (0.12 + tf * 0.08), Color(0.235, 0.235, 0.235, 0.35 * (1 - tf / 3)))
			g.draw_circle(Vector2(x + w * 0.05, b - h * 0.9), max(1.5, w * 0.04), Color(1, 0.47, 0.157, 0.85))
		"barile":
			g.draw_rect(Rect2(x - w / 2, b - h, w, h), col)
			g.draw_rect(Rect2(x - w / 2, b - h * 0.7, w, h * 0.08), Color(0, 0, 0, 0.3))
			g.draw_rect(Rect2(x - w / 2, b - h * 0.3, w, h * 0.08), Color(0, 0, 0, 0.3))
		_:
			g.draw_polyline(curva(Vector2(x - w / 2, b - h), Vector2(x, b - h * 2.2), Vector2(x + w / 2, b - h)), Color(1, 1, 1, 0.6), max(1.0, P.z * 0.06))


func disegna_cattivo(g: CanvasItem, c: Dictionary) -> void:
	alfa = 1.0
	if c.fase == "colpito":
		# v0.18: il cattivo cade a terra piano e poi sparisce
		var k: float = min(1.0, c.morto / 0.5)
		alfa = 1.0 if c.morto < 0.55 else max(0.0, 1 - (c.morto - 0.55) / 0.3)
		var perno := Vector2(c.x, c.piedi)
		g.draw_set_transform_matrix(Transform2D(0, perno) * Transform2D(k * 1.3 * c.o.lato, Vector2.ZERO) * Transform2D(0, -perno))
	omino(g, c)
	if c.fase == "spara":
		var d: float = -c.o.lato
		g.draw_circle(Vector2(c.x + d * c.u * 0.62, c.y + c.u * 0.5), c.u * 0.18, Color(1, 0.9, 0.47, max(0.0, 1 - c.morto * 2)))
	if c.fase == "entra" and c.k > 0.5:
		testo(g, "!", c.x, c.y - c.r * 1.3, roundi(c.r * 1.1), Color("#ff4d4d"), 900, "center")
	g.draw_set_transform_matrix(Transform2D.IDENTITY)
	alfa = 1.0


## La barretta del tempo sopra la testa: gialla, poi rossa. Quando finisce, il cattivo spara.
func barra_tempo(g: CanvasItem, c: Dictionary, r: float) -> void:
	if c.fase != "attende":
		return
	var k: float = min(1.0, (c.t - c.entra) / c.tempo)
	var w := r * 1.8
	var h: float = max(4.0, r * 0.16)
	g.draw_rect(Rect2(c.x - w / 2, c.y - r * 1.55, w, h), A(Color(0, 0, 0, 0.5)))
	g.draw_rect(Rect2(c.x - w / 2, c.y - r * 1.55, w * (1 - k), h), A(Color("#ff4d4d") if k > 0.7 else ORO))


## v0.7 (indicazione del prof): omini interi, non cerchietti, che escono dal nascondiglio
func omino(g: CanvasItem, c: Dictionary) -> void:
	var u: float = c.u
	var x: float = c.x
	var y: float = c.y
	var r: float = c.r
	var d: float = -c.o.lato
	var b: Dictionary = c.b
	var col := Color(b.colore if b.colore is String else "#444444")
	var passo: float = sin(c.t * 22) * u * 0.08 if c.fase == "entra" else 0.0
	var ya := y + r * 0.95
	# le gambe
	mim_linea(g, [Vector2(x - u * 0.09, ya + u * 0.62), Vector2(x - u * 0.12 + passo, c.piedi - u * 0.03)], u * 0.13)
	mim_linea(g, [Vector2(x + u * 0.09, ya + u * 0.62), Vector2(x + u * 0.12 - passo, c.piedi - u * 0.03)], u * 0.13)
	g.draw_rect(Rect2(x - u * 0.2 + passo, c.piedi - u * 0.06, u * 0.15, u * 0.06), A(Color("#16181c")))
	g.draw_rect(Rect2(x + u * 0.05 - passo, c.piedi - u * 0.06, u * 0.15, u * 0.06), A(Color("#16181c")))
	# il busto
	var busto := curva(Vector2(x - u * 0.22, ya + u * 0.05), Vector2(x, ya - u * 0.04), Vector2(x + u * 0.22, ya + u * 0.05), 6)
	busto.append(Vector2(x + u * 0.19, ya + u * 0.66))
	busto.append(Vector2(x - u * 0.19, ya + u * 0.66))
	mim_poligono(g, busto)
	g.draw_rect(Rect2(x - u * 0.19, ya + u * 0.5, u * 0.38, u * 0.07), A(Color("#2b2418")))
	g.draw_rect(Rect2(x - u * 0.2, ya + u * 0.08, u * 0.07, u * 0.07), A(col))
	# le braccia e l'arma puntata verso il treno
	mim_linea(g, [Vector2(x - d * u * 0.18, ya + u * 0.12), Vector2(x - d * u * 0.02, ya + u * 0.36), Vector2(x + d * u * 0.22, ya + u * 0.36)], u * 0.11)
	mim_linea(g, [Vector2(x + d * u * 0.18, ya + u * 0.12), Vector2(x + d * u * 0.32, ya + u * 0.3)], u * 0.11)
	g.draw_circle(Vector2(x + d * u * 0.24, ya + u * 0.36), u * 0.055, A(Color("#e0b48a")))
	g.draw_circle(Vector2(x + d * u * 0.33, ya + u * 0.3), u * 0.05, A(Color("#e0b48a")))
	if b.img != null and b.arma == "ak":
		fucile(g, Vector2(x, ya + u * 0.31), u, d)
	else:
		g.draw_rect(Rect2(x if d > 0 else x - u * 0.62, ya + u * 0.27, u * 0.62, u * 0.09), A(Color("#1d1f24")))
		g.draw_rect(Rect2(x + u * 0.08 if d > 0 else x - u * 0.2, ya + u * 0.33, u * 0.12, u * 0.14), A(Color("#1d1f24")))
	# la testa: la faccia della foto, oppure il bandito con la maschera
	if b.img != null:
		faccia(g, c)
		return
	var arr: bool = c.fase == "attende" and c.t > c.entra + c.tempo * 0.55
	barra_tempo(g, c, r)
	var t := Vector2(x, y)
	g.draw_circle(t, r, A(Color("#e0b48a")))
	var capelli := ellisse(t + Vector2(0, -r * 0.25), r * 1.02, r * 1.02, PI * 1.05, PI * 1.95, 16)
	g.draw_colored_polygon(capelli, A(Color("#2b1a10")))
	if b.cappello == 1:
		g.draw_rect(Rect2(x - r * 1.1, y - r * 0.72, r * 2.2, r * 0.2), A(Color("#222222")))
		g.draw_rect(Rect2(x - r * 0.65, y - r * 1.35, r * 1.3, r * 0.7), A(Color("#222222")))
	g.draw_rect(Rect2(x - r * 1.02, y - r * 0.32, r * 2.04, r * 0.42), A(col))
	for i in 2:
		var e: float = [-0.38, 0.38][i]
		g.draw_circle(Vector2(x + e * r, y - r * 0.12), r * 0.17, A(Color.WHITE))
		g.draw_circle(Vector2(x + e * r + sin(c.t * 6 + i) * r * 0.04, y - r * 0.1), r * 0.08, A(Color("#111111")))
		if arr:
			g.draw_line(Vector2(x + e * r - r * 0.2, y - r * (0.42 if e < 0 else 0.32)), Vector2(x + e * r + r * 0.2, y - r * (0.32 if e < 0 else 0.42)), A(Color("#111111")), r * 0.1)
	if arr:
		g.draw_colored_polygon(ellisse(Vector2(x, y + r * 0.48), r * 0.28, r * 0.16), A(Color("#5a1a1a")))
	else:
		g.draw_colored_polygon(ellisse(Vector2(x, y + r * 0.5), r * 0.22, r * 0.06), A(Color("#5a1a1a")))
	if b.nome != "":
		var tw := larghezza(b.nome, 12, 700) + 12
		g.draw_rect(Rect2(x - tw / 2, y - r * 2.1, tw, 17), A(Color(0, 0, 0, 0.55)))
		testo(g, b.nome, x, y - r * 2.1 + 13, 12, A(Color.WHITE), 700, "center")


## v0.8: il fucile d'assalto (calcio e paramano di legno, caricatore curvo) per chi ha "ak" in facce.json
func fucile(g: CanvasItem, o: Vector2, u: float, d: float) -> void:
	var P := func(px: float, py: float) -> Vector2: return o + Vector2(px * d * u, py * u)
	var R4 := func(px: float, py: float, w: float, h: float) -> PackedVector2Array: return PackedVector2Array([P.call(px, py), P.call(px + w, py), P.call(px + w, py + h), P.call(px, py + h)])
	var legno := A(Color("#8a5a2b"))
	g.draw_colored_polygon(PackedVector2Array([P.call(-0.32, -0.04), P.call(-0.05, -0.05), P.call(-0.05, 0.06), P.call(-0.3, 0.12)]), legno)
	g.draw_colored_polygon(R4.call(-0.06, -0.06, 0.42, 0.1), A(Color("#2a2a2a")))
	g.draw_colored_polygon(R4.call(0.36, -0.035, 0.34, 0.04), A(Color("#2a2a2a")))
	g.draw_colored_polygon(R4.call(0.62, -0.08, 0.025, 0.05), A(Color("#2a2a2a")))
	g.draw_colored_polygon(R4.call(0.2, -0.055, 0.2, 0.08), legno)
	var car := PackedVector2Array([P.call(0.08, 0.04)])
	for q in curva(Vector2(0.08, 0.04), Vector2(0.1, 0.24), Vector2(0.2, 0.3), 6).slice(1):
		car.append(P.call(q.x, q.y))
	car.append(P.call(0.26, 0.27))
	for q in curva(Vector2(0.26, 0.27), Vector2(0.17, 0.2), Vector2(0.16, 0.04), 6).slice(1):
		car.append(P.call(q.x, q.y))
	g.draw_colored_polygon(car, A(Color("#3a3a3a")))


## La testa con la faccia di una foto: ritagliata a forma di testa (un ovale), senza cerchio intorno.
func faccia(g: CanvasItem, c: Dictionary) -> void:
	var r: float = c.r
	var b: Dictionary = c.b
	var t := Vector2(c.x, c.y)
	barra_tempo(g, c, r)
	if b.nome != "":
		var tw := larghezza(b.nome, 13, 700) + 12
		g.draw_rect(Rect2(t.x - tw / 2, t.y + r * 1.22, tw, 18), A(Color(0, 0, 0, 0.55)))
		testo(g, b.nome, t.x, t.y + r * 1.22 + 13, 13, A(Color.WHITE), 700, "center")
	var punti := ellisse(t, r * 0.86, r * 1.08, 0.0, TAU, 32)
	var uv := PackedVector2Array()
	var origine := t + Vector2(-r * 1.25, -r * 1.3)
	for q in punti:
		uv.append((q - origine) / (2.5 * r))
	g.draw_colored_polygon(punti, A(Color.WHITE), uv, b.img)


## v0.26 (PR di Lina A., Youssef A., Oscar F. e Riccardo B.): il meteo.
## Dal livello 2 cielo grigio, dal 3 pioggia, dal 4 nebbia (preso dal fork della 3INF, v1.2).
func meteo(g: CanvasItem, f: Rect2, s: Dictionary) -> void:
	var L: int = s.livello
	if L < 2:
		return
	g.draw_rect(f, Color(120 / 255.0, 130 / 255.0, 145 / 255.0, min(0.35, 0.08 * (L - 1))))
	if L >= 3:
		var n := 220 if L >= 4 else 120
		var righe := PackedVector2Array()
		for i in min(n, GOCCE.size()):
			var q = GOCCE[i]
			var x: float = f.position.x + q.x * f.size.x
			var y: float = f.position.y + q.y * f.size.y
			righe.append(Vector2(x, y))
			righe.append(Vector2(x - 4, y + 14))
		if righe.size() > 0:
			g.draw_multiline(righe, Color(200 / 255.0, 215 / 255.0, 235 / 255.0, 0.55), 1.3)
	if L >= 4:
		var nb := Color(210 / 255.0, 215 / 255.0, 220 / 255.0)
		var y6 := f.position.y + f.size.y * 0.6
		g.draw_polygon(PackedVector2Array([f.position, Vector2(f.end.x, f.position.y), Vector2(f.end.x, y6), Vector2(f.position.x, y6)]), PackedColorArray([Color(nb, 0.55), Color(nb, 0.55), Color(nb, 0.25), Color(nb, 0.25)]))
		g.draw_polygon(PackedVector2Array([Vector2(f.position.x, y6), Vector2(f.end.x, y6), f.end, Vector2(f.position.x, f.end.y)]), PackedColorArray([Color(nb, 0.25), Color(nb, 0.25), Color(nb, 0.0), Color(nb, 0.0)]))


## v0.31 (PR di Francesco M.): uccelli che passano nel cielo (in pausa si fermano anche loro)
func uccelli(g: CanvasItem, f: Rect2, hz: float) -> void:
	for u in UCC:
		var x: float = f.position.x + u.x * f.size.x
		var y: float = f.position.y + u.y * (hz - f.position.y)
		var w: float = 9 * u.s
		var ali: float = sin(u.a) * 4 * u.s
		var ala := curva(Vector2(x - w, y - ali), Vector2(x - w / 2, y - 4 * u.s), Vector2(x, y), 5)
		ala.append_array(curva(Vector2(x, y), Vector2(x + w / 2, y - 4 * u.s), Vector2(x + w, y - ali), 5).slice(1))
		g.draw_polyline(ala, Color(20 / 255.0, 20 / 255.0, 25 / 255.0, 0.85), 2.0)


## Il vetro: un velo azzurro, un riflesso, e le crepe (v1.0: dal bordo verso il centro).
func vetro(g: CanvasItem, s: Dictionary) -> void:
	var f := finestra()
	g.draw_rect(f, Color(160 / 255.0, 210 / 255.0, 1, 0.07))
	g.draw_line(Vector2(f.position.x + f.size.x * 0.05, f.end.y), Vector2(f.position.x + f.size.x * 0.3, f.position.y), Color(1, 1, 1, 0.14), 16)
	for c in s.crepe:
		g.draw_circle(Vector2(c.x, c.y), 10, Color(1, 1, 1, 0.16))
		for seg in c.linee:
			g.draw_polyline(seg, Color(1, 1, 1, 0.9), 1.4, true)
		for seg in c.rami:
			g.draw_polyline(seg, Color(1, 1, 1, 0.7), 1.0, true)
		for a in c.anelli:
			var anello := PackedVector2Array()
			for i in 11:
				var t := i / 10.0 * TAU
				var rr: float = a * (1 + sin(i * 2.7) * 0.18)
				anello.append(Vector2(c.x + cos(t) * rr, c.y + sin(t) * rr))
			g.draw_polyline(anello, Color(1, 1, 1, 0.55), 1.0, true)
		for sch in c.schegge:
			g.draw_colored_polygon(sch, Color(1, 1, 1, 0.85))
		g.draw_circle(Vector2(c.x, c.y), 3.5, Color.WHITE)


# ---------- strato 2: la cabina (cruscotto, macchinista, scintille, scritte) ----------
func disegna_cabina(g: CanvasItem) -> void:
	var sc = S if S != null else DEMO
	vagone(g, sc)
	if S == null:
		return
	for p in S.part:
		var al: float = max(0.0, 1 - p.t / (0.25 if p.mira else 0.7))
		if p.mira:
			g.draw_arc(Vector2(p.x, p.y), p.r + p.t * 80, 0, TAU, 32, Color(p.c, al), 3.0, true)
		else:
			g.draw_circle(Vector2(p.x, p.y), p.r, Color(p.c, al))
	for t in S.testi:
		var al: float = max(0.0, 1 - t.t / 1.4)
		var size := 40 if t.big else 19
		var peso := 900 if t.big else 800
		# v1.0: le scritte grandi si rimpiccioliscono se non stanno nello schermo (telefono in verticale)
		var lw := larghezza(t.s, size, peso)
		if t.big and lw > W - 16:
			size = int(size * (W - 16) / lw)
		if t.fumetto:
			var w := larghezza(t.s, size, peso) + 16
			var bx: float = clamp(t.x, w / 2 + 4, W - w / 2 - 4)
			g.draw_rect(Rect2(bx - w / 2, t.y - 24 - t.t * 20, w, 30), Color(1, 1, 1, al))
			testo(g, t.s, bx, t.y - 3 - t.t * 20, size, Color(0.07, 0.07, 0.07, al), peso, "center")
		else:
			testo(g, t.s, t.x, t.y - t.t * 40, size, Color(ORO if t.big else Color.WHITE, al), peso, "center")


func vagone(g: CanvasItem, s: Dictionary) -> void:
	var f := finestra()
	var grigio := Color("#3b3f46")
	g.draw_rect(Rect2(-40, -40, W + 80, f.position.y + 40), grigio)
	g.draw_rect(Rect2(-40, f.end.y, W + 80, H - f.end.y + 40), grigio)
	g.draw_rect(Rect2(-40, f.position.y, f.position.x + 40, f.size.y), grigio)
	g.draw_rect(Rect2(f.end.x, f.position.y, W - f.end.x + 40, f.size.y), grigio)
	g.draw_rect(f, Color("#22252a"), false, 8.0)
	g.draw_rect(Rect2(W / 2 - 4, f.position.y, 8, f.size.y * 0.18), Color("#2b2e33"))
	var dy := f.end.y
	var dh := H - dy
	g.draw_rect(Rect2(-40, dy + dh * 0.25, W + 80, dh * 0.75 + 40), Color("#2a2d33"))
	# il tachimetro (km/h) e lo stato del vetro
	var r: float = min(dh * 0.32, W * 0.09)
	var quadranti := [[W * 0.2, "km/h", str(int(60 * R.velocita_treno * (1 + s.livello * 0.04)))], [W * 0.8, "vetro", "%d/%d" % [s.vetro, s.vetroMax]]]
	for q in quadranti:
		var cq := Vector2(q[0], dy + dh * 0.58)
		g.draw_circle(cq, r, Color("#111111"))
		g.draw_arc(cq, r, 0, TAU, 48, ORO, 3.0, true)
		testo(g, q[2], cq.x, cq.y + r * 0.15, roundi(r * 0.55), Color.WHITE, 800, "center")
		testo(g, q[1], cq.x, cq.y + r * 0.55, roundi(r * 0.3), Color.WHITE, 600, "center")
	# il macchinista (protagonista.json)
	g.draw_colored_polygon(ellisse(Vector2(W / 2, H), W * 0.16, dh * 0.55, PI, TAU, 32), Color(PROT.giacca))
	testo(g, PROT.nome, W / 2, H - dh * 0.18, 14, Color.WHITE, 700, "center")


# ---------- strato 3: lampi, sfera d'oro, punteggio (non tremano) ----------
func disegna_sopra(g: CanvasItem) -> void:
	if S != null:
		if S.flash > 0:
			g.draw_rect(Rect2(0, 0, W, H), Color(1, 60 / 255.0, 40 / 255.0, min(1.0, S.flash * 2)))
		if S.sfera != null:
			var sf = S.sfera
			var rr: float = 22 + sin(sf.t * 8) * 3
			for i in 10:
				var k := i / 9.0
				var cc := Vector2(sf.x, sf.y) + Vector2(-6, -6) * k
				g.draw_circle(cc, max(3.0, rr * (1 - k * 0.85)), Color("#d4a017").lerp(Color("#fff6b0"), k))
			testo(g, "x2", sf.x, sf.y + 6, 16, Color("#5a3b00"), 900, "center")
		if S.x2 > 0:
			testo(g, "PUNTI x2 · %d s" % ceili(S.x2), W / 2, H * 0.16, 22, ORO, 900, "center")
		if S.flashRosso > 0:
			g.draw_rect(Rect2(0, 0, W, H), Color(1, 0, 0, S.flashRosso))
		if not S.fine:
			hud(g)
	for c in COCCI:
		g.draw_set_transform(Vector2(c.x, c.y), c.r)
		var tri := PackedVector2Array([Vector2(0, -c.s / 2), Vector2(c.s / 2, c.s / 3), Vector2(-c.s / 3, c.s / 2)])
		g.draw_colored_polygon(tri, Color(190 / 255.0, 230 / 255.0, 1, 0.55))
		tri.append(tri[0])
		g.draw_polyline(tri, Color(1, 1, 1, 0.9), 1.0)
	for c in CONF:
		g.draw_set_transform(Vector2(c.x, c.y), c.r)
		g.draw_rect(Rect2(-5, -3, 10, 6), c.c)
	g.draw_set_transform(Vector2.ZERO)


func hud(g: CanvasItem) -> void:
	var f := finestra()
	var pad := 10.0
	var ty: float = f.position.y - 12 if f.position.y - 12 > 18 else 24.0
	var stretto := W < 640   # telefono in verticale: la riga dell'ambiente va sotto la barra
	testo(g, "Punti %d" % S.punti, pad, ty, 20, Color.WHITE, 800)
	# v0.22 (PR di Youssef A.): il record resta e si vede accanto ai punti
	var rec: int = max(S.punti, ui.miglior_punteggio())
	testo(g, "Record %d" % rec, pad + larghezza("Punti %d" % S.punti, 20) * 1.4 + 18, ty, 15, ORO, 700)
	var info := "%s · %s %d · km %d" % [ambiente().nome, TX.livello, S.livello, int(S.km)]
	# v0.28 (PR di Luciano C.): barra al centro in alto, quanto manca al prossimo livello
	var fat: int = S.abbattuti % R.cattivi_per_livello
	var bw: float = min(260.0, W * 0.4)
	var bx := W / 2 - bw / 2
	var by := f.position.y + 8
	g.draw_rect(Rect2(bx - 2, by - 2, bw + 4, 14), Color(0, 0, 0, 0.55))
	g.draw_rect(Rect2(bx, by, bw * fat / R.cattivi_per_livello, 10), Color("#2f9e57"))
	testo(g, "prossimo livello: ancora %d" % (R.cattivi_per_livello - fat), W / 2, by + 26, 12, Color.WHITE, 700, "center")
	if stretto:
		var iw := larghezza(info, 13, 700) + 14
		g.draw_rect(Rect2(W / 2 - iw / 2, by + 32, iw, 20), Color(0, 0, 0, 0.45))
		testo(g, info, W / 2, by + 47, 13, ORO, 700, "center")
	else:
		testo(g, info, W / 2, ty, 15, ORO, 700, "center")
	var y0 := f.end.y + 12
	testo(g, "Vetro", W - pad, y0 + 14, 12, Color.WHITE, 700, "right")
	for i in S.vetroMax:
		g.draw_rect(Rect2(W - pad - 50 - (i + 1) * 22, y0, 16, 20), Color("#8fd3ff") if i < S.vetro else Color("#53213a"))


# ---------------- prova automatica (solo con ?prova nell'indirizzo) ----------------
func pubblica_prova(delta: float) -> void:
	prova_t += delta
	if prova_t < 0.1:
		return
	prova_t = 0.0
	var st := {"schermo": ui.schermo_attivo, "pausa": PAUSA, "fps": Engine.get_frames_per_second(), "t": S.t if S != null else 0.0, "W": W, "H": H, "scala": get_window().content_scale_factor, "bottoni": ui.rettangoli_bottoni()}
	if S != null:
		st.merge({"punti": S.punti, "vetro": S.vetro, "vetroMax": S.vetroMax, "colpi": S.colpi_presi, "livello": S.livello, "spari": S.spari, "abbattuti": S.abbattuti, "fine": S.fine,
			"sfera": [S.sfera.x, S.sfera.y] if S.sfera != null else null, "x2": S.x2,
			"cattivi": S.cattivi.filter(func(c): return c.fase == "attende" or c.fase == "entra").map(func(c): return [c.x, c.y, c.fase, c.r])})
	if OS.has_feature("web"):
		JavaScriptBridge.eval("window.__treno=" + JSON.stringify(st), true)
		return
	# dal terminale: la partita parte da sola, si colpisce ogni tanto un cattivo e si stampa lo stato
	if S == null and ui.schermo_attivo == "inizio":
		parti()
	elif S != null and randf() < 0.3:
		for c in S.cattivi:
			if c.fase == "attende":
				tocca(Vector2(c.x, c.y))
				break
	if S != null and randf() < 0.1:
		print("prova: ", JSON.stringify(st).left(300))
