extends CanvasLayer
## LE SCHERMATE del treno: inizio, fine partita, «Chi l'ha fatto», «I personaggi», «Facce della classe»,
## il bottone Pausa e la scritta della versione in basso a destra.
##
## Ponte da Lazarus: qui ci sono i «componenti» (Button = TButton, LineEdit = TEdit, Label con il suo testo
## come la Caption). Invece di trascinarli su un Form, li creiamo con il codice, uno sotto l'altro,
## dentro dei contenitori (VBoxContainer = in colonna, HFlowContainer = in riga che va a capo).
## Il collegamento al clic (l'evento OnClick) si fa con: bottone.pressed.connect(funzione).

const ORO := Color("#ffd34d")
const VERDE := Color("#2f9e57")
const SFONDO := Color(20 / 255.0, 14 / 255.0, 10 / 255.0, 0.9)
const GALLERIA_PERSONAGGI := "Ancora nessun personaggio della classe: arrivano con le Pull Request!"

var gioco          # il motore (treno.gd)
var mem            # la memoria (memoria.gd)
var radice: Control
var schermi := {}
var schermo_attivo := "inizio"
var bottoni := {}  # i bottoni con un nome (servono anche alla prova automatica)
var misure := []   # [nodo, larghezza massima]: si adattano alla larghezza dello schermo
var caratteri := [] # [LabelSettings o Button, minimo, % della larghezza, massimo]: come clamp() del CSS
var w_titolo: Label
var w_sotto: Label
var w_record: RichTextLabel
var w_top_inizio: RichTextLabel
var w_cattivi: VBoxContainer
var w_controllo: RichTextLabel
var w_titolo_fine: Label
var w_punti: Label
var w_lode: RichTextLabel
var w_stat: Label
var w_salva: HBoxContainer
var w_nome: LineEdit
var w_top_fine: RichTextLabel
var w_squadre: RichTextLabel
var w_autori: HFlowContainer
var w_galleria: HFlowContainer
var w_anteprime: HFlowContainer
var w_msg_foto: Label
var bt_pausa: Button
var velo_pausa: Control
var w_ver: Label
var sfondo_copertina: TextureRect
var id_top := 0.0
var cb_foto            # la «richiamata» che il browser usa quando le foto sono pronte
var dialogo_foto: FileDialog


func _ready() -> void:
	mem = gioco.mem
	radice = Control.new()
	radice.set_anchors_preset(Control.PRESET_FULL_RECT)
	radice.mouse_filter = Control.MOUSE_FILTER_IGNORE
	var tema := Theme.new()
	tema.default_font = gioco.FONT[600]
	tema.default_font_size = 16
	radice.theme = tema
	add_child(radice)
	costruisci_inizio()
	costruisci_fine()
	costruisci_personaggi()
	costruisci_facce()
	costruisci_crediti()
	# v0.23 (PR di Lina A.): il bottone Pausa e il velo con la scritta PAUSA
	velo_pausa = ColorRect.new()
	velo_pausa.color = Color(0, 0, 0, 0.55)
	velo_pausa.set_anchors_preset(Control.PRESET_FULL_RECT)
	velo_pausa.mouse_filter = Control.MOUSE_FILTER_IGNORE
	var scritta := etichetta("PAUSA", 72, ORO, 900, 2000)
	scritta.set_anchors_preset(Control.PRESET_FULL_RECT)
	scritta.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	caratteri.append([scritta.label_settings, 36, 0.09, 72])
	misure.erase(misure.back())
	velo_pausa.add_child(scritta)
	velo_pausa.visible = false
	radice.add_child(velo_pausa)
	bt_pausa = bottone("Pausa", "pausa", Color("#1f6fa5"), Color("#123f60"), 16, Vector2(14, 6), 3)
	bt_pausa.set_anchors_preset(Control.PRESET_TOP_RIGHT)
	bt_pausa.grow_horizontal = Control.GROW_DIRECTION_BEGIN
	bt_pausa.offset_left = -8
	bt_pausa.offset_right = -8
	bt_pausa.offset_top = 6
	bt_pausa.visible = false
	bt_pausa.pressed.connect(func(): gioco.pausa())
	radice.add_child(bt_pausa)
	# la versione, piccola in basso a destra (come nella versione HTML)
	w_ver = Label.new()
	w_ver.add_theme_font_size_override("font_size", 12)
	w_ver.modulate = Color(1, 1, 1, 0.7)
	w_ver.set_anchors_preset(Control.PRESET_BOTTOM_RIGHT)
	w_ver.grow_horizontal = Control.GROW_DIRECTION_BEGIN
	w_ver.grow_vertical = Control.GROW_DIRECTION_BEGIN
	w_ver.offset_right = -10
	w_ver.offset_bottom = -4
	w_ver.mouse_filter = Control.MOUSE_FILTER_IGNORE
	radice.add_child(w_ver)
	get_viewport().size_changed.connect(aggiorna_misure)
	if OS.has_feature("web"):
		prepara_foto_web()
	mostra("inizio")


