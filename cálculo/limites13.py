'''
    Limites - Asymptotes and Infinity - 01
    d(x)=4 / (x−25), x≠25
 '''

# Plota a Função
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    if x != 25:
        return 4 / ( x - 25)


# Cria os arrays de valores de x de -100 a 100
x = list(range(-100,24))
x.append(24.9) # Valores fracionados em torno de 25
x.append(25)
x.append(25.1)
x = x + list(range(26, 101))

# Gera os valores de y correspondentes
y = [f(i) for i in x]

# Configura o Gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()

# Plota a função
plt.plot(x, y, color='purple')

plt.show()

