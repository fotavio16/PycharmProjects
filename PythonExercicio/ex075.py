valores = tuple(int(input("Digite um número: ")) for _ in range(4))

print("Você digitou os valores: ", end='')
for v in valores:
    print(f'{v} ',end='')
print()
print(f'O valor 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'O primeiro 3 foi digitado na posição {valores.index(3)+1}.')
else:
    print("Não foi digitado o número 3 na sequência.")

print("Os números pares são: ")
for v in valores:
    if (v % 2) == 0:
        print(f'{v} ', end='')
print()
