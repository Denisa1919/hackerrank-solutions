# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:31:05 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    count_in_s = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    
    return count_in_s * full_repeats + s[:remainder].count('a')
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