# =====================================================================
#   I «COMPONENTI» (piccole fabbriche di bottoni, scritte, contenitori)
# =====================================================================
func stile(fondo: Color, ombra: Color, raggio := 14, sotto := 5, margini := Vector2(26, 14)) -> StyleBoxFlat:
	var s := StyleBoxFlat.new()
	s.bg_color = fondo
	s.border_color = ombra
	s.border_width_bottom = sotto
	s.set_corner_radius_all(raggio)
	s.content_margin_left = margini.x
	s.content_margin_right = margini.x
	s.content_margin_top = margini.y
	s.content_margin_bottom = margini.y
	return s


## Un bottone (come TButton): verde se è quello principale, marrone se è secondario.
func bottone(testo: String, nome: String, fondo := VERDE, ombra := Color("#1d6b3a"), size := 24, margini := Vector2(26, 14), sotto := 5) -> Button:
	var b := Button.new()
	b.text = testo
	b.name = nome
	var normale := stile(fondo, ombra, 14, sotto, margini)
	var sopra := stile(fondo.lightened(0.08), ombra, 14, sotto, margini)
	var premuto := stile(fondo.darkened(0.05), ombra, 14, 0, margini)
	premuto.content_margin_bottom += sotto
	b.add_theme_stylebox_override("normal", normale)
	b.add_theme_stylebox_override("hover", sopra)
	b.add_theme_stylebox_override("pressed", premuto)
	b.add_theme_stylebox_override("hover_pressed", premuto)
	b.add_theme_stylebox_override("focus", StyleBoxEmpty.new())
	for c in ["font_color", "font_hover_color", "font_pressed_color", "font_focus_color", "font_hover_pressed_color"]:
		b.add_theme_color_override(c, Color.WHITE)
	b.add_theme_font_override("font", gioco.FONT[800])
	b.add_theme_font_size_override("font_size", size)
	b.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	b.mouse_default_cursor_shape = Control.CURSOR_POINTING_HAND
	bottoni[nome] = b
	return b


func secondario(testo: String, nome: String) -> Button:
	return bottone(testo, nome, Color("#4a3a2c"), Color("#2a2018"), 17, Vector2(18, 10))


## Una scritta (come una Label di Lazarus con la sua Caption), che va a capo da sola.
func etichetta(testo: String, size: int, colore := Color.WHITE, peso := 600, larga := 560) -> Label:
	var l := Label.new()
	l.text = testo
	var ls := LabelSettings.new()
	ls.font = gioco.FONT[peso]
	ls.font_size = size
	ls.font_color = colore
	l.label_settings = ls
	l.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	l.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	l.mouse_filter = Control.MOUSE_FILTER_IGNORE
	misure.append([l, larga])
	return l


## Un testo «ricco»: con grassetti e colori, come l'HTML (si scrive con i tag [b] e [color]).
func ricco(larga := 560, size := 16) -> RichTextLabel:
	var r := RichTextLabel.new()
	r.bbcode_enabled = true
	r.fit_content = true
	r.scroll_active = false
	r.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	r.add_theme_font_override("normal_font", gioco.FONT[600])
	r.add_theme_font_override("bold_font", gioco.FONT[900])
	r.add_theme_font_size_override("normal_font_size", size)
	r.add_theme_font_size_override("bold_font_size", size)
	r.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	r.mouse_filter = Control.MOUSE_FILTER_IGNORE
	misure.append([r, larga])
	return r


func riga(larga := 900) -> HFlowContainer:
	var r := HFlowContainer.new()
	r.alignment = FlowContainer.ALIGNMENT_CENTER
	r.add_theme_constant_override("h_separation", 10)
	r.add_theme_constant_override("v_separation", 10)
	r.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	r.mouse_filter = Control.MOUSE_FILTER_IGNORE
	misure.append([r, larga])
	return r


## Un «gettone» con una scritta (come i chip della versione HTML).
func gettone(testo: String, bordo := Color("#6b5440"), errore := false) -> PanelContainer:
	var p := PanelContainer.new()
	var s := StyleBoxFlat.new()
	s.bg_color = Color("#2c2119")
	s.border_color = Color("#e0413a") if errore else bordo
	s.set_border_width_all(1)
	s.set_corner_radius_all(999)
	s.content_margin_left = 10
	s.content_margin_right = 10
	s.content_margin_top = 4
	s.content_margin_bottom = 4
	p.add_theme_stylebox_override("panel", s)
	var l := Label.new()
	l.text = testo
	l.add_theme_font_size_override("font_size", 14)
	if errore:
		l.add_theme_color_override("font_color", Color("#ffb0aa"))
	p.add_child(l)
	p.mouse_filter = Control.MOUSE_FILTER_IGNORE
	return p


