def ordenados(n1, n2, n3):
	if n1 < n2:
		if n2 < n3:
			return True
		else:
			return False
	else:
		return False

n1 = int(input('Introduce el primer número: '))
n2 = int(input('Introduce el segundo número: '))
n3 = int(input('Introduce el tecer número: '))
print(ordenados(n1, n2, n3))