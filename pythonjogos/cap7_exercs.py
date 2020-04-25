def programa1():
    '''
    Verificação de CPF.
    Programa que solicita a digitação de um número de CPF
    no formato xxx:xxx:xxx-zz
    Verifique se é um número válido ou inválido através da
    validação dos dígitos verificadores e dos caracteres de
    formatação.
    Dica: faça uma pesquisa na internet para entender como é vericado se um CPF é
válido ou não.
    :return:
    '''

    print("Digite o número de CPF no formato xxx:xxx:xxx-zz")
    cpf = [' ' for i in range(11)]
    for i in range(11):
        cpf[i] = int(input())
        imprimeCPF(cpf)
    if validaDigitos(cpf):
        print("CPF Válido.")
    else:
        print("CPF Inválido.")


def validaDigitos(cpf):
    digito1 = cpf[9]
    digito2 = cpf[10]
    soma1 = 0
    soma2 = cpf[9] * 2
    multiplicador1 = 10
    multiplicador2 = 11
    for i in range(9):
        soma1 += cpf[i] * multiplicador1
        soma2 += cpf[i] * multiplicador2
        multiplicador1 -= 1
        multiplicador2 -= 1
    verificador1 = (soma1 * 10) % 11
    verificador2 = (soma2 * 10) % 11
    if verificador1 == digito1 and verificador2 == digito2:
        return True
    else:
        return False


def imprimeCPF(cpf):
    print(f'{cpf[0]}{cpf[1]}{cpf[2]}.', end='')
    print(f'{cpf[3]}{cpf[4]}{cpf[5]}.', end='')
    print(f'{cpf[6]}{cpf[7]}{cpf[8]}-', end='')
    print(f'{cpf[9]}{cpf[10]}')


def programa2():
    '''
    Damas do Xadrez. Desenvolva um programa que dado duas
    posições em um jogo de xadrez retorne quantas jogadas
    é preciso para uma dama se mover da primeira para a
    segunda posição.
    :return:
    '''


def programa3():
    '''
    Crie um programa que dada um sequencia de n números
    ordene em ordem decrescente.
    :return:
    '''


def programa4():
    '''
    Quadrado mágico. Um quadrado mágico é aquele dividido
    em linhas e colunas, com um número em cada posição e
    no qual a soma das linhas, colunas e diagonais é a mesma.
    Por exemplo, veja um quadrado mágico de lado 3, com
    números de 1 a 9:
    Elabore um programa que receba como entrada um quadrado
    3x3 e retorne se ele é ou não um quadrado mágico.
    Receber qualquer quadrado nxn, o valor de n deve ser o
    primeiro valor fornecido ao programa.
    :return:
    '''

    n = int(input("Qual o tamanho do quadrado? 3x3, 4x4, 5x5 ou maior? "))
    maior = n * n
    soma = maior * (maior + 1) / (n * 2)
    quadrado = entradaQuadrado(n)

    # Testa as linhas
    for i in range(n):
        if not validaGrupo(quadrado[i],soma):
            print("Não é Quadrado Mágico")
            break
    else: # Testa as Colunas
        for i in range(n):
            grupo = []
            for j in range(n):
                grupo.append(quadrado[i][j])
            if not validaGrupo(grupo,soma):
                print("Não é Quadrado Mágico")
                break
        else: # Testa diagonais
            grupo = []
            for i in range(n):
                grupo.append(quadrado[i][i])
            if not validaGrupo(grupo,soma):
                print("Não é Quadrado Mágico")
            else:
                grupo = []
                for i in range(n):
                    grupo.append(quadrado[i][abs(i-n+1)])
                if not validaGrupo(grupo,soma):
                    print("Não é Quadrado Mágico")
                else:
                    print("É um Quadrado Mágico")


def entradaQuadrado(n):
    print("Digite os números um de cada vez:")
    quadrado = [[0] * n for i in range(n)]
    print(quadrado)

    for i in range(n):
        for j in range(n):
            quadrado[i][j] = int(input("Digite o próximo valor: "))
            imprimeQuad(quadrado,n)

    return quadrado


def imprimeQuad(quadrado, n):
    for i in range(n):
        print(quadrado[i])

def validaGrupo(grupo, soma):
    total = 0
    for elem in grupo:
        total += elem
    return total == soma



programa1()