'''
pessoas = {'nome': 'Fernando', 'sexo': 'M', 'idade': 36}

for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)

estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
'''
boletim = {}
boletim['Nome'] = str(input("Nome: "))
boletim['Média'] = float(input(f"Média de {boletim['Nome']}: "))
if boletim['Média'] < 6.0:
    boletim['Situação'] = "Reprovado"
else:
    boletim['Situação'] = "Aprovado"

for k, v in boletim.items():
    print(f'{k} é igual a {v}.')

