extends Node2D
## IL TRENO BLINDATO — versione Godot (v2.0)
##
## Dalla versione HTML (v1.1 della 1INF) alla versione Godot: stesso gioco, motore nuovo.
## Per questo il numero cambia da 1.x a 2.0 (versione «major»: è cambiato qualcosa di grosso).
##
## Ponte da Lazarus:
##   Lazarus REAGISCE: il programma aspetta un clic (Button1Click) e poi risponde.
##   Godot PULSA: _process(delta) gira da solo circa 60 volte al secondo e muove tutto.
##   _draw() è il «pennello»: ridisegna la scena a ogni giro.
##
## I dati dei ragazzi (cattivi, ambienti, regole) stanno nella cartella dati/ in file .json:
## si cambia il gioco cambiando i dati, senza toccare questo codice.

const VERSIONE := "v2.1.3"  # il numero di versione: si vede sempre in alto a sinistra
const ZF := 18.0   # distanza più lontana che si vede (l'orizzonte)
const ZN := 1.0    # distanza più vicina (il vetro della cabina)
const MISURE := {"alberi": [2.0, 4.5], "case": [3.4, 2.8], "palazzi": [3.4, 8.0], "rocce": [3.0, 1.9], "onde": [3.0, 0.5]}
const CABINA := Color("#1a1410")
const ORO := Color("#ffd34d")

# ---- i dati (letti dai file .json) ----
var R := {}          # regole: vetro, velocità, secondi prima di sparare...
var AMB := {}        # ambienti: bosco, case, città, montagna, mare
var PERC := []       # l'ordine degli ambienti
var SEC_AMB := 20.0  # secondi per ogni ambiente
var CATTIVI := []    # i cattivi inventati dai ragazzi
var PERSONAGGI := [] # v2.1: i personaggi con l'immagine scelta dai ragazzi
var FRASI := []
var LODI := []

# ---- lo stato della partita (le «variabili» del gioco) ----
var stato := "titolo"   # titolo, gioco, fine
var tempo := 0.0
var punti := 0
var record := 0
var abbattuti := 0
var livello := 1
var combo := 0
var vetro := 5
var crepe := []      # le crepe sul vetro
var cattivi := []    # i cattivi in scena
var oggetti := []    # alberi, case, palazzi... vicino ai binari
var part := []       # scintille e coriandoli
var testi := []      # scritte che volano (+100, frasi dei cattivi)
var prossimo := 1.6  # secondi al prossimo cattivo
var prossimo_ogg := 0.0
var dist := 0.0
var amb := 0
var amb_t := 0.0
var scossa := 0.0
var flash := 0.0
var font: Font


func _ready() -> void:
	randomize()
	font = ThemeDB.fallback_font
	R = leggi_json("res://dati/regole.json", {})
	var a: Dictionary = leggi_json("res://dati/ambienti.json", {})
	AMB = a.get("ambienti", {})
	PERC = a.get("percorso", AMB.keys())
	SEC_AMB = float(a.get("secondi_per_ambiente", 20))
	CATTIVI = leggi_json("res://dati/cattivi.json", {}).get("cattivi", [])
	# v2.1: i PERSONAGGI dei ragazzi (immagini prese dal web e consegnate con il Modulo)
	for p in leggi_json("res://dati/personaggi.json", {}).get("personaggi", []):
		var tex = load(String(p.get("immagine", "")))
		if tex is Texture2D:
			p["tex"] = tex
			if not p.has("colore"):
				p["colore"] = "#3a4a5b"
			PERSONAGGI.append(p)
	var tx: Dictionary = leggi_json("res://dati/testi.json", {})
	FRASI = tx.get("frasi_cattivi", ["Hahahahaha, perdente!"])
	LODI = tx.get("lodi", ["Grande!"])
	record = carica_record()
	oggetti.clear()
	var z := ZF
	while z > 2.0:
		oggetti.append(nuovo_oggetto(z))
		z -= 1.3
	# prova automatica (solo per il controllo: godot --headless -- prova)
	if "prova" in OS.get_cmdline_user_args():
		nuova_partita()
	if "test" in OS.get_cmdline_user_args():
		nuova_partita()

func leggi_json(percorso: String, predefinito):
	if not FileAccess.file_exists(percorso):
		return predefinito
	var x = JSON.parse_string(FileAccess.get_file_as_string(percorso))
	return x if x != null else predefinito


