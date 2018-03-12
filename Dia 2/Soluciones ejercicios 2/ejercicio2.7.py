palabras = 5000000000000000000
velocidad = float(input('¿Velocidad de descarga (en Mbps)?: ')) * 1000000
tiempo = (palabras * 8 ) / velocidad
anyos = tiempo/(3600 * 24 * 365)
print('Años: ', format( anyos, '.6e'), format( anyos, ',f'))