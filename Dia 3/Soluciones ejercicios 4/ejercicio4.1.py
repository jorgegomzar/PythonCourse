lista = []
final = False
while not final:
	num = input('Escribe un número entero: ')
	if num == '':
		final = True
	elif int(num) >= 0 and int(num) <= 100:
		lista.append(int(num))
	elif int(num) < 0 or int(num) > 100:
		print('El número entero debe ser entre 0 y 100.')

for k in lista:
	print(k)