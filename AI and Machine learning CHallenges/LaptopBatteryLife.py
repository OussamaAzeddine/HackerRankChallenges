#!/bin/python3
import numpy as np
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
  #Read Data over our file, 
  myfile = open('trainingdata.txt','r')
  mylines = myfile.readlines()
  X=np.empty(0)
  Y=np.empty(0)

  for n_lines in range(len(mylines)):
    row_data=[]
    row_data = mylines[n_lines].split(',')
    X = np.append(X,float(row_data[0]))
    Y = np.append(Y,float(row_data[1]))
  Y = Y[X<4] #the case where X >4 are useless since it will always output 8.00h of charge 
  X = X[X<4] #To figure out this we need to visualize data (not done here)
  # we can also get same result by determining mathematically m & b of the equation y = m*x +b
  # but personnaly I prefer to use sklearn
  model = LinearRegression(fit_intercept=False)
  model = model.fit(X.reshape(-1, 1),Y) #our dataset contains one feature we need ro reshape our array for our linearRegression model
  timeCharged = float(input())
  arraydata = np.array(timeCharged)
  prediction = model.predict(arraydata.reshape(1,-1))
  #print results
  if(timeCharged>4) : print("8.00")
  else : print(str(round(prediction[0],2)))
  
  #Once you see that your data output same result starting a specific treshold this exercice become easy, 
  #in our case => ~ 4  
