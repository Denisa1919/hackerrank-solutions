# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:37:12 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    counts = {}
    for sock in ar:
        counts[sock] = counts.get(sock, 0) + 1
        
    pairs = 0
    for count in counts.values():
        pairs += count // 2
        
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
