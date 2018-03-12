import math

partidasPorAño=7500000000*365
partidasPosibles=math.pow(10,120)
total=partidasPosibles/partidasPorAño
print('El número de años necesarios para jugar todas las partidas de ajedrez posibles si cada humano juega una sola partida al día, es de '+str(total))