extends Node2D

var punti = 0

func _on_stella_raccolta():
	punti += 1
	$Suono.play()
	$Punteggio.text = "Stelle: " + str(punti)