func regola(nome: String, predefinito: float) -> float:
	return float(R.get(nome, predefinito))


# ---------------- record (si salva sul PC/telefono di chi gioca) ----------------
func carica_record() -> int:
	var c := ConfigFile.new()
	if c.load("user://record.cfg") == OK:
		return int(c.get_value("treno", "record", 0))
	return 0


func salva_record() -> void:
	var c := ConfigFile.new()
	c.set_value("treno", "record", record)
	c.save("user://record.cfg")


# ---------------- la geometria: guardiamo AVANTI lungo i binari ----------------
func finestra() -> Rect2:
	var s := get_viewport_rect().size
	var m: float = max(10.0, min(s.x, s.y) * 0.03)
	return Rect2(m, 44.0, s.x - 2.0 * m, s.y * 0.76 - 44.0)


func vista() -> Dictionary:
	var f := finestra()
	return {"f": f, "hz": f.position.y + f.size.y * 0.42, "bot": f.end.y, "vx": f.position.x + f.size.x / 2.0, "k": f.size.x * 0.16}


## Prospettiva: una cosa a distanza z sembra grande 1/z. X = quanto è a destra o a sinistra dei binari.
func proj(V: Dictionary, X: float, z: float) -> Vector3:
	var s := ZN / z
	return Vector3(V["vx"] + X * V["k"] * s, V["hz"] + (V["bot"] - V["hz"]) * s, V["k"] * s)


# ---------------- il gioco ----------------
func ambiente() -> Dictionary:
	return AMB[PERC[amb % PERC.size()]]


func nuova_partita() -> void:
	stato = "gioco"
	punti = 0
	abbattuti = 0
	livello = 1
	combo = 0
	vetro = int(regola("vetro", 5))
	crepe.clear()
	cattivi.clear()
	part.clear()
	testi.clear()
	prossimo = 1.6
	amb = 0
	amb_t = 0.0
	annuncia_ambiente()


func annuncia_ambiente() -> void:
	var s := get_viewport_rect().size
	testi.append({"x": s.x / 2.0, "y": s.y * 0.22, "s": String(ambiente().get("nome", "")).to_upper(), "t": 0.0, "big": true})


func nuovo_oggetto(z: float) -> Dictionary:
	var a := ambiente()
	var lato := -1.0 if randf() < 0.5 else 1.0
	if a.get("rottami", false) and randf() < 0.3:
		return {"X": lato * randf_range(1.7, 2.6), "z": z, "tipo": "rottame", "col": Color("#3a3d42"), "w": randf_range(1.2, 1.8), "h": randf_range(0.6, 0.9), "lato": lato, "cattivo": false}
	if randf() < 0.18:
		return {"X": lato * randf_range(1.6, 1.9), "z": z, "tipo": "barile", "col": Color("#8a4b2a"), "w": 0.7, "h": 1.0, "lato": lato, "cattivo": false}
	var tipo: String = a.get("oggetti", "alberi")
	var m: Array = MISURE.get(tipo, [2.0, 3.0])
	return {"X": lato * randf_range(2.2, 4.6), "z": z, "tipo": tipo, "col": Color(a.get("colore_oggetti", "#2b5d2b")),
		"w": m[0] * randf_range(0.8, 1.2), "h": m[1] * randf_range(0.8, 1.25), "lato": lato,
		"tetto": [Color("#8a2f22"), Color("#6b3a24"), Color("#a0432c")].pick_random(), "cattivo": false}


