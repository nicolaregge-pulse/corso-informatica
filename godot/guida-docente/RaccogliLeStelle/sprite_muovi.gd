extends Sprite2D

func _process(delta):
	var direzione = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	position += direzione * 300 * delta
