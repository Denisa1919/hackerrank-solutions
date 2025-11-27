# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:43:43 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    if n == 0:
        return 1  # Only x = 0
    count_zero_bits = bin(n)[2:].count('0')
    return 2 ** count_zero_bits

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
