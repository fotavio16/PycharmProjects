print("### C A L C U L A D O R A ##")
print("")
print("Digite dois valores:")
num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))
print("")
print("[ 1 ] Somar")
print("[ 2 ] Multiplicar")
print("[ 3 ] Maior")
print("[ 4 ] Novos Números")
print("[ 5 ] Sair do programa")
sair = False
while (not sair):
    option = int(input("Digite a sua opção: "))
    if option == 1:
        print("A soma de {} mais {} é {}.".format(num1, num2, num1+num2))
    elif option == 2:
        print("O produto de {} vezes {} é {}.".format(num1, num2, num1*num2))
    elif option == 3:
        if num1 > num2:
            print("{} é maior que {}.".format(num1, num2))
        elif num1 < num2:
            print("{} é maior que {}.".format(num2, num1))
        else:
            print("Os dois números são iguais")
    elif option == 4:
        print("Digite os dois novos valores:")
        num1 = float(input("Primeiro valor: "))
        num2 = float(input("Segundo valor: "))
    elif option == 5:
        print("O programa foi encerrado.")
        sair = True
    else:
        print("Opção inválida. Digite novamente.")

