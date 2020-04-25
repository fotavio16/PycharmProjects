from random import randint

# Cálculos iniciais
# Média Força Total - 10%
mediaForcaA = 50
mediaForcaB = 50

# Forças por setor - 40%
# Equipe A
goleiroA = 65
zagaA = 58
meioDefA = 60
meioCentA = 55
meioAtaqA = 65
atacanteA = 70
# Equipe B
goleiroB = 75
zagaB = 63
meioDefB = 67
meioCentB = 55
meioAtaqB = 49
atacanteB = 66

# Moral da Equipe - 20%
# Posição na tabela
# Jogos ganhos em sequência
# Somatório de vitórias, empates e derrotas
moralA = 75
moralB = 70

# Lotação do Estádio - 20%
lotacaoA = 6
lotacaoB = 4

# Fator Sorte - 10%
sorteA = randint(1,50)
sorteB = randint(1,50)

# Disputas de jogadas
# Etapa 1 - MeioDef x MeioCent ou MeioCent x MeioDef
# Etapa 2 - MeioAtaq x Zaga
# Etapa 3 - Atacante x Goleiro
# disputaA = mediaForcaA * 0.1 + setorA * 0.4 + moralA * 0.2 + lotacaoA * 0.2 + sorteA * 0.1
# disputaB = mediaForcaB * 0.1 + setorB * 0.4 + moralB * 0.2 + lotacaoB * 0.2 + sorteB * 0.1
def disputa(media, setor, moral, lotacao):
    sorte = randint(1,50)
    return media * 0.1 + setor * 0.4 + moral * 0.2 + lotacao * 0.2 + sorte * 0.1

# Define o vencedor de uma determinada jogada
def jogada(etapa, posseCasa):
    # Verifica a etapa
    if etapa == 1:
        # Testa a posse de bola
        if posseCasa:
            disputaP = disputa(mediaForcaA, meioDefA, moralA, lotacaoA)
            disputaD = disputa(mediaForcaB, meioCentB, moralB, lotacaoB)
        else:
            disputaD = disputa(mediaForcaA, meioCentA, moralA, lotacaoA)
            disputaP = disputa(mediaForcaB, meioDefB, moralB, lotacaoB)
    elif etapa == 2:
        # Testa a posse de bola
        if posseCasa:
            disputaP = disputa(mediaForcaA, meioAtaqA, moralA, lotacaoA)
            disputaD = disputa(mediaForcaB, zagaB, moralB, lotacaoB)
        else:
            disputaD = disputa(mediaForcaA, zagaA, moralA, lotacaoA)
            disputaP = disputa(mediaForcaB, meioAtaqB, moralB, lotacaoB)
    else: # Etapa igual a 3
        # Testa a posse de bola
        if posseCasa:
            disputaP = disputa(mediaForcaA, atacanteA, moralA, lotacaoA)
            disputaD = disputa(mediaForcaB, goleiroB, moralB, lotacaoB)
        else:
            disputaD = disputa(mediaForcaA, goleiroA, moralA, lotacaoA)
            disputaP = disputa(mediaForcaB, atacanteB, moralB, lotacaoB)
    if disputaP > disputaD:
        return True
    else:
        return False



