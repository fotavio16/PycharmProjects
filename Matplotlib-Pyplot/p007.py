import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import NullFormatter  # útil para escalas `logit`

# Fixação de estado aleatório
np.random.seed(19680801)

# Prepara alguns dados no intervalo ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plota com diferentes escalas de eixos
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Formata os rótulos de escala menores do eixo y em cadeias vazias com
# `NullFormatter`, para evitar sobrecarregar o eixo com muitas legendas.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Ajuste o layout do subplot, porque o logit pode levar mais espaço
# do que o habitual, devido aos rótulos y-tick, como "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