func nuovo_cattivo() -> void:
	# v2.1.1: il cattivo sceglie un nascondiglio più lontano, così ha il tempo di sparare prima che il treno lo superi
	var cand := oggetti.filter(func(o): return o["z"] > 6.0 and o["z"] < 12.0 and o["tipo"] != "onde" and not o["cattivo"])
	if cand.is_empty():
		return
	var o: Dictionary = cand.pick_random()
	var b: Dictionary
	if PERSONAGGI.size() > 0 and randf() < 0.6:
		b = PERSONAGGI.pick_random()
	elif CATTIVI.size() > 0 and randf() < 0.7:
		b = CATTIVI.pick_random()
	else:
		b = {"nome": "", "colore": ["#5b6b3a", "#6b5a3a", "#3a4a5b"].pick_random(), "occhi": randi_range(1, 3), "cappello": randi_range(0, 2), "bocca": randi_range(0, 2), "velocita": 1, "frase": ""}
	var vel := float(b.get("velocita", 1))
	var t_sparo: float = max(0.75, (regola("secondi_prima_di_sparare", 3.0) - livello * 0.12) / (1.0 + (vel - 1.0) * 0.2))
	# v2.1.1 (correzione di un errore segnalato dalla 1INF): prima il treno superava il cattivo PRIMA che sparasse,
	# così il vetro non si rompeva mai. Ora il tempo per sparare non supera il tempo in cui il cattivo resta visibile.
	var v_treno := 6.0 * regola("velocita_treno", 0.5) * (1.0 + livello * 0.04)
	var resta: float = (float(o["z"]) - ZN * 0.8) / v_treno
	t_sparo = min(t_sparo, max(0.8, resta - 0.75 - 0.5))
	o["cattivo"] = true
	# il cattivo è NASCOSTO dietro l'oggetto e scivola fuori di lato, verso i binari
	cattivi.append({"o": o, "dx": -o["lato"] * (o["w"] * 0.5 + 0.62), "t": 0.0, "entra": 0.75, "tempo": t_sparo, "b": b,
		"fase": "entra", "morto": 0.0, "x": 0.0, "y": 0.0, "r": 10.0, "u": 10.0, "piedi": 0.0, "k": 0.0})


func colpito(c: Dictionary) -> void:
	c["fase"] = "colpito"
	c["morto"] = 0.0
	abbattuti += 1
	combo += 1
	var p: int = int(regola("punti_per_cattivo", 100)) + min(40, combo * 2)
	punti += p
	testi.append({"x": c["x"], "y": c["y"] - c["r"], "s": "+%d%s" % [p, (" COMBO x%d" % combo) if combo > 2 else ""], "t": 0.0})
	for i in 22:
		var ang := randf() * TAU
		var v := randf_range(80, 380)
		part.append({"p": Vector2(c["x"], c["y"]), "v": Vector2(cos(ang), sin(ang)) * v, "t": 0.0, "c": Color(b_colore(c["b"])) if i % 3 else Color.WHITE, "r": randf_range(3, 8)})
	if abbattuti % int(regola("cattivi_per_livello", 10)) == 0:
		livello += 1
		var s := get_viewport_rect().size
		testi.append({"x": s.x / 2.0, "y": s.y * 0.34, "s": "LIVELLO %d!" % livello, "t": 0.0, "big": true})
		coriandoli(60)
		amb += 1
		amb_t = 0.0
		annuncia_ambiente()


func b_colore(b: Dictionary) -> String:
	return String(b.get("colore", "#5b6b3a"))


func spara(c: Dictionary) -> void:
	c["fase"] = "spara"
	c["morto"] = 0.0
	combo = 0
	flash = 0.18
	scossa = 0.35
	vetro -= 1
	if "test" in OS.get_cmdline_user_args():
		print("SPARO: vetro = ", vetro)
	var fr: String = c["b"].get("frase", "")
	if fr == "" and FRASI.size() > 0:
		fr = FRASI.pick_random()
	if fr != "":
		testi.append({"x": c["x"], "y": c["y"] - c["r"] - 12, "s": "«" + fr + "»", "t": 0.0, "fumetto": true})
	var f := finestra()
	crepe.append(crea_crepa(Vector2(clamp(c["x"] + randf_range(-60, 60), f.position.x + 20, f.end.x - 20), clamp(c["y"] + randf_range(-40, 40), f.position.y + 20, f.end.y - 20))))
	if vetro <= 0:
		fine()


func crea_crepa(centro: Vector2) -> Array:
	var f := finestra()
	var linee := []
	var n := randi_range(7, 11)
	for i in n:
		var a := float(i) / n * TAU + randf_range(-0.2, 0.2)
		var l: float = randf_range(0.15, 0.35) * max(f.size.x, f.size.y)
		var p := centro
		var seg := PackedVector2Array([p])
		for j in 6:
			a += randf_range(-0.35, 0.35)
			p += Vector2(cos(a), sin(a)) * l / 6.0
			seg.append(p)
		linee.append(seg)
	return linee


