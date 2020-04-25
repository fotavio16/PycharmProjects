import matplotlib.pyplot as plt
plt.figure(1)                # a primeira figura
plt.subplot(211)             # o primeiro subplot na primeira figura
plt.plot([1, 2, 3])
plt.subplot(212)             # o segundo subplot na primeira figura
plt.plot([4, 5, 6])


plt.figure(2)                # a segunda figura
plt.plot([4, 5, 6])          # cria um subplot(111) por default

plt.figure(1)                # figure 1 é atual; subplot(212) ainda é atual
plt.subplot(211)             # faz subplot(211) na figure 1 atual
plt.title('Easy as 1, 2, 3') # título subplot 211

plt.show()
