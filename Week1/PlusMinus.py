#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    size_of_arr = len(arr)
    zero_numbers = 0
    pos_numbers = 0
    neg_numbers = 0
    
    if size_of_arr == 0:
        return
    
    for x in arr:
        if x == 0:
            zero_numbers += 1
        elif x > 0:
            pos_numbers += 1
        else: # x<0
            neg_numbers += 1
    
    pos_ratios = pos_numbers/size_of_arr
    neg_ratios = neg_numbers/size_of_arr
    zero_ratios = zero_numbers/size_of_arr
    
    print("{:.6f}".format(pos_ratios))
    print("{:.6f}".format(neg_ratios))
    print("{:.6f}".format(zero_ratios))
    
    return None

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(arr)