## Una schermata intera: sfondo scuro, si scorre col dito se il contenuto è lungo, tutto in colonna al centro.
func nuovo_schermo(id: String, sfondo := SFONDO, in_alto := false) -> VBoxContainer:
	var p := Panel.new()
	p.set_anchors_preset(Control.PRESET_FULL_RECT)
	var st := StyleBoxFlat.new()
	st.bg_color = sfondo
	p.add_theme_stylebox_override("panel", st)
	radice.add_child(p)
	schermi[id] = p
	var sc := ScrollContainer.new()
	sc.set_anchors_preset(Control.PRESET_FULL_RECT)
	sc.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	p.add_child(sc)
	var m := MarginContainer.new()
	for lato in ["left", "right", "top", "bottom"]:
		m.add_theme_constant_override("margin_" + lato, 16)
	m.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	sc.add_child(m)
	var v := VBoxContainer.new()
	v.alignment = BoxContainer.ALIGNMENT_BEGIN if in_alto else BoxContainer.ALIGNMENT_CENTER
	v.add_theme_constant_override("separation", 12)
	v.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	v.size_flags_vertical = Control.SIZE_EXPAND_FILL
	m.add_child(v)
	p.set_meta("contenuto", m)
	return v


func h1(testo: String, size_fissa := 0) -> Label:
	var l := etichetta(testo, 56 if size_fissa == 0 else size_fissa, ORO, 900, 900)
	l.label_settings.shadow_color = Color("#8a3b12")
	l.label_settings.shadow_offset = Vector2(0, 4)
	l.label_settings.shadow_size = 1
	if size_fissa == 0:
		caratteri.append([l.label_settings, 30, 0.08, 56])
	return l


func sub(testo := "", size := 20) -> Label:
	var l := etichetta(testo, size, Color(1, 1, 1, 0.92), 600, 560)
	caratteri.append([l.label_settings, 15, 0.04, size])
	return l


func esc(s) -> String:
	return str(s).replace("[", "[lb]")


# =====================================================================
#   LE SCHERMATE
# =====================================================================
func costruisci_inizio() -> void:
	var v := nuovo_schermo("inizio", Color(0, 0, 0, 0))
	var p: Panel = schermi["inizio"]
	# lo sfondo: l'immagine di copertina della classe (se c'è) e un velo scuro sfumato sopra al treno che corre
	if gioco.COPERTINA:
		sfondo_copertina = TextureRect.new()
		sfondo_copertina.texture = gioco.COPERTINA
		sfondo_copertina.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		sfondo_copertina.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
		sfondo_copertina.set_anchors_preset(Control.PRESET_FULL_RECT)
		sfondo_copertina.mouse_filter = Control.MOUSE_FILTER_IGNORE
		p.add_child(sfondo_copertina)
		p.move_child(sfondo_copertina, 0)
	var velo := TextureRect.new()
	var gr := Gradient.new()
	gr.set_color(0, Color(20 / 255.0, 14 / 255.0, 10 / 255.0, 0.55))
	gr.set_color(1, Color(20 / 255.0, 14 / 255.0, 10 / 255.0, 0.92))
	var gt := GradientTexture2D.new()
	gt.gradient = gr
	gt.fill_from = Vector2(0, 0)
	gt.fill_to = Vector2(0, 1)
	gt.width = 4
	gt.height = 64
	velo.texture = gt
	velo.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	velo.stretch_mode = TextureRect.STRETCH_SCALE
	velo.set_anchors_preset(Control.PRESET_FULL_RECT)
	velo.mouse_filter = Control.MOUSE_FILTER_IGNORE
	p.add_child(velo)
	p.move_child(velo, 1 if gioco.COPERTINA else 0)
	w_titolo = h1("IL TRENO BLINDATO")
	v.add_child(w_titolo)
	var base := etichetta("classe 3INF · fork della base del prof · su Godot", 15, ORO, 700)
	v.add_child(base)
	w_sotto = sub()
	v.add_child(w_sotto)
	var r := riga()
	var parti := bottone("PARTI!", "parti")
	caratteri.append([parti, 18, 0.05, 24])
	parti.pressed.connect(func(): gioco.parti())
	r.add_child(parti)
	var cred := secondario("Chi l'ha fatto", "crediti")
	cred.pressed.connect(func(): mostra("crediti"))
	r.add_child(cred)
	var pers := secondario("I personaggi", "personaggi")
	pers.pressed.connect(func(): mostra("personaggi"))
	r.add_child(pers)
	var fc := secondario("Facce della classe", "facce")
	fc.pressed.connect(func():
		mostra_facce()
		mostra("facce"))
	r.add_child(fc)
	v.add_child(r)
	w_record = ricco(560, 20)
	v.add_child(w_record)
	w_top_inizio = ricco(520, 15)
	v.add_child(w_top_inizio)
	w_cattivi = VBoxContainer.new()
	w_cattivi.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	v.add_child(w_cattivi)
	w_controllo = ricco(560, 13)
	v.add_child(w_controllo)
	var link := LinkButton.new()
	link.text = "Tutte le versioni del gioco"
	link.name = "versioni"
	link.add_theme_color_override("font_color", ORO)
	link.add_theme_color_override("font_hover_color", ORO.lightened(0.2))
	link.add_theme_font_override("font", gioco.FONT[800])
	link.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	link.pressed.connect(apri_versioni)
	bottoni["versioni"] = link
	v.add_child(link)


