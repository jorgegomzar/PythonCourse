def bienvenida():
	print('Este programa convierte temperaturas (Fahrenheit/Celsius)')
	print('Teclea (F) para convertir de Fahrenheit a Celsius')
	print('Teclea (C) para convertir de Celsius a Fahrenheit')

while True:
	bienvenida()
	char = input('Tipo de conversion? ')
	t1 = int(input('Introduce la temperatura inicial a convertir: '))
	t2 = int(input('Introduce la temperatura final a convertir: '))
	if char == 'C' or char == 'c':
		print('Celsius     Fahrenheit')
		for temp in range(t1, t2 + 1):
			print(format(temp, '.1f'), '      ', format(1.8 * temp + 32, '.1f'))

	elif char == 'F' or char == 'f':
		print('Fahrenheit     Celsius')
		for temp in range(t1, t2 + 1):
			print(format(temp, '.1f'), '         ', format((temp - 32) / 1.8, '.1f'))