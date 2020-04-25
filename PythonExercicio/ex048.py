import numpy as np

print("Soma dos números ímpares e múltiplos de três no intervalo.")
init = int(input("Digite o intervalo inicial: "))
if init%3 == 0:
    inicio = init
else:
    inicio = init + 3 - init%3

fim = int(input("Digite o final do intervalo: "))+1

# Calculando a soma com loop
soma = 0
for i in range(inicio, fim, 3):
    if i%2 != 0:
        soma += i
print("O valor da soma dos números ímpares e múltiplos de três no intervalo de {} e {} é {}.".format(init,fim-1,soma))

# Calculando com a fórmula da Soam de uma PA
if init%3 == 0: # Verifica se o intervalo inicial é o primeiro termo da PA
    if init%2 != 0:
        inicio = init
    else: # Caso contrário ajusta o inicio da PA
        inicio = init + 3
else:
    inicio = init + 3 - init%3
    if inicio%2 == 0:
        inicio += 3
fim -= 1
if fim%3 == 0:
    if fim%2 != 0:
        final = fim
    else:
        final = fim - 3
else:
    final = fim - fim%3
    if final%2 == 0:
        final -= 3

n = np.floor((final - inicio) / 6) + 1
somaPA = int((inicio + final) * n / 2)
print("O valor da soma dos números ímpares e múltiplos de três no intervalo de {} e {} é {}.".format(init,fim,somaPA))