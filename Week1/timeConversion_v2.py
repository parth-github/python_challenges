#!/bin/python3

import math
import os
import random
import re
import sys
'''
12:01:00PM -> 12:01:00
01:01:00PM -> 13:01:00
11:59:59PM -> 23:59:59

12:01:00AM -> 00:01:00
01:01:00AM -> 01:01:00
11:59:59AM -> 11:59:59
'''



def timeConversion(s):
    # Write your code here
    new_time = ''
    new_hour = 0
    if s[-2] == 'P'and s[0:2]!='12':
        new_hour = int(s[0:2]) +12
        new_time = str(new_hour) + s[2:-2]
        print (new_hour, new_time)
        
    elif s[-2] == 'A' and s[0:2]=='12':
        new_time = '00' + s[2:-2]
    
    else:
        new_time = s[:-2]
    
    return(new_time)


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    
    print(result)