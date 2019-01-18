#!/bin/python3
#Tn = n² - (n-1)²
#Sn = T1 + T2 + T3 + .... + Tn
# given n solve Sn mod 10^9+7


import os
import sys

#
# Complete the summingSeries function below.
#
def summingSeries(n):
    result = 0
    if(n>=1 and n<=10**16):
        result = n*n
    return result%(10**9 +7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
