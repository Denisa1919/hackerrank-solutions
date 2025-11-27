# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:28:04 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    
    important = []
    total_luck = 0
    
    for luck, importance in contests:
        if importance == 1:
            important.append(luck)
        else:
            total_luck += luck
    
    # Sort important contests by luck descending
    important.sort(reverse=True)
    
    # Lose the top k important contests
    total_luck += sum(important[:k])
    
    # Win the rest
    total_luck -= sum(important[k:])
    
    return total_luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
