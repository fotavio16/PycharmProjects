# Sequência de Fibonacci

import tensorflow as tf

n = int(input("Digite o número de termos da sequência de Fibonacci: "))
val2 = tf.Variable(1)
val1 = tf.Variable(1)
valor = tf.Variable(0)

soma = tf.add(val1,val2)
oper1 = tf.assign(valor,soma)
oper2 = tf.assign(val2, val1)
oper3 = tf.assign(val1, valor)
init_op = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init_op)
    print("Sequência de {} primeiros termos de Fibonacci: {}, {}".format(n, session.run(val2), session.run(val1)), end="")
    for i in range(n-2):
        session.run(oper1)
        session.run(oper2)
        session.run(oper3)
        print(", {}".format(session.run(valor)), end="")

print("... FIM")