positivos = 0
negativos = 0
while True:
   entrada = input('Introduce un valor. Introduce f para finalizar: ')
   if entrada == 'f':
         break
   else:
      numero = int(entrada)
      if numero > 0:
         positivos = positivos + 1
      elif numero < 0:
         negativos = negativos + 1
print('Has introducido', positivos, 'números enteros positivos y', negativos, 'números enteros negativos.')