func costruisci_fine() -> void:
	var v := nuovo_schermo("fine")
	w_titolo_fine = etichetta("", 22, Color("#ff8d86"), 800, 900)
	v.add_child(w_titolo_fine)
	w_punti = etichetta("0", 80, ORO, 900, 900)
	caratteri.append([w_punti.label_settings, 40, 0.12, 80])
	v.add_child(w_punti)
	w_lode = ricco(560, 18)
	v.add_child(w_lode)
	w_stat = sub("", 17)
	v.add_child(w_stat)
	# v0.10-v0.11: il soprannome per i migliori punteggi (mai nome e cognome)
	w_salva = HBoxContainer.new()
	w_salva.alignment = BoxContainer.ALIGNMENT_CENTER
	w_salva.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	w_salva.add_theme_constant_override("separation", 6)
	w_nome = LineEdit.new()
	w_nome.placeholder_text = "Il tuo soprannome"
	w_nome.max_length = 12
	w_nome.custom_minimum_size = Vector2(180, 0)
	var sn := StyleBoxFlat.new()
	sn.bg_color = Color.WHITE
	sn.set_corner_radius_all(10)
	sn.content_margin_left = 10
	sn.content_margin_right = 10
	sn.content_margin_top = 10
	sn.content_margin_bottom = 10
	w_nome.add_theme_stylebox_override("normal", sn)
	w_nome.add_theme_stylebox_override("focus", sn)
	w_nome.add_theme_color_override("font_color", Color("#111111"))
	w_nome.add_theme_color_override("font_placeholder_color", Color("#777777"))
	w_nome.add_theme_color_override("caret_color", Color("#111111"))
	w_nome.add_theme_font_size_override("font_size", 18)
	w_nome.text_submitted.connect(func(_t): salva_top())
	w_salva.add_child(w_nome)
	var ok := bottone("Salva nei migliori", "salva", VERDE, Color("#1d6b3a"), 18, Vector2(14, 8))
	ok.pressed.connect(salva_top)
	w_salva.add_child(ok)
	v.add_child(w_salva)
	w_top_fine = ricco(640, 16)
	v.add_child(w_top_fine)
	var r := riga()
	var ancora := bottone("RIPARTI", "riparti")
	caratteri.append([ancora, 18, 0.05, 24])
	ancora.pressed.connect(func(): gioco.parti())
	r.add_child(ancora)
	var menu := secondario("Menu", "menu")
	menu.pressed.connect(func():
		aggiorna_record()
		mostra("inizio"))
	r.add_child(menu)
	v.add_child(r)


func costruisci_personaggi() -> void:
	var v := nuovo_schermo("personaggi", SFONDO, true)
	v.add_child(h1("I PERSONAGGI", 32))
	v.add_child(sub("I personaggi della classe, disegnati con l'intelligenza artificiale. Le loro facce compaiono nel gioco."))
	w_galleria = riga(900)
	v.add_child(w_galleria)
	if gioco.PERSONAGGI.is_empty():
		v.add_child(etichetta(GALLERIA_PERSONAGGI, 14, Color(1, 1, 1, 0.8)))
	for p in gioco.PERSONAGGI:
		var c := VBoxContainer.new()
		c.custom_minimum_size = Vector2(200, 0)
		var cornice := PanelContainer.new()
		var s := StyleBoxFlat.new()
		s.bg_color = Color("#2c2119")
		s.border_color = ORO
		s.set_border_width_all(3)
		s.set_corner_radius_all(12)
		cornice.add_theme_stylebox_override("panel", s)
		var im := TextureRect.new()
		if p.tex:
			im.texture = p.tex
			im.custom_minimum_size = Vector2(194, 194.0 * p.tex.get_height() / max(1, p.tex.get_width()))
		else:
			im.custom_minimum_size = Vector2(194, 194)
		im.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		im.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		cornice.add_child(im)
		c.add_child(cornice)
		var n := etichetta(p.nome, 16, Color.WHITE, 800, 200)
		c.add_child(n)
		c.add_child(etichetta(p.ruolo, 13, Color(1, 1, 1, 0.8), 600, 200))
		w_galleria.add_child(c)
	var ind := bottone("Indietro", "indietro")
	ind.pressed.connect(func(): mostra("inizio"))
	v.add_child(ind)


