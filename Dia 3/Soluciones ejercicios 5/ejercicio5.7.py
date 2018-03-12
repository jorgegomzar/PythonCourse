def umbral(lista, valor):
	for numero in lista:
		if numero < valor:
			lista[lista.index(numero)] = 0

lista = []
finalizar = False
while not finalizar:
	numero = input('Introduce un número entero: ')
	if numero == '':
		finalizar = True
	else:
		lista.append(int(numero))
valor = int(input('Introduce un valor umbral: '))
print(lista)
umbral(lista, valor)
print(lista)