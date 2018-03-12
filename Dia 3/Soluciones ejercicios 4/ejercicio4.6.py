lista = []
finalizar = False

while not finalizar:
	sublista = []
	fruta = input('Introduce el tipo de fruta: ')
	if fruta == '':
		finalizar = True
	else:
		peso = float(input('Introduce su peso: '))
		sublista.append(fruta)
		sublista.append(peso)
		lista.append(sublista)
print(format('Tipo', ' <10'), 'Peso')
for k in lista:
	print(format(k[0], ' <10'), k[1])