print("Digite o nome, a idade e o sexo de 4 pessoas.")
somaIdade = 0
idadeMaior = 0
nomeMaisVelho = "nenhum"
menos20 = 0
for i in range(4):
    print("{}ª pessoa:".format(i+1))
    nome = str(input("Nome : "))
    idade = int(input("Idade : "))
    sexo = str(input("Sexo (M/F) : "))
    somaIdade += idade
    if sexo == "M":
        if idade > idadeMaior:
            idadeMaior = idade
            nomeMaisVelho = nome
    elif sexo == "F":
        if idade < 20:
            menos20 += 1
    else:
        print("Você digitou uma opção inválida")
        break
print("Resultados:")
print("A média de idade do grupo é {}.".format(somaIdade/4))
print("O nome do homem mais velho é {}.".format(nomeMaisVelho))
print("O total de mulheres com menos de 20 anos é {}.".format(menos20))
