# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:26:40 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    sorted_rows = [''.join(sorted(row)) for row in grid]
    
    n = len(sorted_rows)
    m = len(sorted_rows[0])
    
    # Check columns
    for col in range(m):
        for row in range(1, n):
            if sorted_rows[row][col] < sorted_rows[row-1][col]:
                return "NO"
                
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
