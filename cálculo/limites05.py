'''
    Limites
'''

def g(x):
    if x != 0:
        return -(12/(2*x))**2
        #return x ** 2 - 3 * x

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

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

# Plota um círculo no vazio da função ou perto suficiente
xy = (0, g(1))
plt.annotate('O', xy, xytext=(-0.7, -37), fontsize=14, color='green')

plt.show()

