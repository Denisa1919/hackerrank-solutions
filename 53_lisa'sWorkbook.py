# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:51:03 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    page = 1
    special_count = 0
    
    for problems in arr:
        for start in range(1, problems + 1, k):
            end = min(start + k - 1, problems)
            if start <= page <= end:
                special_count += 1
            page +=1
            
    return special_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
