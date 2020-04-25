print("Tabuada dos Números")
print('-\/'*7)
print("Entre com um valor por vez. Tecle um número negativo para parar.")
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for i in range(1, 11):
        print(" {} x {} = {}".format(i, num, i*num))
    print('-' * 15)
print("Programa Encerrado.")
