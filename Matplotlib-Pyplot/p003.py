import numpy as np
import matplotlib.pyplot as plt

# tempo uniformemente amostrado em intervalos de 200 ms
t = np.arange(0., 5., 0.2)

# traços vermelhos, quadrados azuis e triângulos verdes
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
