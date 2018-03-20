def compruebaPalindromo(cadena):
	"""Utiliza iteración para devolver True si una cadena proporcionada es un palíndromo, y False en caso contrario."""
	invertida = ''
	nuevaCadena = ''
	pal = True
	for char in cadena:
		if char != ' ' and char != ',' and char != '.':
			invertida = char.lower() + invertida
			nuevaCadena = nuevaCadena + char.lower()
	for i in range(len(nuevaCadena)):
		if invertida[i] != nuevaCadena[i]:
			pal = False

	return pal