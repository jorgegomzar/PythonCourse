def umbral(lista, valor):
	nueva_lista = []
	for numero in lista:
		if numero < valor:
			nueva_lista.append(0)
		else:
			nueva_lista.append(numero)
	return nueva_lista
lista = []
nueva_lista = []
finalizar = False
while not finalizar:
	numero = input('Introduce un número entero: ')
	if numero == '':
		finalizar = True
	else:
		lista.append(int(numero))
valor = int(input('Introduce un valor umbral: '))
print(lista)
nueva_lista = umbral(lista, valor)
print(nueva_lista)