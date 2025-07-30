# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:45:49 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    max_hurdle_height = max(height)
    
    if max_hurdle_height > k:
        potions_needed = max_hurdle_height - k
        
    else:
        potions_needed = 0
        
    return potions_needed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
