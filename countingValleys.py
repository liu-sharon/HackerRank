#Sharon Liu (2018)
#Given Gary's sequence of up and down steps during his last hike, find and print 
#the number of valleys he walked through.
#!/bin/python3


import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    amount=0
    for i in s:
        temp=level
        if i == "U":
            level+=1
        if i == "D":
            level-=1
        if level >= 0 and temp < 0:
            amount+=1
    return amount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()