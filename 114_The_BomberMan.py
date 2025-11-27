# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:59:53 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n == 1:
        return grid
    
    r, c = len(grid), len(grid[0])
    
    def explode(g):
        new_grid = [['O']*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if g[i][j] == 'O':
                    new_grid[i][j] = '.'
                    for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                        ni, nj = i+dx, j+dy
                        if 0 <= ni < r and 0 <= nj < c:
                            new_grid[ni][nj] = '.'
        return ["".join(row) for row in new_grid]
    
    if n % 2 == 0:
        return ['O'*c for _ in range(r)]
    elif n % 4 == 3:
        return explode(grid)
    else:  # n % 4 == 1
        return explode(explode(grid))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
