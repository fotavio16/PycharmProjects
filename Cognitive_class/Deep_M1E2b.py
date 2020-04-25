# modelling a linear relationship between "chirps of a cricket" and ground temperature.

# Let's import tensorFlow and python dependencies
import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

# Download and Explore the Data
df = pd.read_csv("PierceCricketData.csv")
print(df.head())

# Plot the Data Points
x_data, y_data = (df["Chirps"].values,df["Temp"].values)

# plots the data points
plt.plot(x_data, y_data, 'ro')
# label the axis
plt.xlabel("# Chirps per 15 sec")
plt.ylabel("Temp in Farenhiet")

# Create a Data Flow Graph using TensorFlow
X = tf.placeholder(tf.float32, shape=(x_data.size))
Y = tf.placeholder(tf.float32, shape=(y_data.size))

m = tf.Variable(3.0)
c = tf.Variable(2.0)

# Construindo o Modelo
Ypred = tf.add(tf.multiply(X, m), c)

# Create and Run a Session to Visualize the Predicted Line
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

pred = sess.run(Ypred, feed_dict={X:x_data})

#plot initial prediction against datapoints
plt.plot(x_data, pred)
plt.plot(x_data, y_data, 'ro')
# label the axis
plt.xlabel("# Chirps per 15 sec")
plt.ylabel("Temp in Farenhiet")


# normalization factor
nf = 1e-1

# seting up the loss function
loss = tf.reduce_mean(tf.squared_difference(Ypred*nf,Y*nf))

# Define an Optimization Graph to Minimize the Loss and Training the Model

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
#optimizer = tf.train.AdagradOptimizer(0.01 )

# pass the loss function that optimizer should optimize on.
train = optimizer.minimize(loss)

# Initialize all the vairiables again
sess.run(tf.global_variables_initializer())

# Run session to train and predict the values of 'm' and 'c'
convergenceTolerance = 0.0001
previous_m = np.inf
previous_c = np.inf

steps = {}
steps['m'] = []
steps['c'] = []

losses=[]

for k in range(100000):
    # run a session to train , get m and c values with loss function
    _, _m, _c, _l = sess.run([train, m, c, loss], feed_dict={X: x_data, Y: y_data})

    steps['m'].append(_m)
    steps['c'].append(_c)
    losses.append(_l)
    if (np.abs(previous_m - _m) <= convergenceTolerance) or (np.abs(previous_c - _c) <= convergenceTolerance):
        print("Finished by Convergence Criterion")
        print("k = {}".format(k))
        print("Loss = {}".format(_l))
        print("m = {}".format(_m))
        print("c = {}".format(_c))
        break
    previous_m = _m,
    previous_c = _c,

sess.close()

plt.plot(losses[:])
plt.show()
