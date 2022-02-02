#!/bin/python3

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    if len(arr) != 5:
        return
    '''
    sorted_arr = sorted(arr)
    min_sum = sum(sorted_arr[:4])
    max_sum = sum(sorted_arr[1:])
    '''
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(f'{min_sum} {max_sum}')
        
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
