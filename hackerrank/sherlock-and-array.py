#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    n = len(arr)
    acum = [0] * (n+2) 
    for i in range(1,n+1):
        acum[i] = acum[i-1] + arr[i-1]
    acum[n+1] = acum[n]

    for i in range(1,n+1):
        if acum[i-1] == (acum[n+1]-acum[i]):
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

