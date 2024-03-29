# -*- coding: utf-8 -*-
"""logisticregression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dstbh9Mn7URbrAyIebnsSx0YwYz0U27e
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class logistic_regression():
  #declaring learning rate and no of iterations(hyperparameters)
  def __init__(self, learning_rate, no_of_iterations):
    self.learning_rate= learning_rate
    self.no_of_iterations=no_of_iterations

  #fir function is for training model with dataset
  def fit(self,x,y):
    self.m, self.n=x.shape

    #initiate weight and bias value
    self.w=np.zeros(self.n)
    self.b=0
    self.x=x
    self.y=y

    #implemeting gradient descent
    for i in range(self.no_of_iterations):
      self.update_weights()

  def update_weights(self):
    y_cap=1/(1+np.exp(-(self.x.dot(self.w)+self.b)))

    #derivatives
    dw=(1/self.m)*np.dot(self.x.T, (y_cap-self.y))
    db=(1/self.m)*np.sum(y_cap-self.y)

    #updating weights nd bias
    self.w=self.w-(self.learning_rate*dw)
    self.b=self.b-(self.learning_rate*db)



  #sigmoid equation and decision boundary
  def predict(self,x):
    y_predict=1/(1+np.exp(-(x.dot(self.w)+self.b)))
    y_predict=np.where(y_predict>0.5,1,0)
    return y_predict

ds=pd.read_csv('/content/diabetes.csv')

ds.head()

ds.shape

ds['Outcome'].value_counts()

ds.groupby('Outcome').mean()

features= ds.drop(columns='Outcome', axis=1)
target=ds['Outcome']

scaler=StandardScaler()

scaler.fit(features)

std_data=scaler.transform(features)

print(std_data)

features=std_data
target=ds['Outcome']

x_train, x_test, y_train, y_test= train_test_split(features,target, test_size=0.2,random_state=3)

x_test.shape

model=logistic_regression(learning_rate=0.1, no_of_iterations=1000)

model.fit(x_train, y_train)

model.predict(x_test)

prediction=model.predict(x_train)
accuracy=accuracy_score(y_train, prediction)

print(accuracy)

pred=model.predict(x_test)
acc=accuracy_score(y_test, pred)

print(acc)



