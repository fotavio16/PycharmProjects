'''
    Limites - One-Sided Limits
    lim x->2 (x-2)/(x**2 -4) = 1/4
    lim x->0 (sqrt(x**2 + 9) -3)/ x**2
    = 1/6
 '''

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    if x <= 0:
        return x + 20
    else:
        return x - 100

# Cria os arrays de valores de x de -20 a 20
x1 = range(-20,6)
x2 = range(6,21)

# Gera os valores de y correspondentes
y1 = [f(i) for i in x1]
y2 = [f(i) for i in x2]

# Configura o Gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

# Plota a função
plt.plot(x1, y1, color='purple')
plt.plot(x2, y2, color='purple')

# Plota um círculo perto suficiente dos limites de f
plt.plot(5, f(5), color='purple',
         marker='o', markerfacecolor='purple', markersize=10)
plt.plot(5, f(5.001), color='purple',
         marker='o', markerfacecolor='w', markersize=10)

# Plota alguns pontos da direção direita
posx = [20, 15, 10, 6]
posy = [f(i) for i in posx]
plt.scatter(posx, posy, color='blue', marker='<', s=70)
for p in posx:
    plt.annotate(str(f(p)),(p, f(p)),xytext=(p, f(p) + 5))

# Plota alguns pontos da direção esquerda
negx = [-15, -10, -5, 0, 4]
negy = [f(i) for i in negx]
plt.scatter(posx, posy, color='orange', marker='>', s=70)
for n in negx:
    plt.annotate(str(f(n)),(n, f(n)),xytext=(n, f(n) + 5))


plt.show()

