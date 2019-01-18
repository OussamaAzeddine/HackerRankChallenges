# Enter your code here. Read input from STDIN. Print output to STDOUT
#import necessary libraries
import numpy as np

#get inputs
features, n_rows = map(int, input().split())
X = []
Y = []

for i_rows in range(n_rows):
  x_temp = []
  inputs = list(map(float,input().split()))
  for i_features in range(features):
    x_temp.append(inputs[i_features])
  X.append(x_temp)
  Y.append(inputs[features])
val = n_rows - 1 
n_test = int(input())
X_test = []
for i_test in range(n_test):
  x=[]
  elements = list(map(float, input().split()))
  for k_test in range(len(elements)):
    x.append(elements[k_test])
  X_test.append(x)

# Start the real work : 
# This is a polynomial regression, let's use some of Scikit-learn funGame
#src : https://scikit-learn.org/stable/modules/linear_model.html#polynomial-regression-extending-linear-models-with-basis-functions 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

model = Pipeline([('poly', PolynomialFeatures(degree=3)),('linear', LinearRegression(fit_intercept=False))])
model = model.fit(X,Y)
prediction = model.predict(X_test)

#Show our results : 
for i in range(len(prediction)): print(round(prediction[i],2))
