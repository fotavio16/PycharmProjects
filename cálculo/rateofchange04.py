'''
    Rate of Change - Quadratic
'''

def r(x):
    #return x**2 + x
    return x**2 - 3*x

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

# Cria um array de x com valores de 0 a 10
x = np.array(range(0, 11))

# Cria um array para a linha secante
s = np.array([2,8])

# Calcula a Taxa de Mudança
x1 = s[0]
x2 = s[1]
y1 = r(x1)
y2 = r(x2)
T = (y2 - y1) / (x2 - x1)

# Configura o Gráfico
plt.xlabel('Segundos')
plt.ylabel('Metros')
plt.grid()

# Plota x por r(x)
plt.plot(x, r(x), color='green')

# Plota a linha secante
plt.plot(s, r(s), color='magenta')

plt.annotate('Velocidade Média = ' + str(T) + ' m/s',((x2+x1)/2, (y2+y1)/2))
plt.show()



