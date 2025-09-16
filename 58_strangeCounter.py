# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:57:00 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    cycle_length = 3
    start_time = 1
    
    while t > start_time + cycle_length - 1:
        start_time += cycle_length
        cycle_length *= 2
        
    return cycle_length - (t - start_time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
