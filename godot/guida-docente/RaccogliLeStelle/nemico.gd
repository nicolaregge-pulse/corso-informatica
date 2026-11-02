extends Area2D

signal toccato

var velocita = 150.0
var direzione = 1

func _process(delta):
	position.x += velocita * direzione * delta
	if position.x > 1000 or position.x < 100:
		direzione = -direzione

func _on_body_entered(body):
	if body.name == "Player":
		toccato.emit()
