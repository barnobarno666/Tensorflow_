import matplotlib.pyplot as plt
import tensorflow as tf
#from tensorflow import keras
from keras.models import Model
from keras.layers import Dense
from keras.models import Sequential
import numpy as np
import shutil
#make the model
model_nn=Sequential([
    Dense(units=20,activation='relu',input_dim=1),
    Dense(units=25,activation='relu'),
    Dense(units=25,activation='relu'),
   Dense(units=25,activation='relu'),
    Dense(units=1)
        ])

import time
name=str(time.time())+'.png'
#is this model enough ?
data_y=np.array([(np.sin(10*i)) for i in np.linspace(0,1,90) ]).reshape(-1,1)
data_x=np.array([i for i in np.linspace(0,1,90) ]).reshape(-1,1)

#7 is good\
model_nn.compile( optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])
for i in range(1,100):
    model_nn.fit(data_x,data_y,epochs=i, verbose=1, batch_size=32)
    y=model_nn.predict(data_x)
    plt.scatter(data_x,data_y,color='red')
    plt.xlim(0,1)
    plt.ylim(-2,2)
    plt.plot(data_x,y,color='blue')
    plt.xlabel(f'Epoch= {i}',fontsize=25)
    plt.savefig(name)
    plt.figure(facecolor='white') 
    shutil.move(r'C:\Users\defaultuser0.LAPTOP-LRB3T941\Documents\Tensorflow'+f'\{name}', r'C:\Users\defaultuser0.LAPTOP-LRB3T941\Documents\Tensorflow\Numpy\ANI'+ f'\{i}' +'.png' )

#plt.show()
