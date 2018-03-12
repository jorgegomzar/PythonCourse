lista1 = []
lista2 = []
comunes = []
suma1 = 0
suma2 = 0
finalizar = False

while not finalizar:
	num = input('Introduce un número entero para la primera lista: ')
	if num == '':
		finalizar = True
	else:
		lista1.append(int(num))
	num = input('Introduce un número entero para la segunda lista: ')
	if num == '':
		finalizar = True
	else:
		lista2.append(int(num))
if len(lista1) < len(lista2):
	print('La segunda lista tiene más elementos que la primera lista.')
elif len(lista1) > len(lista2):
	print('La primera lista tiene más elementos que la segunda lista.')
else:
	print('Las dos listas tienen la misma longitud.')
for k in lista1:
	suma1 = suma1 + k
for k in lista2:
	suma2 = suma2 + k
if suma1 < suma2:
	print('Los números de la segunda lista suman un mayor número.')
elif suma1 > suma2:
	print('Los números de la primera lista suman un menor número.')
else:
	print('La suma de todos los números de ambas listas es igual.')
for k in lista1:
	for j in lista2:
		if k == j:
			comunes.append(k)
if len(comunes) == 0:
	print('Las dos listas no tienen ningún número en común.')
else:
	print('Las dos listas tienen', len(comunes), 'números en común: ', comunes)