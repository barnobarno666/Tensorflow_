import pandas
import time
import tensorflow as tf
start=time.time() 
d=tf.Variable(['test'],tf.string)
print(tf.rank(d))
#f=tf.reshape(d, 2)
print(d.shape)
d=tf.ones([5,5,5,5])

print(d)
#with open('file.txt','w') as f:
#    f.write(str(d))
#f.close()
tf.reshape(d, [])
print(d)
print(time.time()-start)