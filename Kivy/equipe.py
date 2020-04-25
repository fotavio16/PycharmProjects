import csv

# Rotina responsável por carregar os jogadores numa equipe
def montaEquipe(time, formacao):
    escalacao = []
    with open('jogadores.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for j in readCSV:
            if j[1] == time:
                escalacao.append(j)
    return escalacao

