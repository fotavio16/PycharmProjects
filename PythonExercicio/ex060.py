fatorial = 1
num = int(input("Digite o número para calcular o fatorial: "))
temp = num
while temp > 1:
    fatorial = fatorial * temp
    temp -= 1
print("O fatorial de {} é igual a {}".format(num, fatorial))
