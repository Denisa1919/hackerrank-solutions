# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:21:22 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
   
    freq_arr = {}
    freq_brr = {}

   
    for x in arr:
        freq_arr[x] = freq_arr.get(x, 0) + 1

    
    for x in brr:
        freq_brr[x] = freq_brr.get(x, 0) + 1

    missing = []

    
    for num in freq_brr:
        if freq_brr[num] != freq_arr.get(num, 0):
            missing.append(num)

    return sorted(missing)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
