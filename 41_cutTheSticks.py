# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:29:47 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    arr.sort()
    result = []
    n = len(arr)
    
    for i in range(n):
        
        if i == 0 or arr[i] != arr[i -1]:
            result.append(n - i)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
