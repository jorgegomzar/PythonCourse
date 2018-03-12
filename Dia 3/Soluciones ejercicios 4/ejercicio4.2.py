lista = []
valores_validos = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
finalizar = False
print('Valores válidos:', valores_validos)
while not finalizar:
	num = input('Introduce un número entero: ')
	if num == '':
		finalizar = True
	elif int(num) in valores_validos:
		lista.append(int(num))
for k in lista:
	print(k)