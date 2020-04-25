'''
    Rate of Change - Quadratic
'''

def r(x):
    #return x**2 + x
    return x ** 2 - 3 * x

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

# Cria um array de x com valores de 0 a 10
x = np.array(range(0, 11))

# Cria um array para a linha secante
s = np.array([0,10])

# Configura o Gráfico
plt.xlabel('Segundos')
plt.ylabel('Metros')
plt.grid()

# Plota x por r(x)
plt.plot(x, r(x), color='green')

# Plota a linha secante
plt.plot(s, r(s), color='magenta')

plt.show()



