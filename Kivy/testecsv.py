import csv

# Rotina responsável por carregar os jogadores numa equipe
def monta(time, formacao):
    escalacao = []
    with open('jogadores.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for j in readCSV:
            if j[1] == time:
                escalacao.append(j)
    return escalacao

with open('exemplo.csv') as csvfile:
    #readCSV = csv.reader(csvfile, delimiter=',')
    #for row in readCSV:
    #    print(row)
    #    print(row[0])
    #    print(row[0],row[1],row[2],)
    reader = csv.DictReader(csvfile, delimiter=',')
    dict_list = []
    for line in reader:
        dict_list.append(line)

    print(dict_list)

timeCasa = monta('Vasco da Gama','442')
for i in range(len(timeCasa)):
    print(timeCasa[i])