func costruisci_facce() -> void:
	var v := nuovo_schermo("facce")
	v.add_child(h1("FACCE DELLA CLASSE", 32))
	var t := ricco(560, 18)
	t.text = "[center]Le foto restano [b]solo su questo dispositivo[/b]: non vanno su Internet e non finiscono su GitHub. Solo foto di chi ha detto di sì.[/center]"
	v.add_child(t)
	var r := riga()
	var sc := bottone("Scegli le foto", "scegli_foto")
	sc.pressed.connect(scegli_foto)
	r.add_child(sc)
	var tg := secondario("Cancella le foto", "togli_foto")
	tg.pressed.connect(func():
		mem.scrivi("foto", [])
		gioco.carica_facce()
		mostra_facce())
	r.add_child(tg)
	v.add_child(r)
	w_anteprime = riga(640)
	v.add_child(w_anteprime)
	w_msg_foto = etichetta("", 13, Color(1, 1, 1, 0.8))
	v.add_child(w_msg_foto)
	var fatto := bottone("Fatto", "fatto")
	fatto.pressed.connect(func(): mostra("inizio"))
	v.add_child(fatto)


func costruisci_crediti() -> void:
	var v := nuovo_schermo("crediti")
	v.add_child(h1("CHI L'HA FATTO", 34))
	w_squadre = ricco(560, 18)
	v.add_child(w_squadre)
	w_autori = riga(640)
	v.add_child(w_autori)
	var storia := ricco(600, 15)
	storia.text = "[center][b][color=#ffd34d]La storia di questa versione[/color][/b]\nQuesto è il [b]treno della 3INF[/b], versione %s, fatto con il motore Godot. È un fork pulito della base del prof. Nicola Regge (v1.0), che viene dal gioco della classe 2INF (versione HTML 0.31). Da qui la 3INF aggiunge i suoi pezzi con le Pull Request: regole, ambienti, cattivi. Versione 2.0 perché è cambiato il motore (prima il treno della 3INF era in HTML).[/center]" % gioco.VERSIONE.versione
	v.add_child(storia)
	var p := etichetta("Ogni pezzo arriva con una Pull Request e viene unito (merge) nel progetto. La storia è su GitHub, nel repository del corso: Insights › Network.", 13, Color(1, 1, 1, 0.8))
	v.add_child(p)
	var b := bottone("Torna al treno", "torna")
	b.pressed.connect(func(): mostra("inizio"))
	v.add_child(b)


# =====================================================================
#   COSA SI VEDE (come mostra() della versione HTML)
# =====================================================================
func mostra(id: String) -> void:
	schermo_attivo = id
	for k in schermi:
		schermi[k].visible = k == id
	gioco.mirino(id == "")
	if id != "" and schermi.has(id):
		var sc: ScrollContainer = schermi[id].get_child(schermi[id].get_child_count() - 1)
		sc.scroll_vertical = 0
	aggiorna_misure()


