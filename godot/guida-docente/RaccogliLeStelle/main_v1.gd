extends Node2D

var punti = 0
const STELLE_PER_VINCERE = 5

func _ready():
	for stella in get_tree().get_nodes_in_group("stelle"):
		stella.raccolta.connect(_on_stella_raccolta)
	aggiorna_testo()

func _on_stella_raccolta():
	punti += 1
	aggiorna_testo()
	if punti == STELLE_PER_VINCERE:
		$Punteggio.text = "HAI VINTO! Premi Invio per ricominciare"

func aggiorna_testo():
	$Punteggio.text = "Stelle: " + str(punti)

func _input(event):
	if event.is_action_pressed("ui_accept"):
		get_tree().reload_current_scene()
