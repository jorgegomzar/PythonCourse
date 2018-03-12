lista = []
finalizar = False
veces = 0

while not finalizar:
	nombre = input('Introduce un nombre: ')
	if nombre == '':
		finalizar = True
	else:
		lista.append(nombre)
for k in lista:
	veces = veces + k.count('a') + k.count('A')
print('En total se han encontrado',veces, 'veces la letra a.')