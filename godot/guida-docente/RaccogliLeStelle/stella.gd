extends Area2D

signal raccolta

func _on_body_entered(body):
	if body.name == "Player":
		raccolta.emit()
		queue_free()
