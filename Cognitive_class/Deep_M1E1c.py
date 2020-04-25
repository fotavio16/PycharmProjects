import matplotlib
import tensorflow as tf

# Cria 2 constantes
a = tf.constant([5])
b = tf.constant([2])

# Cria uma soma
c = a + b

# Cria uma multiplicação
d = a * b

# Executa a sessão
with tf.Session() as session:
    result1 = session.run(c)
    print("A soma das duas constantes é : {0}".format(result1))
    result2 = session.run(d)
    print("O produto das duas constantes é : {0}".format(result2))

# Multiplicação de matrizes
matrixA = tf.constant([[2,3],[3,4]])
matrixB = tf.constant([[2,3],[3,4]])

first_operation = tf.multiply(matrixA, matrixB)
second_operation = tf.matmul(matrixA, matrixB)

with tf.Session() as session:
    result = session.run(first_operation)
    print("Element-wise multiplication: \n", result)

    result = session.run(second_operation)
    print("Matrix Multiplication: \n", result)

a = tf.constant(1000)
b = tf.Variable(0)
init_op = tf.global_variables_initializer()

b = a + 1

with tf.Session() as session:
    session.run(init_op)
    print(session.run(b))
