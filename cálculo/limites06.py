'''
    Limites
'''

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

def g(x):
    if x >= 0:
        return 2*np.sqrt(x)
        #return x ** 2 - 3 * x

# Cria o array de valores de x de 0 a 10
x = range(-20,21)

# Gera os valores de y correspondentes
y = [g(i) for i in x]

# Configura o Gráfico
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()

# Plota a função
plt.plot(x, y, color='green')

# Traça um círculo perto o suficiente para o limite g(-x)
plt.plot(0, g(0), color='green', marker='o', markerfacecolor='green', markersize=10)

plt.show()

