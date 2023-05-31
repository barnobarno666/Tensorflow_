import matplotlib.pyplot as plt
import random
import numpy as np
from sklearn.linear_model import LinearRegression
#import tensorflow as tf 
# values=[0]*50
# for i in range(50):
#     values[i]=random.randint(0,100)
#     plt.xlim(0,50)
#     plt.ylim(0,100)
#     plt.bar(list(range(50)),values)
#     plt.pause(.0001)
# plt.show()
xx=[(25*np.sin(.05*i)) for i in range(1000)]
#yy=[(i)  for i in range(100)]
x_values=[]
y_values=[]
reg=LinearRegression()
for i in range(1000):
    plt.clf()
    if i%7==0:
        x_values.append(i)
        y_values.append(xx[i])
    plt.xlim(0,1000)
    plt.ylim(-100,100)
    x=np.array(x_values)
    x=x.reshape(-1,1)
    y=np.array(y_values)
    y=y.reshape(-1,1)
    reg.fit(x,y)
    plt.scatter(x,y,color='black')
    plt.plot(list(range(100)),reg.predict(np.array([x for x in range(100)]).reshape(-1,1)) )
    plt.pause(.001)
    plt.legend('hello')
    #plt.text(3, 8, 'some text', fontsize=1400)
    

plt.show()
