# ML0120EN-1.1-Review-TensorFlow-Hello-World0

import tensorflow as tf

# Cria 2 constantes
a = tf.constant([2])
b = tf.constant([3])

# Cria uma soma
c = tf.add(a,b)

# Cria a Sessão
# session = tf.Session()
# Roda a sessão e imprime o resultado
# result = session.run(c)
# print(result)
# Fecha a sessão
# session.close()

with tf.Session() as session:
    result = session.run(c)
    print(result)

Scalar = tf.constant([2])
Vector = tf.constant([5,6,2])
Matrix = tf.constant([[1,2,3],[2,3,4],[3,4,5]])
Tensor = tf.constant( [ [[1,2,3],[2,3,4],[3,4,5]] , [[4,5,6],[5,6,7],[6,7,8]] , [[7,8,9],[8,9,10],[9,10,11]] ] )
with tf.Session() as session:
    result = session.run(Scalar)
    print("Scalar (1 entry):\n %s \n" % result)
    result = session.run(Vector)
    print("Vector (3 entries) :\n %s \n" % result)
    result = session.run(Matrix)
    print("Matrix (3x3 entries):\n %s \n" % result)
    result = session.run(Tensor)
    print("Tensor (3x3x3 entries) :\n %s \n" % result)

Matrix_one = tf.constant([[1,2,3],[2,3,4],[3,4,5]])
Matrix_two = tf.constant([[2,2,2],[2,2,2],[2,2,2]])

first_operation = tf.add(Matrix_one, Matrix_two)
second_operation = Matrix_one + Matrix_two

with tf.Session() as session:
    result = session.run(first_operation)
    print("Defined using tensorflow function :")
    print(result)
    result = session.run(second_operation)
    print("Defined using normal expressions :")
    print(result)

Matrix_one = tf.constant([[2,3],[3,4]])
Matrix_two = tf.constant([[2,3],[3,4]])

Matrix_one = tf.constant([[1,2,3],[2,3,4]])
Matrix_two = tf.constant([[2,2],[2,2],[2,2]])

Matrix_one = tf.constant([[2,3],[3,4],[4,5]])
Matrix_two = tf.constant([[2,2,2],[2,2,2]])

first_operation = tf.matmul(Matrix_one, Matrix_two)

with tf.Session() as session:
    result = session.run(first_operation)
    print("Defined using tensorflow function :")
    print(result)



