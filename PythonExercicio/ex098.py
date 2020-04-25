# Rotina que realiza contagens
def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if passo == 0:
        passo = 1
    if (inicio > fim) and (passo > 0):
        passo = -passo
    while True:
        print(f'{inicio} ',end='')
        inicio += passo
        if (inicio > fim) and (passo > 0):
            break
        elif (inicio < fim) and (passo < 0):
            break
    print("FIM!")
    pass


contador(1,10,1)
contador(10,0,2)
print("Agora é a sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim:    "))
p = int(input("Passo:  "))
contador(i,f,p)

