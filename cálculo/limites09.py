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

# Plota f(x) quando x = 0.1
posx = 0.1
posy = f(posx)
plt.plot(posx, posy, color='blue', marker='<', markersize=10)
plt.annotate(str(posy),(posx, posy), xytext=(posx +1, posy))

# Plota f(x) quando x = -0.1
negx = -0.1
negy = f(negx)
plt.plot(negx, negy, color='orange', marker='>', markersize=10)
plt.annotate(str(negy),(negx, negy), xytext=(negx -2, negy))

plt.show()