func coriandoli(n: int) -> void:
	var s := get_viewport_rect().size
	for i in n:
		part.append({"p": Vector2(randf() * s.x, -10), "v": Vector2(randf_range(-60, 60), randf_range(120, 300)), "t": 0.0,
			"c": [ORO, Color("#2f9e57"), Color("#e0413a"), Color("#1f6fa5"), Color("#ff6fb1"), Color.WHITE].pick_random(), "r": randf_range(3, 6), "conf": true})


func fine() -> void:
	stato = "fine"
	if punti > record:
		record = punti
		salva_record()


# ---------------- il «battito»: gira circa 60 volte al secondo ----------------
func _process(delta: float) -> void:
	tempo += delta
	if stato == "gioco":
		aggiorna(delta)
		if "prova" in OS.get_cmdline_user_args() and cattivi.size() > 0 and randf() < 0.02:
			var c = cattivi.pick_random()
			if c["fase"] == "attende":
				colpito(c)
	for p in part:
		p["t"] += delta
		p["p"] += p["v"] * delta
		if not p.get("conf", false):
			p["v"] *= 0.9
	part = part.filter(func(p): return p["t"] < (3.0 if p.get("conf", false) else 0.7))
	for x in testi:
		x["t"] += delta
	testi = testi.filter(func(x): return x["t"] < (2.0 if x.get("big", false) else 1.4))
	scossa = max(0.0, scossa - delta)
	flash = max(0.0, flash - delta)
	queue_redraw()


func aggiorna(delta: float) -> void:
	var a := ambiente()
	var v := 6.0 * regola("velocita_treno", 0.5) * (1.0 + livello * 0.04)
	dist += v * delta
	prossimo_ogg -= delta
	if prossimo_ogg <= 0.0:
		oggetti.append(nuovo_oggetto(ZF))
		var dens: float = [1.6, 1.0, 0.7][clamp(int(a.get("densita", 2)) - 1, 0, 2)]
		prossimo_ogg = randf_range(0.12, 0.28) * dens / regola("velocita_treno", 0.5)
	for o in oggetti:
		o["z"] -= v * delta
	oggetti = oggetti.filter(func(o): return o["z"] > ZN * 0.7)
	amb_t += delta
	if amb_t > SEC_AMB:
		amb_t = 0.0
		amb += 1
		annuncia_ambiente()
	prossimo -= delta
	if prossimo <= 0.0:
		nuovo_cattivo()
		prossimo = max(0.7, 2.2 - livello * 0.15) * randf_range(0.8, 1.2)
	var V := vista()
	for c in cattivi:
		c["t"] += delta
		var o: Dictionary = c["o"]
		var k: float = min(1.0, c["t"] / c["entra"]) if c["fase"] == "entra" else 1.0
		k = 1.0 - (1.0 - k) * (1.0 - k)
		var Q := proj(V, o["X"] + c["dx"] * k, o["z"])
		var su := (1.0 - k) * 0.55 if c["fase"] == "entra" else 0.0
		c["u"] = Q.z * 1.7
		c["r"] = max(9.0, 0.24 * c["u"])
		c["piedi"] = Q.y
		c["x"] = Q.x
		c["y"] = Q.y - (1.62 - su) * c["u"]
		c["k"] = k
		if c["fase"] == "entra" and c["t"] > c["entra"]:
			c["fase"] = "attende"
		elif c["fase"] == "attende" and c["t"] > c["entra"] + c["tempo"]:
			spara(c)
		elif c["fase"] == "colpito" or c["fase"] == "spara":
			c["morto"] += delta
	cattivi = cattivi.filter(func(c): return c["morto"] < 0.6 and c["o"]["z"] > ZN * 0.8)


# ---------------- il clic (qui il gioco «reagisce», come in Lazarus) ----------------
func _unhandled_input(event: InputEvent) -> void:
	var premuto := false
	var pos := Vector2.ZERO
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		premuto = true
		pos = event.position
	elif event is InputEventScreenTouch and event.pressed:
		premuto = true
		pos = event.position
	if not premuto:
		return
	if stato != "gioco":
		nuova_partita()
		return
	part.append({"p": pos, "v": Vector2.ZERO, "t": 0.0, "c": ORO, "r": 18.0, "mira": true})
	var meglio = null
	var bd := 1e9
	for c in cattivi:
		if c["fase"] != "entra" and c["fase"] != "attende":
			continue
		var d := pos.distance_to(Vector2(c["x"], c["y"]))
		var nel_corpo: bool = abs(pos.x - c["x"]) < c["u"] * 0.38 and pos.y > c["y"] and pos.y < c["piedi"]
		if (d < c["r"] * 1.35 or nel_corpo) and d < bd:
			bd = d
			meglio = c
	if meglio != null:
		colpito(meglio)


