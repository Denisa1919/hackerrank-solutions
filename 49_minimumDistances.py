# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:43:48 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    seen = {}
    min_dist = float('inf')
    
    for i, val in enumerate(a):
        if val in seen:
            min_dist = min(min_dist, i - seen[val])
        seen[val] = i
    return min_dist if min_dist != float('inf') else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
