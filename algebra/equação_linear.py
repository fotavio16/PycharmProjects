import pandas as pd

# Cria os valores de x como um dataframe
dados = pd.DataFrame({'x': range(-10, 11)})

# Determina os valores de y de acordo com equação y = 3x + 5
dados['y'] = 3*dados['x'] + 5

print(dados)

# Vamos criar o gráfico dessa equação
from matplotlib import pyplot as plt
plt.plot(dados.x, dados.y, color='blue', marker='o')
plt.grid()
plt.axhline()
plt.axvline()
plt.xlabel('x')
plt.ylabel('y')
#plt.annotate('interseção_x', (-1.666, 0))
#plt.annotate('interseção_y', (0, 5))
a = 3 # inclinação da reta
yInt = 5
xInt = -1.666
ax = [xInt, 0]
ay = [0, yInt]
plt.plot(ax, ay, color='red', lw=4)
plt.show()


