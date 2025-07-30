# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 21:44:55 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    period = s[-2:]
    hour = int(s[:2])
    
    if period == 'AM':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
            
    return f"{hour:02}:{s[3:5]}:{s[6:8]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
