'''
    Limits at Non-Continuous Points 03
'''

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    if x != 0:
        return (-2*x**2) * 1/x

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

# Plota f(x) quando x = -0.00001
# negx = 0.1
negx = 0.00001
negy = f(negx)
plt.plot(negx, negy, color='blue', marker='<', markersize=10)
plt.annotate(str(negy),(negx, negy), xytext=(negx + 1, negy))


# Plota f(x) quando x = -0.00001
# negx = -0.1
negx = -0.00001
negy = f(negx)
plt.plot(negx, negy, color='orange', marker='>', markersize=10)
plt.annotate(str(negy),(negx, negy), xytext=(negx + 1, negy))


plt.show()

