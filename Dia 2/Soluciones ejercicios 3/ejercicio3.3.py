crObtenidos = int(input('¿Cuántos créditos has obtenido? '))
if crObtenidos >= 90:
	print('Senior')
elif crObtenidos >= 60:
	print('Junior')
elif crObtenidos >= 30:
	print('Segundo curso')
else:
	print('Primer curso')