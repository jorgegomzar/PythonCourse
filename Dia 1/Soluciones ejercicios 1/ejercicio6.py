import math

ciudades=int(input('Escribe el número de ciudades: '))
rutas=int(math.factorial(ciudades))
print('Número de rutas: '+str(rutas))
rutasPorAño=int(1000000*24*365*3600)
print('Número de rutas por año: '+str(rutasPorAño))
print('El tiempo necesario para resolver el problema del viajante para '+str(ciudades)+' ciudades es aproximadamente de '+str(float(rutas/rutasPorAño))+' años.')