extends CharacterBody2D

const VELOCITA = 300.0

func _physics_process(_delta):
	var direzione = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	velocity = direzione * VELOCITA
	move_and_slide()
