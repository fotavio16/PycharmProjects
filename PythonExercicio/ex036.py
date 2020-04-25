print("Sistema de Aprovação de Empréstimo:")
valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário atual: "))
prazo = int(input("Digite o prazo do empréstimo em anos: "))
prestacao = valor / (prazo*12)
if prestacao > salario*0.3:
    print("O empréstimo foi negado pois a prestação ultrapassa o valor de 30% do salário")
else:
    print("O valor da prestação é de R$ {:.2f} por mês.".format(prestacao))
