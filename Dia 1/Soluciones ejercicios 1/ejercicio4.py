import math

num1 = int(input('Escribe el dígito más a la izquierda: '))
num2 = int(input('Escribe el siguiente digito: '))
num3 = int(input('Escribe el siguiente digito: '))
num4 = int(input('Escribe el siguiente digito: '))
total = num1+num2*2+num3*4+num4*8
print('El valor binario '+str(num1)+str(num2)+str(num3)+str(num4)+' es '+str(int(total))+' en base 10.')