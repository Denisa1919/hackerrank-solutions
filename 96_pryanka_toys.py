# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:32:08 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Write your code here
    
    w.sort()
    count = 0
    i = 0
    n = len(w)

    while i < n:
        count += 1
        limit = w[i] + 4  # max weight for current container
        i += 1
        while i < n and w[i] <= limit:
            i += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
