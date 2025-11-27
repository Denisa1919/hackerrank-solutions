# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 23:38:29 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    total = sum(int(d) for d in n) * k

    # Recursive helper function
    def digitSum(x):
        if x < 10:
            return x
        return digitSum(sum(int(d) for d in str(x)))

    return digitSum(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