func prepara_schermate() -> void:
	var V: Dictionary = gioco.VERSIONE
	w_ver.text = "versione " + str(V.versione) + (" · " + str(V.nome) if str(V.nome) != "" else "")
	if OS.has_feature("web"):
		JavaScriptBridge.eval("document.title=%s" % JSON.stringify(str(V.get("titolo", "Il treno blindato"))), true)
	else:
		get_window().title = str(V.get("titolo", "Il treno blindato"))
	w_titolo.text = gioco.TX.titolo
	w_sotto.text = gioco.TX.sottotitolo
	aggiorna_record()
	aggiorna_top()
	for n in w_cattivi.get_children():
		n.queue_free()
	var CATTIVI: Array = gioco.CATTIVI
	CATTIVI.sort_custom(func(a, b): return a.pc < b.pc)
	if CATTIVI.size() > 0:
		var t := ricco(560, 16)
		t.text = "[center]Cattivi della classe: [b]%d[/b][/center]" % CATTIVI.size()
		w_cattivi.add_child(t)
		var r := riga(640)
		for c in CATTIVI:
			r.add_child(gettone("PC %d · %s" % [c.pc, c.nome], Color(c.colore)))
		w_cattivi.add_child(r)
	else:
		w_cattivi.add_child(etichetta("Ancora nessun cattivo della classe: arrivano con le Pull Request!", 13, Color(1, 1, 1, 0.8)))
	var E: Array = gioco.ERRORI
	if E.size() > 0:
		var s := "[center][b][color=#ffb0aa]Controllo dei file: %d da sistemare[/color][/b]" % E.size()
		for e in E:
			s += "\n[color=#ffb0aa]• " + esc(e) + "[/color]"
		w_controllo.text = s + "[/center]"
	else:
		w_controllo.text = "[center][color=#ffffffcc]Controllo dei file: tutto a posto.[/color][/center]"
	var nomi := []
	for k in gioco.PERC.ambienti:
		nomi.append(esc(gioco.AMB[k].nome))
	var sq := "[center]Percorso: " + " › ".join(nomi)
	for s in gioco.SQUADRE:
		sq += "\n[b]" + esc(s.sq) + "[/b]" + (": " + ", ".join(s.aut.map(esc)) if s.aut.size() > 0 else "")
	w_squadre.text = sq + "[/center]"
	for c in CATTIVI:
		w_autori.add_child(gettone("PC %d › %s" % [c.pc, c.nome]))
	aggiorna_misure()


func aggiorna_record() -> void:
	var r := int(mem.leggi("record", 0))
	w_record.text = ("[center]Il tuo record: [b][color=#ffd34d]%d[/color][/b][/center]" % r) if r > 0 else ""
	w_record.visible = r > 0


func top_lista() -> Array:
	var t = mem.leggi("top", [])
	return t.filter(func(x): return x is Dictionary) if t is Array else []


func miglior_punteggio() -> int:
	var t := top_lista()
	return int(t[0].get("p", 0)) if t.size() > 0 else 0


func top_testo(titolo: String) -> String:
	var t := top_lista()
	var h := ""
	if t.size() > 0:
		h += "[b][color=#ffd34d]" + titolo + "[/color][/b]"
		for i in t.size():
			h += "\n%d. %s — [b]%d[/b] [color=#ffffffb3](v%s)[/color]" % [i + 1, esc(t[i].get("n", "")), int(t[i].get("p", 0)), esc(t[i].get("v", ""))]
	var RC: Array = gioco.RECORD_CLASSE
	if RC.size() > 0:
		h += ("\n\n" if h != "" else "") + "[b][color=#7be08f]Record della classe[/color][/b]"
		for i in RC.size():
			h += "\n%d. %s — [b]%d[/b]" % [i + 1, esc(RC[i].squadra), RC[i].punti]
	return "[center]" + h + "[/center]" if h != "" else ""


func aggiorna_top() -> void:
	w_top_inizio.text = top_testo("I migliori punteggi su questo dispositivo")
	w_top_inizio.visible = w_top_inizio.text != ""


## v0.11: il punteggio si salva subito (come «Anonimo»); il soprannome si può scrivere dopo.
func salva_subito(p: int) -> bool:
	var t := top_lista()
	id_top = float(int(Time.get_unix_time_from_system() * 1000.0))
	t.append({"id": id_top, "n": "Anonimo", "p": p, "v": str(gioco.VERSIONE.versione)})
	t.sort_custom(func(a, b): return float(a.get("p", 0)) > float(b.get("p", 0)))
	t = t.slice(0, 10)
	mem.scrivi("top", t)
	return t.any(func(x): return float(x.get("id", 0)) == id_top)


func salva_top() -> void:
	var n := w_nome.text.strip_edges().substr(0, 12)
	if n == "":
		n = "Anonimo"
	var t := top_lista()
	for x in t:
		if float(x.get("id", 0)) == id_top:
			x.n = n
	mem.scrivi("top", t)
	mem.scrivi_testo("treno-3inf-v2-soprannome", n)
	w_salva.visible = false
	w_top_fine.text = top_testo("I migliori punteggi")
	aggiorna_top()