# ---------------- il disegno (il «pennello») ----------------
func _draw() -> void:
	var s := get_viewport_rect().size
	draw_rect(Rect2(Vector2.ZERO, s), CABINA)
	var off := Vector2(randf_range(-8, 8), randf_range(-8, 8)) * scossa
	draw_set_transform(off, 0.0, Vector2.ONE)
	paesaggio()
	vetro_e_crepe()
	draw_set_transform(Vector2.ZERO, 0.0, Vector2.ONE)
	cornice()
	for p in part:
		if p.get("mira", false):
			draw_arc(p["p"], p["r"] * (1.0 + p["t"] * 3.0), 0, TAU, 24, Color(ORO, max(0.0, 1.0 - p["t"] * 2.0)), 3.0)
		else:
			draw_circle(p["p"], p["r"], Color(p["c"], max(0.0, 1.0 - p["t"] / (3.0 if p.get("conf", false) else 0.7))))
	for x in testi:
		var al: float = max(0.0, 1.0 - x["t"] / (2.0 if x.get("big", false) else 1.4))
		var sz := 54 if x.get("big", false) else (22 if x.get("fumetto", false) else 26)
		scritta(Vector2(x["x"], x["y"] - x["t"] * 30.0), x["s"], sz, Color(ORO if not x.get("fumetto", false) else Color.WHITE, al))
	if flash > 0.0:
		draw_rect(Rect2(Vector2.ZERO, s), Color(1, 0.2, 0.1, flash * 1.5))
	# il numero di versione, sempre visibile (è il tema della lezione!)
	draw_string_outline(font, Vector2(14, 34), "Treno blindato " + VERSIONE, HORIZONTAL_ALIGNMENT_LEFT, -1, 24, 4, Color.BLACK)
	draw_string(font, Vector2(14, 34), "Treno blindato " + VERSIONE, HORIZONTAL_ALIGNMENT_LEFT, -1, 24, ORO)
	if stato == "titolo":
		schermata("IL TRENO BLINDATO", "Versione Godot " + VERSIONE + " · con i personaggi della 1INF\nI cattivi saltano fuori da dietro alberi e case: cliccali prima che sparino.\nIl vetro regge %d colpi!" % int(regola("vetro", 5)), "CLICCA PER PARTIRE")
	elif stato == "fine":
		schermata("IL VETRO È ANDATO IN PEZZI!", "Punti: %d · Record: %d\n%s" % [punti, record, LODI.pick_random() if punti >= record and punti > 0 else "Riprova: il treno ha bisogno di te!"], "CLICCA PER RIPARTIRE")


func scritta(pos: Vector2, testo: String, size: int, col: Color) -> void:
	var w := 1600.0
	var p := Vector2(pos.x - w / 2.0, pos.y)
	draw_string_outline(font, p, testo, HORIZONTAL_ALIGNMENT_CENTER, w, size, max(2, size / 8), Color(0, 0, 0, col.a))
	draw_string(font, p, testo, HORIZONTAL_ALIGNMENT_CENTER, w, size, col)


func schermata(titolo: String, sotto: String, invito: String) -> void:
	var s := get_viewport_rect().size
	draw_rect(Rect2(Vector2.ZERO, s), Color(0, 0, 0, 0.62))
	scritta(Vector2(s.x / 2, s.y * 0.3), titolo, 64, ORO)
	var righe := sotto.split("\n")
	for i in righe.size():
		scritta(Vector2(s.x / 2, s.y * 0.42 + i * 34), righe[i], 24, Color.WHITE)
	var a := 0.6 + 0.4 * sin(tempo * 4.0)
	scritta(Vector2(s.x / 2, s.y * 0.72), invito, 34, Color(ORO, a))


