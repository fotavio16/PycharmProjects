n = int(input("Digite o número de elementos da Sequência de Fibonacci: "))
fn2 = 0
fn1 = 1
print('{} -> {} -> '.format(fn2, fn1), end='')
cont = 3
while cont <= n:
    f = fn1 + fn2
    print('{} -> '.format(f), end='')
    fn2 = fn1
    fn1 = f
    cont += 1
print('FIM')
