extends Node
## I SUONI del treno (squadra SUONI).
## Nessun file audio: ogni suono si «costruisce» con la matematica, come nella versione HTML
## (là lo faceva il WebAudio del browser). Qui si calcolano i campioni una volta sola, all'avvio,
## e poi si suonano con alcuni AudioStreamPlayer (più suoni insieme = più «altoparlanti»).
##
## rumore(...)  = un fruscio filtrato (spari, vetro che si crepa)
## tono(...)    = una nota (fischio, vittoria, «pop» del cattivo colpito)

const FREQ := 22050          # campioni al secondo
var volume := 0.6            # da suoni.json
var note_vittoria := [392, 523, 659, 784]   # da suoni.json
var suoni := {}              # nome -> Array di AudioStreamWAV (più varianti per i suoni casuali)
var casse := []              # gli «altoparlanti»
var prossima := 0


func prepara(vol: float, note: Array) -> void:
	volume = vol
	note_vittoria = note
	for i in 10:
		var p := AudioStreamPlayer.new()
		add_child(p)
		casse.append(p)
	suoni["colpo"] = [costruisci(func(b): rumore(b, .12, .5, 3000, 400, "bandpass"); tono(b, 220, .08, .15, "square", 0, 90))]
	suoni["pop"] = [costruisci(func(b): tono(b, 520, .09, .18, "triangle", 0, 1400); tono(b, 900, .12, .1, "sine", .04, 300))]
	suoni["sparo"] = [costruisci(func(b): rumore(b, .25, .9, 1800, 120, "lowpass"); tono(b, 140, .2, .25, "sawtooth", 0, 50))]
	suoni["crepa"] = []
	for v in 3:
		suoni["crepa"].append(costruisci(func(b):
			rumore(b, .35, .6, 6000, 2500, "highpass")
			for i in 6:
				tono(b, randf_range(2500, 5000), .12, .05, "sine", i * .035)))
	suoni["rotto"] = []
	for v in 2:
		suoni["rotto"].append(costruisci(func(b):
			rumore(b, 1.2, .9, 7000, 800, "highpass")
			for i in 16:
				tono(b, randf_range(1800, 6000), .18, .06, "triangle", i * .05)))
	suoni["fischio"] = [costruisci(func(b): tono(b, 660, .5, .12, "sine", 0, 640); tono(b, 830, .5, .08, "sine", 0, 800))]
	suoni["sferraglia"] = [costruisci(func(b): rumore(b, .08, .12, 500, 200, "lowpass"))]
	suoni["vittoria"] = [costruisci(func(b):
		for i in note_vittoria.size():
			tono(b, float(note_vittoria[i]), .18, .12, "square", i * .09))]


func suona(nome: String) -> void:
	if not suoni.has(nome) or volume <= 0.0:
		return
	var p: AudioStreamPlayer = casse[prossima]
	prossima = (prossima + 1) % casse.size()
	p.stream = suoni[nome].pick_random()
	p.play()


# ---------------- la fabbrica dei suoni ----------------
## Prepara un «nastro» vuoto, ci lascia scrivere i suoni (ricetta) e lo trasforma in un AudioStreamWAV.
func costruisci(ricetta: Callable) -> AudioStreamWAV:
	var b := {"dati": PackedFloat32Array()}
	ricetta.call(b)
	var campioni: PackedFloat32Array = b["dati"]
	var byte := PackedByteArray()
	byte.resize(campioni.size() * 2)
	for i in campioni.size():
		byte.encode_s16(i * 2, int(clamp(campioni[i], -1.0, 1.0) * 32000.0))
	var w := AudioStreamWAV.new()
	w.format = AudioStreamWAV.FORMAT_16_BITS
	w.mix_rate = FREQ
	w.stereo = false
	w.data = byte
	return w


func allunga(b: Dictionary, n: int) -> void:
	var d: PackedFloat32Array = b["dati"]
	if d.size() < n:
		var vecchio := d.size()
		d.resize(n)
		for i in range(vecchio, n):
			d[i] = 0.0
		b["dati"] = d


## Una nota: frequenza f (che scivola fino a f2), durata dur, volume vol, forma dell'onda tipo.
func tono(b: Dictionary, f: float, dur: float, vol: float, tipo := "square", quando := 0.0, f2 := 0.0) -> void:
	vol *= volume
	if vol <= 0.0:
		return
	var inizio := int(quando * FREQ)
	var n := int(dur * FREQ)
	allunga(b, inizio + n)
	var d: PackedFloat32Array = b["dati"]
	var fase := 0.0
	for i in n:
		var k := float(i) / n
		var fr := f * pow(f2 / f, k) if f2 > 0.0 else f
		fase = fmod(fase + fr / FREQ, 1.0)
		var onda := 0.0
		match tipo:
			"sine": onda = sin(fase * TAU)
			"square": onda = 1.0 if fase < 0.5 else -1.0
			"triangle": onda = 4.0 * abs(fase - 0.5) - 1.0
			_: onda = 2.0 * fase - 1.0   # sawtooth (dente di sega)
		var g := vol * pow(0.001 / vol, k)   # il volume scende piano piano
		d[inizio + i] += onda * g * 0.5
	b["dati"] = d


## Un fruscio (rumore bianco) che si spegne, passato in un filtro che sposta la sua frequenza da f1 a f2.
func rumore(b: Dictionary, dur: float, vol: float, f1: float, f2: float, tipo := "bandpass") -> void:
	vol *= volume
	var n := int(dur * FREQ)
	allunga(b, n)
	var d: PackedFloat32Array = b["dati"]
	var x1 := 0.0
	var x2 := 0.0
	var y1 := 0.0
	var y2 := 0.0
	var c := [0.0, 0.0, 0.0, 0.0, 0.0]
	for i in n:
		if i % 32 == 0:
			c = coefficienti(tipo, f1 * pow(f2 / f1, float(i) / n))
		var x := (randf() * 2.0 - 1.0) * pow(1.0 - float(i) / n, 2.0)
		var y: float = c[0] * x + c[1] * x1 + c[2] * x2 - c[3] * y1 - c[4] * y2
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
		d[i] += y * vol * 0.6
	b["dati"] = d


## Il filtro (biquad, come quello del browser): lascia passare solo una parte delle frequenze.
func coefficienti(tipo: String, f: float) -> Array:
	f = clamp(f, 20.0, FREQ * 0.45)
	var w0 := TAU * f / FREQ
	var al := sin(w0) / 2.0   # Q = 1
	var cw := cos(w0)
	var b0 := 0.0
	var b1 := 0.0
	var b2 := 0.0
	match tipo:
		"lowpass":
			b0 = (1.0 - cw) / 2.0; b1 = 1.0 - cw; b2 = (1.0 - cw) / 2.0
		"highpass":
			b0 = (1.0 + cw) / 2.0; b1 = -(1.0 + cw); b2 = (1.0 + cw) / 2.0
		_:
			b0 = al; b1 = 0.0; b2 = -al
	var a0 := 1.0 + al
	return [b0 / a0, b1 / a0, b2 / a0, (-2.0 * cw) / a0, (1.0 - al) / a0]
