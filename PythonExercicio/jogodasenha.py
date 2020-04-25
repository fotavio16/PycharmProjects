# Jogo da Senha
# Com 3 casas sem repetição de números  e 6 rodadas no máximo
from random import randint

def valida(senha,tenta):
    emcheio = 0
    emparte = 0
    for i in range(len(tenta)):
        if tenta[i] == senha[i]:
            emcheio += 1
        elif tenta[i] in senha:
            emparte += 1
    if emcheio == len(senha):
        return "ACERTOU! FIM DE JOGO."
    else:
        return f'posição certa = {emcheio} posição errada = {emparte}'


# Escolhe a senha
senha = list()
tamanho = 3
while len(senha) < tamanho:
    sorteio = randint(0,9)
    if sorteio not in senha:
        senha.append(sorteio)
print("SENHA CRIADA!")
print(" [ ] [ ] [ ]")

# Recebe os palpites
maxTries = 6
tentativa = 1
while tentativa <= maxTries:
    print(f'{tentativa}º Tentativa:')
    dito = list()
    for i in range(tamanho):
        num = int(input(f'Digite o {i+1}º nº: '))
        dito.append(num)
    print(dito)
    resp = valida(senha,dito)
    print(resp)
    if resp == "ACERTOU! FIM DE JOGO.":
        break
    tentativa += 1
if tentativa > maxTries:
    print("ACABOU O TEMPO! VOCÊ PERDEU!")