func paesaggio() -> void:
	var V := vista()
	var f: Rect2 = V["f"]
	var a := ambiente()
	var hz: float = V["hz"]
	var bot: float = V["bot"]
	# cielo sfumato (dall'alto al basso)
	var ca := Color(a.get("cielo_alto", "#5aa0e0"))
	var cb := Color(a.get("cielo_basso", "#dceefa"))
	draw_polygon(PackedVector2Array([f.position, Vector2(f.end.x, f.position.y), Vector2(f.end.x, hz), Vector2(f.position.x, hz)]), PackedColorArray([ca, ca, cb, cb]))
	# colline lontane
	var coll := PackedVector2Array([Vector2(f.position.x, hz)])
	for i in 13:
		var xx := f.position.x + i * f.size.x / 12.0
		coll.append(Vector2(xx, hz - f.size.y * (0.05 + 0.09 * abs(sin(i * 1.7 + dist * 0.003)))))
	coll.append(Vector2(f.end.x, hz))
	draw_colored_polygon(coll, Color(a.get("lontano", "#8c97a8")))
	draw_rect(Rect2(f.position.x, hz, f.size.x, bot - hz), Color(a.get("terra", "#6a8a4a")))
	# massicciata, traversine e binari
	var p1 := proj(V, -1.3, ZF)
	var p2 := proj(V, 1.3, ZF)
	var p3 := proj(V, 1.3, ZN * 0.9)
	var p4 := proj(V, -1.3, ZN * 0.9)
	draw_colored_polygon(PackedVector2Array([Vector2(p1.x, p1.y), Vector2(p2.x, p2.y), Vector2(p3.x, p3.y), Vector2(p4.x, p4.y)]), Color("#6d665c"))
	var z := ZN * 0.9 + (1.0 - fmod(dist, 1.0))
	while z < ZF:
		var l := proj(V, -1.1, z)
		var r := proj(V, 1.1, z)
		draw_line(Vector2(l.x, l.y), Vector2(r.x, r.y), Color("#4a3324"), max(1.0, 0.18 * l.z))
		z += 1.0
	for X in [-0.75, 0.75]:
		var A := proj(V, X, ZF)
		var B := proj(V, X, ZN * 0.9)
		draw_line(Vector2(A.x, A.y), Vector2(B.x, B.y), Color("#c9ccd2"), 3.0)
	# oggetti dal più lontano al più vicino; il cattivo si disegna PRIMA del suo nascondiglio
	var ord := oggetti.duplicate()
	ord.sort_custom(func(x, y): return x["z"] > y["z"])
	for o in ord:
		if o["z"] < ZN * 0.7:
			continue
		for c in cattivi:
			if c["o"] == o:
				omino(c)
		disegna_oggetto(o, proj(V, o["X"], o["z"]))


func disegna_oggetto(o: Dictionary, P: Vector3) -> void:
	var x := P.x
	var b := P.y
	var w: float = o["w"] * P.z
	var h: float = o["h"] * P.z
	var col: Color = o["col"]
	match o["tipo"]:
		"alberi":
			draw_rect(Rect2(x - w * 0.08, b - h * 0.35, w * 0.16, h * 0.35), Color("#5a3b22"))
			draw_colored_polygon(PackedVector2Array([Vector2(x - w / 2, b - h * 0.3), Vector2(x, b - h), Vector2(x + w / 2, b - h * 0.3)]), col)
			draw_colored_polygon(PackedVector2Array([Vector2(x - w * 0.42, b - h * 0.55), Vector2(x, b - h * 1.08), Vector2(x + w * 0.42, b - h * 0.55)]), col.lightened(0.08))
		"case":
			draw_rect(Rect2(x - w / 2, b - h, w, h), col)
			draw_colored_polygon(PackedVector2Array([Vector2(x - w * 0.58, b - h), Vector2(x, b - h * 1.5), Vector2(x + w * 0.58, b - h)]), o.get("tetto", Color("#8a2f22")))
			draw_rect(Rect2(x + o["lato"] * w * 0.25 - w * 0.08, b - h * 0.7, w * 0.16, h * 0.22), Color("#ffe39a"))
			draw_rect(Rect2(x - w * 0.08, b - h * 0.38, w * 0.16, h * 0.38), Color("#5a3b22"))
		"palazzi":
			draw_rect(Rect2(x - w / 2, b - h, w, h), col)
			var st: float = max(6.0, P.z * 0.5)
			var yy := b - h + st
			while yy < b - st:
				var xx := x - w / 2 + st * 0.6
				while xx < x + w / 2 - st * 0.6:
					if int(xx * 7 + yy * 13) % 4 == 0:
						draw_rect(Rect2(xx, yy, st * 0.5, st * 0.6), Color(1, 0.86, 0.47, 0.6))
					xx += st * 1.2
				yy += st * 1.4
		"rocce":
			draw_colored_polygon(PackedVector2Array([Vector2(x - w / 2, b), Vector2(x - w * 0.3, b - h * 0.8), Vector2(x, b - h), Vector2(x + w * 0.35, b - h * 0.7), Vector2(x + w / 2, b)]), col)
		"rottame":
			draw_colored_polygon(PackedVector2Array([Vector2(x - w / 2, b), Vector2(x - w * 0.35, b - h * 0.7), Vector2(x - w * 0.1, b - h * 0.45), Vector2(x + w * 0.05, b - h), Vector2(x + w * 0.3, b - h * 0.55), Vector2(x + w / 2, b - h * 0.3), Vector2(x + w / 2, b)]), col)
			var tf := fmod(tempo / 0.6 + o["X"], 3.0)
			draw_circle(Vector2(x + w * 0.05, b - h - tf * h * 0.6), w * (0.12 + tf * 0.08), Color(0.24, 0.24, 0.24, 0.35 * (1.0 - tf / 3.0)))
		"barile":
			draw_rect(Rect2(x - w / 2, b - h, w, h), col)
			draw_rect(Rect2(x - w / 2, b - h * 0.7, w, h * 0.08), Color(0, 0, 0, 0.3))
			draw_rect(Rect2(x - w / 2, b - h * 0.3, w, h * 0.08), Color(0, 0, 0, 0.3))
		_:
			draw_arc(Vector2(x, b - h), w / 2, PI, TAU, 16, Color(1, 1, 1, 0.6), max(1.0, P.z * 0.06))


