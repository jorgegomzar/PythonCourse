def buscaCero(n1, n2, n3):
	if n1 == 0 or n2 == 0 or n3 == 0:
		return True
	else:
		return False

n1 = int(input('Introduce el primer número: '))
n2 = int(input('Introduce el segundo número: '))
n3 = int(input('Introduce el tercer número: '))
print(buscaCero(n1, n2, n3))