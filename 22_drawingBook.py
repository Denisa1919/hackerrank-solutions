# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:38:34 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    turns_from_front = p // 2
    turns_from_back = (n // 2) -(p // 2)
    
    return min(turns_from_front, turns_from_back)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
