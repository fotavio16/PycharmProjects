total = 0
mais18 = 0
homens = 0
mulheres20 = 0
while True:
    pessoa = str(input('Digite o nome da pessoa: '))
    total += 1
    idade = int(input('Digite a idade da pessoa: '))
    if idade > 18:
        mais18 += 1
    sexo = str(input('Digite o sexo da pessoa (M/F: ')).upper()
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres20 += 1
    continua = str(input('Quer continuar (S/N)? ')).upper()
    if continua == 'N':
        break
print("De um total de {} pessoas, {} são pessoas maiores de 18 anos,".format(total, mais18), end='')
print(" {} são homens e {} são mulheres com menos de 20 anos.".format(homens,mulheres20))
