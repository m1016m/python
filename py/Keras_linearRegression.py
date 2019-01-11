# -*- coding: utf-8 -*-
"""
Keras_linearRegression.py
Created on Tue Dec  5 22:26:19 2017
"""
import pandas as pd
import numpy as np
import seaborn as sns

from keras.layers import Dense
#from keras.models import Model, Sequential
from keras.models import Sequential
#from keras import initializers

## ---------- Create our linear dataset ---------------
## Set the mean, standard deviation, and size of the dataset, respectively
mu, sigma, size = 0, 4, 100

## Set the slope (m) and y-intercept (b), respectively
m, b = 2, 100

## Create a uniformally distributed set of X values between 0 and 10 and store in pandas dataframe
x = np.random.uniform(0,10, size)
df = pd.DataFrame({'x':x})

## Find the "perfect" y value corresponding to each x value given
df['y_perfect'] = df['x'].apply(lambda x: m*x+b)


## Create some noise and add it to each "perfect" y value to create a realistic y dataset
df['noise'] = np.random.normal(mu, sigma, size=(size,))
df['y'] = df['y_perfect']+df['noise']

## Plot our noisy dataset with a standard linear regression 
## (note seaborn, the plotting library, does the linear regression by default)
ax1 = sns.regplot(x='x', y='y', data=df)

##---------- Create our Keras Model -----------------
## Create our model with a single dense layer, with a linear activation function and glorot (Xavier) input normalization
model = Sequential([
        Dense(1, activation='linear', input_shape=(1,), kernel_initializer='glorot_uniform')
    ])

## Compile our model using the method of least squares (mse) loss function 
## and a stochastic gradient descent (sgd) optimizer
model.compile(loss='mse', optimizer='sgd') ## To try our model with an Adam optimizer simple replace 'sgd' with 'Adam'

## Set our learning rate to 0.01 and print it
model.optimizer.lr.set_value(.001)
print(model.optimizer.lr.get_value())

## Fit our model to the noisy data we create above. Notes: 
## The validation split parameter reserves 20% of our data for validation (ie 80% will be used for training)
## I don't really know if using a batch size of 1 makes sense
history = model.fit(x=df['x'], y=df['y'], validation_split=0.2, batch_size=1, epochs=100)

## ---------- Review our weights -------------------
## Save and print our final weights
predicted_m = model.get_weights()[0][0][0]
predicted_b = model.get_weights()[1][0]
print("\nm=%.2f b=%.2f\n" % (predicted_m, predicted_b))

## Create our predicted y's based on the model
df['y_predicted'] = df['x'].apply(lambda x: predicted_m*x + predicted_b)

## Plot the original data with a standard linear regression
ax1 = sns.regplot(x='x', y='y', data=df, label='real')

## Plot our predicted line based on our Keras model's slope and y-intercept
ax2 = sns.regplot(x='x', y='y_predicted', data=df, scatter=False, label='predicted')
ax2.legend(loc="upper left")