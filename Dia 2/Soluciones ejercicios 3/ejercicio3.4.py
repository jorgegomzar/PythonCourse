total = 0
while True:
	num = int(input('Introduce un número entre 0 y 100. Introduce uno negativo para finalizar: '))
	if num >= 0:
		if num < 100:
			total = total + num
	else:
		break
print('La suma de todos los números es: ', total)