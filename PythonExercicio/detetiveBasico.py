print("Olá. Meu nome é Robin.")
nome = str(input('Qual o seu nome? '))
print("{}, estou investigando o assassinato do Sr. Orozimbo.".format(nome))
soma = 0
r = [] # armazena as respostas
r.append(str(input('O senhor telefonou para a vítima (S/N)? ')).upper())
r.append(str(input('O senhor esteve no local do crime (S/N)? ')).upper())
r.append(str(input('O senhor mora perto da vítima (S/N)? ')).upper())
r.append(str(input('O senhor devia algo para o Sr. Orozimbo (S/N)? ')).upper())
r.append(str(input('O senhor já trabalhou com a vítima (S/N)? ')).upper())
for item in r:
    if item == 'S':
        soma += 1
print("Sr {}, de acordo com nossa investigação, é ".format(nome), end="")
if soma < 2:
    print("INOCENTE.")
elif soma < 3:
    print("SUSPEITO.")
elif soma < 5:
    print("CÚMPLICE.")
else:
    print("ASSASSINO.")
