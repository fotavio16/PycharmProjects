print("Lista de números pares no intervalo.")
init = int(input("Digite o intervalo inicial: "))
fim = int(input("Digite o final do intervalo: "))-1
if init%2 != 0:
    init += 1
for i in range(init, fim, 2):
    print("{}, ".format(i), end="")
if fim%2 == 0:
    print("{}.".format(fim))
else:
    print("{}.".format(fim+1))