lista = []
finalizar = False
valido = -1
veces = 0

while not finalizar:
	valido = -1
	nombre = input('Introduce un nombre: ')
	if nombre == '':
		finalizar = True
	else:
		for letra in nombre.upper():
			if nombre[0] == letra:
				valido = valido + 1
		if valido >= 1:
			lista.append(nombre)
print(lista)
for k in lista:
	veces = veces + k.count('a') + k.count('A')
print('En total se han encontrado',veces, 'veces la letra a.')