print('%' *30)
print("Conversor de temperaturas")
print('%' *30)
opcao = input('Para qual temperatura quer converter? Celcius(C) ou Fahrenheit(F): ')
if opcao.upper() == 'C':
    f = float(input('Entre com a temperatura em fahrenheit: '))
    c = 5 * (f - 32) / 9
    print(" A temperatura em graus celcius é {}.".format(c))
elif opcao.upper() == 'F':
    c = float(input('Entre com a temperatura em celcius: '))
    f = 9 * c / 5 + 32
    print(" A temperatura em graus fahrenheit é {}.".format(f))
else:
    print("Opção inválida.")
