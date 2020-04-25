pessoas = []
menor = 1000
maior = -1

while True:
    num = []
    num.append(str(input("Nome: ")))
    num.append(float(input("Peso: ")))
    pessoas.append(num[:])
    if num[1] == maior:
        pesadas.append(num[0])
    if num[1] > maior:
        maior = num[1]
        pesadas = [num[0]]
    if num[1] == menor:
        leves.append(num[0])
    if num[1] < menor:
        menor = num[1]
        leves = [num[0]]
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'nN':
        break

print('-='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for p in pesadas:
    print(f'[{p}] ',end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ',end='')
for p in leves:
    print(f'[{p}] ',end='')
print()
