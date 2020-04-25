from random import randint
import time

def programa1():
    '''
    Faça um programa que converta da notação de 24 horas para a
    notação de 12 horas. Por exemplo, o programa deve converter
    14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
    Deve haver pelo menos duas funções: uma para fazer a conversão
    e uma para a saída. Registre a informação A.M./P.M. como
    um valor 'A' para A.M. e 'P' para P.M. Assim, a função para
    efetuar as conversões terá um parâmetro formal para
    registrar se é A.M.
    :return:
    '''

    print("Digite a hora no formaro de 24 horas no formato HH:MM - ")
    while True:
        hora24 = str(input())
        if ':' not in hora24:
            print("FORMATO INCORRETO! Digite a hora no formato HH:MM - ")
        else:
            break

    converte24p12(hora24)


def converte24p12(hora):
    [horas, minutos]  = hora.split(':')
    horas = int(horas)
    if horas > 11:
        horas = horas - 12
        ampm = 'PM'
    else:
        ampm = 'AM'
    print(f'A hora no formato 12 horas é {str(horas)}:{minutos} {ampm}.')



def programa2():
    '''
    Jogo de Craps. Faça um programa de implemente um jogo de
    Craps. O jogador lança um par de dados, obtendo um valor
    entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11,
    você é um "natural" e ganhou. Se você tirar 2, 3 ou 12 na
    primeira jogada, isto é chamado de "craps" e você perdeu.
    Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
    este é seu "Ponto". Seu objetivo agora é continuar jogando
    os dados até tirar este número novamente. Você perde, no
    entanto, se tirar um 7 antes de tirar este Ponto novamente.
    :return:
    '''

    print("#%#%# JODO DE CRAPS #%#%#")
    jogadas = 0
    while True:
        jogadas += 1
        print(f'Sua {jogadas}ª jogada. Primeiro dado:')
        parDados = lancaDado()
        print("Segundo dado...")
        parDados += lancaDado()
        if jogadas == 1:
            if parDados == 7 or parDados == 11:
                print("Você é um NATURAL!")
                print("Você ganhou!!!")
                break
            elif parDados == 2 or parDados == 3 or parDados == 12:
                print("Você tirou CRAPS. Sinto dizer que Você perdeu!!!")
                break
            else:
                ponto = parDados
        else:
            if parDados == ponto:
                print("Você acertou o ponto novamente.")
                print("Você é o vencedor!!")
                break
            elif parDados == 7:
                print("Que pena. Você tirou 7. Você perdeu.")
                break
        time.sleep(3)

def lancaDado():
    print("Atenção...")
    time.sleep(1)
    dado = randint(1,6)
    print(f'Você tirou {dado}...')
    return dado

def programa3():
    '''
    Data com mês por extenso. Construa uma função que receba
    uma data no formato DD=MM=AAAA e devolva uma string no
    formato D de mesPorExtenso de AAAA. Opcionalmente, valide
    a data e retorne NULL caso a data seja inválida.
    :return:
    '''


def programa4():
    '''
    Desenha moldura. Construa uma função que desenhe um retângulo
    usando os caracteres '+' , '-' e '|'. Esta função deve
    receber dois parâmetros, linhas e colunas, sendo que o valor
    por omissão é o valor mínimo igual a 1 e o valor máximo é
    20. Se valores fora da faixa forem informados, eles devem
    ser modicados para valores dentro da faixa de forma
    elegante.
    :return:
    '''

    desenhaRet(7,10)


def desenhaRet(l=1,c=1):
    if l < 1:
        l = 1
    if l > 20:
        l = 20
    if c < 1:
        c = 1
    if c > 20:
        c = 20

    #Primeira linha
    print('+', end='')
    for i in range(c-2):
        print('-', end='')
    print('+')
    # Linhas Intermediárias
    for j in range(l-2):
        print('|', end='')
        for i in range(c-2):
            print(' ', end='')
        print('|')
    #Última  linha
    print('+', end='')
    for i in range(c-2):
        print('-', end='')
    print('+')

programa4()
