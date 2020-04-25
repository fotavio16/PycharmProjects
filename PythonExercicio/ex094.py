cadastro = list()

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    resp = str(input('Quer continuar? (S/N) '))
    if resp in "Nn":
        break

print("-="*30)
total = len(cadastro)
print(f'- O grupo tem {total} pessoas.')
mulheres = list()
soma = 0
for p in cadastro:
    soma = soma + p['idade']
    if p['sexo'] in "Ff":
        mulheres.append(p['nome'])
media = soma / total
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}.')
print("- Lista das pessoas que estão acima da média:")
for p in cadastro:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print("<< ENCERRADO >>")
