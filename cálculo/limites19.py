'''
    Limites - Determining Limits Analytically
    Rationalization - 01
    h(x)=x⎯⎯√−2x−4, x≠4 and x≥0
 '''

# Plota a Função
import math
from matplotlib import pyplot as plt

def f(x):
    if x >= 0 and x != 4:
        return (math.sqrt(x) - 2) / (x - 4)


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

# Especifica o valor de x desejado
zx = 4
zy = 1 / ((math.sqrt(zx)) + 2)

# Plota o limite de f(x) quando x -> zx
plt.plot(zx, zy, color='red', marker='o', markersize=10)
plt.annotate(str(zy),(zx, zy), xytext=(zx + 2, zy))

plt.show()

print ('Limit as x -> ' + str(zx) + ' = ' + str(zy))
