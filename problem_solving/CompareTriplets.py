#!/bin/python3

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    score = [0, 0]
    for i in range(3):
        if a[i] == b[i]:
            pass
        elif a[i] > b[i]:
            score[0] += 1
        else:
            score[1] += 1
            
    return score

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    
    print(result)
