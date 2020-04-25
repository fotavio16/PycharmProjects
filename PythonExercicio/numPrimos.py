import numpy as np
import matplotlib.pyplot as plt

# Tamanho dos números
num = 200

# Cria a tabela dos num primeiros números inteiros
is_prime = np.ones((num,), dtype=bool)

# Elinina os 0 e 1 que não são primos
is_prime[:2] = 0

N_max = int(np.sqrt(len(is_prime) - 1))
is_busca = np.ones((N_max+1))
is_busca[:2] = 0

for i in range(2, N_max+1):
    is_busca[2*i::i] = False

busca = np.flatnonzero(is_busca)

#busca = np.arange(2,N_max+1)
print(busca)

for j in busca:
    is_prime[2*j::j] = False
    #print("Após retirar os múltiplos de {} a lista primos ficou:".format(j))
    #print(is_prime)

print(np.flatnonzero(is_prime))