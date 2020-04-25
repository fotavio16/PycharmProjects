totalGasto = 0
maisdeMil = 0
maisBarato = ['', 1000000.00]
while True:
    nome = str(input('nome do produto: '))
    preço = float(input('preço do produto: '))
    totalGasto += preço
    if preço > 1000:
        maisdeMil += 1
    if preço < maisBarato[1]:
        maisBarato[0] = nome
        maisBarato[1] = preço
    cont = str(input('Quer continuar(s/n)? ')).upper()
    if cont == 'N':
        break
print("-"*20)
print("Compras encerradas.")
print("O total gasto na compra foi de R${}.".format(totalGasto))
print("{} produtos custasm mais de R$1000.00.".format(maisdeMil))
print("O produto mais barato é {} no valor de {}.".format(maisBarato[0], maisBarato[1]))
