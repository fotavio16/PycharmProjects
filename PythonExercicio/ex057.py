sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input("Digite o sexo da pessoa (M/F): "))
if sexo == "M":
    print("O sexo da pessoa é masculino.")
else:
    print("O sexo da pessoa é feminino.")