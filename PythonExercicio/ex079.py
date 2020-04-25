valores = []

while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(num)
    cont = str(input('Quer continuar? [S/N] ')).upper()
    if cont == 'N':
        break

print(f'Você digitou os valores {valores}.')