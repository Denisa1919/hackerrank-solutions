# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:11:53 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    pos = {}
    for i, val in enumerate(p, start=1):
        pos[val] = i
        
    result = []
    for x in range(1, len(p) + 1):
        
        y= pos[pos[x]]
        result.append(y)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
