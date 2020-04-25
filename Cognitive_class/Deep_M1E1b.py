# ML0120EN-1.1-Review-TensorFlow-Hello-World0
# Variáveis

import tensorflow as tf

state = tf.Variable(0)
one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)

init_op = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init_op)
    #print(session.run(state))
    for _ in range(4):
        print(session.run(state))
        session.run(update)

a = tf.placeholder(tf.float32)

b = a*2

with tf.Session() as sess:
    result = sess.run(b,feed_dict={a:5.5})
    print(result)

dictionary={a: [ [ [1,2,3],[4,5,6],[7,8,9],[10,11,12] ] , [ [13,14,15],[16,17,18],[19,20,21],[22,23,24] ] ] }

with tf.Session() as sess:
    result = sess.run(b,feed_dict=dictionary)
    print(result)

