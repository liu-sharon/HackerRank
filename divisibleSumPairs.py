#Sharon Liu (2018)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    sum = 0
    count=0
    for i in ar:
        temp=count+1
        while temp < n:
            if(i+ar[temp])%k == 0:
                sum += 1
            temp += 1
        count+=1
                
    return sum
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
