#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    last_index = len(arr) -1
    left_to_right_diagonal_sum = 0
    right_to_left_diagonal_sum = 0
    i, j = 0, 0
    while (i <= last_index):
        left_to_right_diagonal_sum += arr[i][j]
        i+=1
        j+=1
        
    p,q = last_index, 0
    while (p >= 0):
        right_to_left_diagonal_sum += arr[p][q]
        p-=1
        q+=1
    
    return abs(left_to_right_diagonal_sum - right_to_left_diagonal_sum)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
