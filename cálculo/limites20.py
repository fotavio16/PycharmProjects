'''
    Limites - Rules for Limit Operations - 01

    j(x)=2x−2
    l(x)=−2x+4
 '''

# Plota a Função
import math
from matplotlib import pyplot as plt

def f(x):
    return x * 2 - 2

def g(x):
    return -x * 2 + 4

# Cria os arrays de valores de x
x = range(-10,11)

# Gera os valores de y correspondentes
fy = [f(i) for i in x]
gy = [g(i) for i in x]

# Configura o Gráfico
plt.xlabel('x')
plt.xticks(range(-10, 11, 1))
plt.ylabel('y')
plt.yticks(range(-30, 30, 2))
plt.grid()

# Plota as funções
plt.plot(x, fy, color='green', label='f(x)')
plt.plot(x, gy, color='magenta', label='g(x)')

plt.legend()

plt.show()