func fine_partita(S: Dictionary) -> void:
	var r := int(mem.leggi("record", 0))
	var p: int = S.punti
	var nuovo := p > r
	var entra := p > 0 and salva_subito(p)
	var sop = mem.leggi_testo("treno-3inf-v2-soprannome")
	w_nome.text = sop if sop is String else ""
	w_salva.visible = entra
	w_top_fine.text = top_testo("I migliori punteggi")
	if nuovo:
		mem.scrivi("record", p)
	w_punti.text = str(p)
	# v0.29 (PR di Giorgio A.): statistiche a fine partita
	var sp: int = S.spari
	var ab: int = S.abbattuti
	var prec := roundi(ab * 100.0 / sp) if sp > 0 else 0
	w_stat.text = "Cattivi colpiti: %d · Colpi a vuoto: %d · Precisione: %d%%" % [ab, max(0, sp - ab), prec]
	w_titolo_fine.text = gioco.TX.fine
	w_lode.text = "[center]" + ("[b][color=#7be08f]" + esc(gioco.TX.record) + "[/color][/b]\n" if nuovo else "") + "Cattivi fermati: [b]%d[/b] · km [b]%d[/b]\n" % [ab, int(S.km)] + esc(gioco.TX.lodi.pick_random()) + "[/center]"
	if nuovo or S.livello > 2:
		gioco.coriandoli(140)
		gioco.suoni.suona("vittoria")
	mostra("fine")


func aggiorna_pausa(p: bool) -> void:
	bt_pausa.text = "Riprendi" if p else "Pausa"
	velo_pausa.visible = p


func bottone_pausa(visibile: bool) -> void:
	if bt_pausa.visible != visibile:
		bt_pausa.visible = visibile


## Un tocco sul bottone Pausa non deve diventare anche uno sparo.
func sopra_un_bottone(pos: Vector2) -> bool:
	return bt_pausa.visible and bt_pausa.get_global_rect().grow(4).has_point(pos)


func apri_versioni() -> void:
	if OS.has_feature("web"):
		# dalla versione attuale si va in versioni/; da una versione congelata (versioni/v1.0/) si torna su di uno
		JavaScriptBridge.eval("location.href=(/\\/versioni\\/v[^\\/]+\\/?$/.test(location.pathname)?'../':'versioni/')", true)
	else:
		OS.shell_open("https://nicolaregge-pulse.github.io/corso-informatica/giochi/treno-3inf-v2/versioni/")


# ---------------- Facce della classe ----------------
func mostra_facce() -> void:
	for n in w_anteprime.get_children():
		n.queue_free()
	for f in gioco.FACCE:
		var t := Tondo.new()
		t.tex = f.tex
		t.custom_minimum_size = Vector2(64, 64)
		w_anteprime.add_child(t)
	var n: int = gioco.FACCE.size()
	w_msg_foto.text = ("%d facce: compariranno sui cattivi." % n) if n > 0 else "Nessuna faccia: i cattivi sono quelli disegnati."


const JS_FOTO := """
window.trenoScegliFoto = function(cb){
  var vecchio = document.getElementById('trenoFileFoto'); if (vecchio) vecchio.remove();
  var inp = document.createElement('input'); inp.type = 'file'; inp.accept = 'image/*'; inp.multiple = true;
  inp.id = 'trenoFileFoto'; inp.style.display = 'none'; document.body.appendChild(inp);
  inp.onchange = function(){
    var files = Array.prototype.slice.call(inp.files).slice(0, 40), resto = files.length;
    window.trenoFotoMsg = '';
    if (!resto) { cb('fatto'); return; }
    var fine = function(){ if (--resto === 0) cb('fatto'); };
    files.forEach(function(f){
      var rd = new FileReader();
      rd.onload = function(){
        var im = new Image();
        im.onload = function(){
          var s = Math.min(im.width, im.height), x0 = (im.width - s) / 2, y0 = Math.max(0, Math.min(im.height - s, im.height * .38 - s / 2));
          var c = document.createElement('canvas'); c.width = c.height = 220;
          c.getContext('2d').drawImage(im, x0, y0, s, s, 0, 0, 220, 220);
          var lista = []; try { lista = JSON.parse(localStorage.getItem('treno-3inf-v2-foto') || '[]') } catch(e) {}
          lista.push(c.toDataURL('image/jpeg', .82));
          try { localStorage.setItem('treno-3inf-v2-foto', JSON.stringify(lista)) } catch(e) { window.trenoFotoMsg = 'Memoria piena: usa meno foto.' }
          fine();
        };
        im.onerror = fine;
        im.src = rd.result;
      };
      rd.onerror = fine;
      rd.readAsDataURL(f);
    });
  };
  inp.click();
};
"""


