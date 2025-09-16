# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:09:14 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared = 5
    cumulative_likes = 0
    
    for day in range(n):
        likes = shared // 2
        cumulative_likes += likes
        shared = likes * 3
        
    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
