cadastro = dict()

cadastro['nome'] = str(input("Nome: "))
ano = int(input("Ano de Nascimento: "))
cadastro['idade'] = 2018 - ano
cadastro['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input("Ano de contratação: "))
    cadastro['salário'] = float(input("Salário: "))

for k, v in cadastro.items():
    print(f"{k} tem o valor {v}")
