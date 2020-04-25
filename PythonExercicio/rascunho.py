import numpy as np
import matplotlib.pyplot as plt

# Carrega os dados
data = np.loadtxt('data/populations.txt')
year, hares, lynxes, carrots = data.T

# Plotar os dados
plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, year, lynxes, year, carrots)
plt.legend(('Lebres', 'Linces', 'Cenouras'), loc=(1.02, 0.5))
plt.show()

populations = data[:, 1:]
print(populations.mean(axis=0))