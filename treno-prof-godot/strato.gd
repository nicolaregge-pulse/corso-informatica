extends Node2D
## Uno «strato» del disegno: un foglio trasparente su cui il motore dipinge.
## Il motore dice quale funzione usare come pennello (disegna); qui _draw() la chiama.
## Gli strati sono uno sopra l'altro: paesaggio, cabina, scritte in alto.

var disegna: Callable


func _draw() -> void:
	if disegna.is_valid():
		disegna.call(self)
