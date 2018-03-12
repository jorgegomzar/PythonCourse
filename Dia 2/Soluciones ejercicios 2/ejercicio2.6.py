fila = 0
total = 0
num = 0
nFilas = (7, 15, 23, 31, 39, 47, 55, 63)
for x in range(0,64):
	total = total + (2 ** x)
	fila = fila + (2 ** x)
	if x in nFilas:
		num = num + 1
		print('Granos en fila ',str(num)+': ', format(format(fila, ',d'),'>30'))
		fila = 0
print(format('Granos totales:', '>18'), format(format(total, ',d'),'>30'))
print('Peso total del trigo:', format(total*0.00004,'.2f'), 'kilogramos')
print('Peso total del trigo:', format(total*0.00004,'.6e'), 'kilogramos')