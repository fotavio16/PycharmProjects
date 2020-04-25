'''
    Limites
'''

def f(x):
    return x**2 + x
    #return x ** 2 - 3 * x

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

# Cria o array de valores de x de 0 a 10
x = list(range(0, 11))

# Gera os valores de y correspondentes
y = [f(i) for i in x]

# Configura o Gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

# Plota a função
plt.plot(x, y, color='lightgrey', marker='o', markeredgecolor='green', markerfacecolor='green')

plt.show()

