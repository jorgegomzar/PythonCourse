def convertStatus(status):
	"""Se le pasa el código de estado 'f', 's', 'j' o 'r' y devuelve la cadena 'freshman', 'sophomore', 'junior' o 'senior', respectivamente."""
	if status.lower() == 'f':
		return 'freshman'
	elif status.lower() == 's':
		return 'sophomore'
	elif status.lower() == 'j':
		return 'junior'
	elif status.lower() == 'r':
		return 'senior'
	else:
		return 'Por favor, ingresa una letra apropiada.'