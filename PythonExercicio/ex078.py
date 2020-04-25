valores = []
for i in range(5):
    valores.append(int(input(f'Digite um valor para a Posição {i}: ')))
print('=-'*30)
print(f'Você digitou os valores {valores}')
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {maior} nas posições ',end='')
temp = valores
real = -1
for i in range(valores.count(maior)):
    pos = temp.index(maior)
    real = real + pos + 1
    print(f'{real}... ',end='')
    if pos+1 == len(temp): break
    temp = temp[pos+1:]
print()
print(f'O menor valor digitado foi {menor} nas posições ',end='')
temp = valores
real = -1
for i in range(valores.count(menor)):
    pos = temp.index(menor)
    real = real + pos + 1
    print(f'{real}... ',end='')
    if pos+1 == len(temp): break
    temp = temp[pos+1:]
print()
