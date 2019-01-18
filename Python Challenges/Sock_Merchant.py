#Complete the sockMerchant function in the editor below. 
#It must return an integer representing the number of matching pairs of socks that are available.
#sockMerchant has the following parameter(s):
## n: the number of socks in the pile
## ar: the colors of each sock ( an array )

#!/bin/python3

import os

def occurrences(valuetofind,table):
    lentghoftable = len(table)
    count = 0
    for i in range(lentghoftable):
        if table[i]==valuetofind: count+=1
    return count

def exist(valuetofind,table):
    lentghoftable = len(table)
    exist = False
    for i in range(lentghoftable):
        if table[i]==valuetofind: exist = True
    return exist

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    alreadyseencases = []
    occurence_tab = []
    for i in range(n):
        if i==0 : 
            alreadyseencases.append(ar[i])
            occurence_tab.append(occurrences(ar[i],ar))
        else:
            if(not exist(ar[i],alreadyseencases)):
                alreadyseencases.append(ar[i])
                occurence_tab.append(occurrences(ar[i],ar))
    result = 0 
    print(occurence_tab)
    for k in range(len(occurence_tab)):
        result = result+occurence_tab[k] if occurence_tab[k]%2==0 else result+occurence_tab[k]-1
    return result//2 #Divide by two to get the number of pairs


     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
