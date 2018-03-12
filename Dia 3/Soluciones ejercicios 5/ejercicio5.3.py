def modCount(n, m):
	for k in range(n+1):
		if k % m == 0:
			print(k, 'es divisible por', m)

n = int(input('Introduce el primer número: '))
m = int(input('Introduce el segundo número: '))
modCount(n, m)