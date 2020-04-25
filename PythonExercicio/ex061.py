inicial = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
contador = 0
maximo = 10
continua = True
while continua == True:
    while contador < maximo:
        contador += 1
        print("O {}º termo da PA é {}.".format(contador, inicial + razao * (contador - 1)))
    mais = int(input("Quer mostrar mais termos? Digite a quantidade de termos adicionais ou 0 para encerrar: "))
    if mais == 0:
        continua = False
        print("Ok. Processo encerrado.")
    else:
        maximo += mais
