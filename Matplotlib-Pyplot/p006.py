import numpy as np
import matplotlib.pyplot as plt

# Fixação de estado aleatório
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# O histograma dos dados
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Inteligências')
plt.ylabel('Probabilidade')
plt.title('Histograma de QI')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()