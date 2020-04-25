valores = []
for i in range(5):
    print(f'vakores = {valores}.')
    num = int(input(f'Digite um valor para a Posição {i}: '))
    fim = True
    for p, v in enumerate(valores):
        if v > num:
            valores.insert(p, num)
            fim = False
            break
    if fim:
        valores.append(num)

print(f'Você digitou os valores {valores}.')
