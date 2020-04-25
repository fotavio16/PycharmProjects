print("Caixa Eletrônico Virtual!")
print("<>"*15)
valor = int(input("Digite o valor a ser sacado (sem centavos): "))
print("O valor solicitado de {} reais será entregue com ".format(valor), end='')
cont = 0
#valores = [50, 20, 10, 1]
valores = [100, 50, 20, 10, 5, 2, 1]
notas = []
while True:
    if valor >= valores[cont]:
        notas.append(int(valor/valores[cont]))
        valor = valor % valores[cont]
        print("{} notas de R${}, ".format(notas[cont], valores[cont]), end='')
    else:
        notas.append(0)
    cont += 1
    if valor == 0:
        break
print(" e obrigado pela preferência.")
