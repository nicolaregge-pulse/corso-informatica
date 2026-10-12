extends RefCounted
## LA MEMORIA del gioco: record, migliori punteggi, soprannome, facce della classe.
## Tutto resta SOLO su questo dispositivo: niente va in rete.
##
## Nel browser usa la memoria del browser (localStorage) con i nomi «treno-prof-...»:
## record e facce della base sono separati da quelli del treno HTML della 2INF.
## Fuori dal browser (Godot sul PC) usa un file nella cartella dell'utente (user://).

const PREFISSO := "treno-prof-"
const FILE := "user://memoria.cfg"
var web := OS.has_feature("web")


func leggi(k: String, predefinito):
	var testo = leggi_testo(PREFISSO + k)
	if testo == null:
		return predefinito
	var v = JSON.parse_string(testo)
	return predefinito if v == null else v


func scrivi(k: String, v) -> bool:
	return scrivi_testo(PREFISSO + k, JSON.stringify(v))


## Legge un testo grezzo (null se non c'è).
func leggi_testo(chiave: String):
	if web:
		var t = JavaScriptBridge.eval("(function(){try{return localStorage.getItem(%s)}catch(e){return null}})()" % JSON.stringify(chiave), true)
		return t if t is String else null
	var c := ConfigFile.new()
	if c.load(FILE) != OK or not c.has_section_key("memoria", chiave):
		return null
	return String(c.get_value("memoria", chiave))


func scrivi_testo(chiave: String, testo: String) -> bool:
	if web:
		return bool(JavaScriptBridge.eval("(function(){try{localStorage.setItem(%s,%s);return true}catch(e){return false}})()" % [JSON.stringify(chiave), JSON.stringify(testo)], true))
	var c := ConfigFile.new()
	c.load(FILE)
	c.set_value("memoria", chiave, testo)
	return c.save(FILE) == OK


# ---------------- le facce della classe (foto ritagliate a cerchio) ----------------
## Le foto sono salvate come «data URL» (testo che contiene l'immagine JPEG), come nella versione HTML.
func foto() -> Array:
	var v = leggi("foto", [])
	return v if v is Array else []


## Trasforma una data URL in una texture che Godot sa disegnare.
func texture_da_dataurl(u: String) -> Texture2D:
	var virgola := u.find(",")
	if virgola < 0:
		return null
	var byte := Marshalls.base64_to_raw(u.substr(virgola + 1))
	var im := Image.new()
	var ok := im.load_jpg_from_buffer(byte) if u.begins_with("data:image/jpeg") else im.load_png_from_buffer(byte)
	if ok != OK:
		return null
	return ImageTexture.create_from_image(im)


## Ritaglia una foto quadrata attorno al viso (220 x 220) e la trasforma in data URL. Serve sul PC (fuori dal browser).
func dataurl_da_file(percorso: String) -> String:
	var im := Image.load_from_file(percorso)
	if im == null or im.is_empty():
		return ""
	var s: int = min(im.get_width(), im.get_height())
	var x0 := int((im.get_width() - s) / 2.0)
	var y0 := int(clamp(im.get_height() * 0.38 - s / 2.0, 0, im.get_height() - s))
	var q := im.get_region(Rect2i(x0, y0, s, s))
	q.resize(220, 220, Image.INTERPOLATE_BILINEAR)
	return "data:image/jpeg;base64," + Marshalls.raw_to_base64(q.save_jpg_to_buffer(0.82))
