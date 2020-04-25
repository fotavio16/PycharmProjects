'''
    Jogo da Senha - Mastermind
    08-04-2020
'''

from random import randint, shuffle

class Senha():
    def __init__(self, tam):
        self.senha = list('0123456789')
        self.tamanho = tam

    def sorteia(self):
        for i in range(50):
            shuffle(self.senha)

        self.senha = self.senha[:self.tamanho]

    def mostra(self):
        return self.senha

    def consulta(self, tenta):
        certos = 0
        foradepos = 0
        for i, val in enumerate(self.senha):
            if tenta[i] == val:
                certos = certos + 1
            elif tenta[i] in self.senha:
                foradepos += 1
        return certos, foradepos




tamCodigo = 4
totalTentativas = 10

s = Senha(tamCodigo)

s.sorteia()

#print(s.mostra())
print("Este é o MASTERMIND.")
print(f'Você terá {totalTentativas} para acertar a SENHA num total de {tamCodigo} dígitos.')
print("BOA SORTE!")
print()

cont = 0

while True:
    cont += 1
    print(f'Tentativa nº {cont}')
    chute = str(input('Digite o seu palpite: '))
    naposi, foraposi = s.consulta(chute)
    print('Resultado: ')
    if naposi > 0:
        print(f'- {naposi} números na posição certa. ')
    if foraposi > 0:
        print(f'- {foraposi} números fora da posição correta.')
    if naposi + foraposi == 0:
        print('Nenhum número na senha.')
    print()

    if naposi == tamCodigo:
        print("Você acertou a SENHA.")
        print(f'A SENHA é {s.mostra()}. Parabéns!!!!')
        break

    if cont == totalTentativas:
        print("Você atingiu o máximo de tentativas.")
        print(f'A SENHA é {s.mostra()}. QUE PENA!!!! Tente novamente mais tarde.')
        break

print("Volte Sempre.")