## Nel browser la finestra «scegli file» si può aprire solo DENTRO il clic (regola di sicurezza del browser).
## Per questo il clic sul bottone «Scegli le foto» lo ascolta direttamente la pagina (JavaScript):
## Godot le dice soltanto dove si trova il bottone sullo schermo (zona_foto).
const JS_ASCOLTA := """
window.__trenoZonaFoto = null;
window.__trenoUltimo = 0;
var trenoSuBottone = function(e){
  var z = window.__trenoZonaFoto, ora = Date.now();
  if (!z || ora - window.__trenoUltimo < 800) return;
  if (e.clientX >= z[0] && e.clientX <= z[0] + z[2] && e.clientY >= z[1] && e.clientY <= z[1] + z[3]) { window.__trenoUltimo = ora; window.trenoScegliFoto(window.__trenoCbFoto); }
};
// mouse: «mouseup»; dito o penna: «pointerup» (sono gli eventi in cui il browser permette di aprire la finestra dei file)
(document.getElementById('canvas') || document.querySelector('canvas')).addEventListener('mouseup', trenoSuBottone);
window.addEventListener('pointerup', function(e){ if (e.pointerType !== 'mouse') trenoSuBottone(e); }, true);
"""
var zona_foto := ""


func prepara_foto_web() -> void:
	JavaScriptBridge.eval(JS_FOTO + JS_ASCOLTA, true)
	cb_foto = JavaScriptBridge.create_callback(func(_args):
		gioco.carica_facce()
		mostra_facce()
		var m = JavaScriptBridge.eval("window.trenoFotoMsg||''", true)
		if m is String and m != "":
			w_msg_foto.text = m)
	JavaScriptBridge.get_interface("window").__trenoCbFoto = cb_foto


func _process(_delta: float) -> void:
	if not OS.has_feature("web"):
		return
	var z := "null"
	var b: Control = bottoni["scegli_foto"]
	if schermo_attivo == "facce" and b.is_visible_in_tree():
		var r := b.get_global_rect()
		z = "[%d,%d,%d,%d]" % [r.position.x, r.position.y, r.size.x, r.size.y]
	if z != zona_foto:
		zona_foto = z
		JavaScriptBridge.eval("window.__trenoZonaFoto=" + z, true)


func scegli_foto() -> void:
	if OS.has_feature("web"):
		return   # nel browser ci pensa la pagina (vedi JS_ASCOLTA)
	# sul PC: la finestra «Apri» di Godot
	if dialogo_foto == null:
		dialogo_foto = FileDialog.new()
		dialogo_foto.file_mode = FileDialog.FILE_MODE_OPEN_FILES
		dialogo_foto.access = FileDialog.ACCESS_FILESYSTEM
		dialogo_foto.use_native_dialog = true
		dialogo_foto.filters = PackedStringArray(["*.jpg, *.jpeg, *.png, *.webp ; Immagini"])
		dialogo_foto.files_selected.connect(func(files):
			var lista: Array = mem.foto()
			for f in files.slice(0, 40):
				var u: String = mem.dataurl_da_file(f)
				if u != "":
					lista.append(u)
			if not mem.scrivi("foto", lista):
				w_msg_foto.text = "Memoria piena: usa meno foto."
			gioco.carica_facce()
			mostra_facce())
		add_child(dialogo_foto)
	dialogo_foto.popup_centered(Vector2i(800, 500))


## La foto ritagliata a cerchio, con il bordo giallo (anteprima nelle Facce della classe).
class Tondo extends Control:
	var tex: Texture2D

	func _draw() -> void:
		var c := size / 2.0
		var r: float = min(size.x, size.y) / 2.0 - 2.0
		var punti := PackedVector2Array()
		var uv := PackedVector2Array()
		for i in 33:
			var a := i / 32.0 * TAU
			var q := c + Vector2(cos(a), sin(a)) * r
			punti.append(q)
			uv.append((q - (c - Vector2(r, r))) / (2.0 * r))
		draw_colored_polygon(punti, Color.WHITE, uv, tex)
		draw_arc(c, r, 0, TAU, 40, Color("#ffd34d"), 3.0, true)


# ---------------- misure che cambiano con lo schermo (telefono, PC...) ----------------
func aggiorna_misure() -> void:
	var s := get_viewport().get_visible_rect().size
	for m in misure:
		if is_instance_valid(m[0]):
			m[0].custom_minimum_size.x = min(float(m[1]), s.x - 32.0)
	for c in caratteri:
		var v: int = int(clamp(s.x * c[2], c[1], c[3]))
		if c[0] is LabelSettings:
			c[0].font_size = v
		elif c[0] is Control:
			c[0].add_theme_font_size_override("font_size", v)
	for k in schermi:
		var m: MarginContainer = schermi[k].get_meta("contenuto")
		m.custom_minimum_size = Vector2(0, s.y)


func rettangoli_bottoni() -> Dictionary:
	var d := {}
	for k in bottoni:
		var b: Control = bottoni[k]
		if b.is_visible_in_tree():
			var r := b.get_global_rect()
			d[k] = [r.position.x, r.position.y, r.size.x, r.size.y]
	return d
