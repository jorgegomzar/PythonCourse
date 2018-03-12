from colorama import *
init(autoreset=True)

print('Conteste a las siguientes preguntas para descubrir si cumple los requisitos para obtener el crédito:')
print('\n')
precVivienda = int(input('Precio de la vivienda: '))
if precVivienda > 800000:
	print(Fore.RED+'Lo sentimos, el precio de la vivienda está limitado a 800000 €.')
	exit()
ingresos = int(input('Ingresos del solicitante: '))
if ingresos > 225000:
	print(Fore.RED+'Lo sentimos, el ingreso del solicitante no debe superar los 225000 €.')
	exit()
propietario = input('¿Ha sido propietario de alguna vivienda anteriormente? (s/n) ').lower()
if propietario == 'n':
	print(Fore.GREEN+'¡ENHORABUENA!')
	print('En base a la información proporcionada, ha conseguido Vd. el crédito solicitado.')
	exit()
anyos = int(input('¿Hace cuantos años que fue propietario de una vivienda?: '))
if anyos <= 3:
	print(Fore.RED+'Lo sentimos, no puede percibir el crédito si ha sido propietario en los últimos 3 años.')
	exit()
else:
	print(Fore.GREEN+'¡ENHORABUENA!')
	print('En base a la información proporcionada, ha conseguido Vd. el crédito solicitado.')
	exit()