## L'omino intero (corpo, gambe, arma, testa) che esce dal nascondiglio
func omino(c: Dictionary) -> void:
	var u: float = c["u"]
	var x: float = c["x"]
	var y: float = c["y"]
	var r: float = c["r"]
	var b: Dictionary = c["b"]
	var alfa := 1.0
	if c["fase"] == "colpito":
		alfa = max(0.0, 1.0 - c["morto"] / 0.5)
	var vestito := Color(b_colore(b), alfa)
	var pelle := Color("#d9a27a", alfa)
	var dir: float = -c["o"]["lato"]
	var ya := y + r
	# gambe
	draw_line(Vector2(x - u * 0.09, ya + u * 0.62), Vector2(x - u * 0.12, c["piedi"]), vestito.darkened(0.2), u * 0.13)
	draw_line(Vector2(x + u * 0.09, ya + u * 0.62), Vector2(x + u * 0.12, c["piedi"]), vestito.darkened(0.2), u * 0.13)
	# corpo
	draw_colored_polygon(PackedVector2Array([Vector2(x - u * 0.22, ya + u * 0.05), Vector2(x + u * 0.22, ya + u * 0.05), Vector2(x + u * 0.19, ya + u * 0.66), Vector2(x - u * 0.19, ya + u * 0.66)]), vestito)
	# braccio e arma puntata verso il treno
	var mano := Vector2(x + dir * u * 0.45, ya + u * 0.3)
	draw_line(Vector2(x, ya + u * 0.2), mano, vestito.darkened(0.1), u * 0.1)
	draw_line(mano, mano + Vector2(dir * u * 0.25, 0), Color(0.1, 0.1, 0.1, alfa), u * 0.08)
	if c["fase"] == "spara":
		draw_circle(mano + Vector2(dir * u * 0.32, 0), u * 0.16, Color(1, 0.9, 0.47, max(0.0, 1.0 - c["morto"] * 2.0)))
	# testa: se il cattivo ha l'immagine di un ragazzo, la testa è quella immagine
	if b.has("tex"):
		var tex: Texture2D = b["tex"]
		var lato := r * 2.8
		var asp: float = float(tex.get_width()) / maxf(1.0, float(tex.get_height()))
		var w: float = lato * (asp if asp < 1.0 else 1.0)
		var h: float = lato / (asp if asp > 1.0 else 1.0)
		draw_texture_rect(tex, Rect2(x - w / 2.0, y - h * 0.62, w, h), false, Color(1, 1, 1, alfa))
		if String(b.get("nome", "")) != "" and c["fase"] != "colpito":
			scritta(Vector2(x, y - h * 0.8), b["nome"], 15, Color.WHITE)
	else:
		draw_circle(Vector2(x, y), r, pelle)
		if int(b.get("cappello", 0)) == 1:
			draw_rect(Rect2(x - r * 1.05, y - r * 0.62, r * 2.1, r * 0.18), Color(0.13, 0.13, 0.13, alfa))
			draw_rect(Rect2(x - r * 0.6, y - r * 1.25, r * 1.2, r * 0.66), Color(0.13, 0.13, 0.13, alfa))
		var arrabbiato: bool = c["fase"] == "attende" and c["t"] > c["entra"] + c["tempo"] * 0.55
		var occhi := int(b.get("occhi", 2))
		var dx := [0.0] if occhi == 1 else ([-0.38, 0.38] if occhi == 2 else [-0.5, 0.0, 0.5])
		for d in dx:
			draw_circle(Vector2(x + d * r, y - r * 0.15), r * 0.19, Color(1, 1, 1, alfa))
			draw_circle(Vector2(x + d * r + sin(c["t"] * 6.0) * r * 0.05, y - r * 0.15), r * 0.09, Color(0.07, 0.07, 0.07, alfa))
		if int(b.get("cappello", 0)) == 2:
			draw_rect(Rect2(x - r * 0.95, y + r * 0.12, r * 1.9, r * 0.6), Color(0.75, 0.22, 0.17, alfa))
		elif arrabbiato:
			draw_circle(Vector2(x, y + r * 0.42), r * 0.25, Color(0.23, 0.05, 0.09, alfa))
		else:
			draw_arc(Vector2(x, y + r * 0.25), r * 0.3, 0.2, PI - 0.2, 10, Color(0.23, 0.05, 0.09, alfa), max(1.0, r * 0.08))
		# nome del cattivo (chi l'ha inventato è nei crediti)
		if String(b.get("nome", "")) != "" and c["fase"] != "colpito":
			scritta(Vector2(x, y - r * 1.5), b["nome"], 15, Color.WHITE)
	# barra del tempo: quando è piena, spara!
	if c["fase"] == "attende":
		var k: float = clamp((c["t"] - c["entra"]) / c["tempo"], 0.0, 1.0)
		var bw := r * 2.4
		draw_rect(Rect2(x - bw / 2, y - r * 2.1, bw, 5), Color(0, 0, 0, 0.5))
		draw_rect(Rect2(x - bw / 2, y - r * 2.1, bw * k, 5), Color("#2f9e57").lerp(Color("#e0413a"), k))
	elif c["fase"] == "entra" and c["k"] > 0.5:
		scritta(Vector2(x, y - r * 2.6), "!", int(r * 1.4), Color("#ff4d4d"))


