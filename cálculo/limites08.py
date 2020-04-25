'''
    Limites
'''

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return x**2 + 1

# Cria o array de valores de x de 0 a 10
x = range(-10,11)

# Gera os valores de y correspondentes
y = [f(i) for i in x]

# Configura o Gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

# Plota a função
plt.plot(x, y, color='purple')

# Plota f(x) quando x = 0
zx = 0
zy = f(zx)
plt.plot(zx, zy, color='red', marker='o', markersize=10)
plt.annotate(str(zy),(zx, zy), xytext=(zx, zy + 5))

plt.show()

