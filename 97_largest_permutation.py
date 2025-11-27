# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:33:35 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    n = len(arr)
    pos = {val: i for i, val in enumerate(arr)}

    for i in range(n):
        if k == 0:
            break

        desired = n - i
        if arr[i] == desired:
            continue

        # Swap current element with the desired one
        idx_to_swap = pos[desired]
        arr[i], arr[idx_to_swap] = arr[idx_to_swap], arr[i]

        # Update positions
        pos[arr[idx_to_swap]] = idx_to_swap
        pos[arr[i]] = i

        k -= 1

    return arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
