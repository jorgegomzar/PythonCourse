lista = []
finalizar = False

while not finalizar:
	num = input('Introduce un número entero: ')
	if num == '':
		finalizar = True
	elif int(num) <= 100:
		lista.append(int(num))
	elif int(num) > 100:
		lista.append('pasa')
for k in lista:
	print(k)