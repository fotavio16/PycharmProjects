print("Entre com os números. Digite 999 para parar.")
quant = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    quant += 1
    soma += num
print("Foram digitados {} números, cuja soma é {}.".format(quant, soma))
