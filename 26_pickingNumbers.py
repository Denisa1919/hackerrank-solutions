# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:44:29 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    
    counts =[0] * 101
    
    for num in a:
        counts[num] += 1
        
    max_length = 0
    
    for i in range(100):
        
        current_length = counts[i] + counts[i+1]
        
        max_length = max(max_length, current_length)
        
    return max_length
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
