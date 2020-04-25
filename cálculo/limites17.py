'''
    Limites - Determining Limits Analytically
    Direct Substitution - 01
    g(x)= (x**2 - 1) / (x - 1), x≠1
 '''

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    if x != 1:
        return (x**2 - 1) / (x - 1)


# Cria os arrays de valores de x
x = range(-20,21)

# Gera os valores de y correspondentes
y = [f(i) for i in x]

# Configura o Gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

# Plota a função
plt.plot(x, y, color='purple')

# Plot f(x) when x = 4
zx = 4
zy = f(zx)
plt.plot(zx, zy, color='red', marker='o', markersize=10)
plt.annotate(str(zy),(zx, zy), xytext=(zx - 2, zy + 1))

plt.show()

print ('Limite de x -> ' + str(zx) + ' = ' + str(zy))

