extends Node

const FILE_RECORD = "user://record.json"

func carica_record():
	if not FileAccess.file_exists(FILE_RECORD):
		return 0
	var f = FileAccess.open(FILE_RECORD, FileAccess.READ)
	var dati = JSON.parse_string(f.get_as_text())
	if dati == null:
		return 0
	return int(dati["record"])

func salva_record(valore):
	var f = FileAccess.open(FILE_RECORD, FileAccess.WRITE)
	f.store_string(JSON.stringify({"record": valore}))
