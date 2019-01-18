# Problem Statement
#On the eve of Diwali, Hari is decorating his house with a serial light bulb set. 
#The serial light bulb set has N bulbs placed sequentially on a string 
#which is programmed to change patterns every second.
#If at least one bulb in the set is on at any given instant of time,
#how many different patterns of light can the serial light bulb set produce?

#Note: Lighting two bulbs *-* is different from **-

#!/bin/python3

import os
import sys

#
# Complete the lights function below.
#
def lights(n):
    result =0
    if(0<n and n<10**4):
        result = 2**n - 1 
    return result%10**5

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
