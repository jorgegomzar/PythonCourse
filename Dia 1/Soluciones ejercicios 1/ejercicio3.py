import math
base = int(input('¿Qué base? ' ))
potencia = int(input('¿Qué potencia de '+str(base)+'? '))
print(str(base)+' elevado a la potencia '+str(potencia)+' es '+str(int(math.pow(base,potencia))))
