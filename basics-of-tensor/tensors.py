import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# initialization of tensor

x = tf.constant(4)
print(x)
# create a matrix
z = tf.constant([[1,2,3],[4,5,6]])
print(z)
# create a ones matrix
a = tf.ones((3,3))
print(a)
# create zeros matrix
b = tf.zeros((2,3))
print(b)
# create a Identity matrix 3 x 3
c = tf.eye(3)
print(c)
# standard distribution between -1 y 1
d = tf.random.normal((3,3), mean=0, stddev=1)
print(d)
# uniform distribution 0 1
e = tf.random.uniform((1,3), minval=0, maxval = 1)
print(e)

## adding the characateristics
y = tf.constant(4, shape=(1,1), dtype=tf.float32)
print(y)