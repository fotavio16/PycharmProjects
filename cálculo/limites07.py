'''
    Limites
'''

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    if x <= 0:
        return x + 20
    else:
        return x - 100


# Cria o array de valores de x para cada intervalo da função
x1 = range(-20,1)
x2 = range(1, 20)

# Gera os valores de y correspondentes
y1 = [f(i) for i in x1]
y2 = [f(i) for i in x2]

# Configura o Gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

# Plota a função
plt.plot(x1, y1, color='green')
plt.plot(x2, y2, color='green')

# Traça um círculo perto o suficiente para o limite g(-x)
plt.plot(0, f(0), color='green', marker='o', markerfacecolor='green', markersize=10)
plt.plot(0, f(0.0001), color='green', marker='o', markerfacecolor='w', markersize=10)

plt.show()

