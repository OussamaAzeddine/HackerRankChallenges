# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
import numpy as np

def func_median(N,tab):
  tab = np.sort(tab)
  if(N%2 == 1):
    return tab[N//2]
  else:
    return round((tab[N//2]+tab[(N//2)-1])/2,1)

def func_mean(N,tab):
  count = 0
  for i in range(N):
    count += tab[i]
  return round(count/N,1)

def func_mode(N,tab):
  #get max occurences
  occ =0
  #find number of max occurences
  for k in range(N):
    if(occ<tab.count(tab[k])):
      occ = tab.count(tab[k])
  #find the minimum with max_occurences
  mode = max(tab)
  for k in range(N):
    if(occ == tab.count(tab[k])):
      if(tab[k]< mode): mode = tab[k]
  return mode

def fun_sd(N,tab):
  square_sum = 0
  mean = func_mean(N,tab)
  for k in range(N):
    square_sum += (tab[k]-mean)**2
  return round(sqrt(square_sum/N),1)

def fun_cdint(N,tab):
  mean = func_mean(N,tab)
  stand = fun_sd(N,tab)
  upper_bound = round(mean + (stand*1.96/sqrt(N)),1) # the formula is mean +/- (standard_deviation*z-value/sqrt(numberofSamples)) where Z-value is the equivalent of 95% for confidence interval
  lower_bound = round(mean - (stand*1.96/sqrt(N)),1)
  return str(lower_bound)+' '+str(upper_bound)


if __name__ == '__main__':
  #read Data
  N = int(input())
  tab_entry = list(map(int,input().split()))
  print(func_mean(N,tab_entry))
  print(func_median(N,tab_entry))
  print(func_mode(N,tab_entry))
  print(fun_sd(N,tab_entry))
  print(fun_cdint(N,tab_entry))