func vetro_e_crepe() -> void:
	for cr in crepe:
		for seg in cr:
			draw_polyline(seg, Color(1, 1, 1, 0.85), 2.0)


func cornice() -> void:
	var s := get_viewport_rect().size
	var f := finestra()
	# la cabina copre tutto quello che sta fuori dal vetro
	draw_rect(Rect2(0, 0, s.x, f.position.y), CABINA)
	draw_rect(Rect2(0, f.end.y, s.x, s.y - f.end.y), CABINA)
	draw_rect(Rect2(0, 0, f.position.x, s.y), CABINA)
	draw_rect(Rect2(f.end.x, 0, s.x - f.end.x, s.y), CABINA)
	draw_rect(f, Color("#6b5440"), false, 6.0)
	# cruscotto
	var y := f.end.y + 46
	scritta(Vector2(s.x * 0.18, y), "PUNTI %d" % punti, 30, ORO)
	scritta(Vector2(s.x * 0.5, y), "LIVELLO %d · %s" % [livello, String(ambiente().get("nome", "")).to_upper()], 26, Color.WHITE)
	var vmax := int(regola("vetro", 5))
	for i in vmax:
		var col := Color("#6fd3ff") if i < vetro else Color("#3a2c20")
		draw_rect(Rect2(s.x * 0.76 + i * 30, y - 22, 24, 24), col)
	scritta(Vector2(s.x * 0.5, y + 44), "Record %d · Godot v2.0 · cattivi della 1INF: %s" % [record, ", ".join(CATTIVI.map(func(b): return "%s (%s)" % [b.get("nome", ""), b.get("autore", "")]))], 16, Color("#d8c8b4"))
	scritta(Vector2(s.x * 0.5, 30), "IL TRENO BLINDATO", 22, ORO)
