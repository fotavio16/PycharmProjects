soma = 0
cont = 0
flag = True
while flag == True:
    n = int(input('Digite o próximo número (999 para parar): '))
    if n == 999:
        flag = False
    else:
        cont += 1
        soma += n
print("Foram digitados {} números, cuja soma é {}.".format(cont, soma))

