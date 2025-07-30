# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:32:35 2025

@author: recam
"""

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    counts = Counter(arr)
    if not counts:
        return None
        
    max_frequency =0
    for bird_id, frequency in counts.items():
        if frequency >max_frequency:
            max_frequency = frequency
            
    result_bird_id = float('inf')
            
    for bird_id, frequency in counts.items():
        if frequency == max_frequency:
            if bird_id < result_bird_id:
                result_bird_id = bird_id
    return result_bird_id
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
