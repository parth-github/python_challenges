#!/bin/python3


from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    str_datetime = datetime.strptime(s, '%H:%M:%S%p')
    return(f'{str_datetime.hour}:{str_datetime.minute}:{str_datetime.second}')

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    
    print(result)