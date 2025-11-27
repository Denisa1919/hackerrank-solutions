# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:29:17 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    
    sticks.sort()
    
    # Check triplets from the end for largest perimeter
    for i in range(len(sticks)-3, -1, -1):
        a, b, c = sticks[i], sticks[i+1], sticks[i+2]
        if a + b > c:
            return [a, b, c]
    
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
