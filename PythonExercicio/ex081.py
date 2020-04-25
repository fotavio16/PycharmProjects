valores = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    cont = str(input('Quer continuar? [S/N] ')).upper()
    if cont == 'N':
        break

print(f'Você digitou {len(valores)} elememtos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista.')