# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:32:30 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    from collections import Counter
    
    freq = Counter(arr)
    max_freq = max(freq.values())
    return len(arr) - max_freq
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
