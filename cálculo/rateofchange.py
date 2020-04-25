'''
    Linear Rate of Change
'''

def q(x):
    return 3*x + 2

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

# Cria um array de x com valores de 0 a 10
x = np.array(range(0, 11))

# Configura o Gráfico
plt.xlabel('Segundos')
plt.ylabel('Metros')
plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 35, 1))
plt.grid()

# Plota x por q(x)
plt.plot(x, q(x), color='green')
plt.show()



