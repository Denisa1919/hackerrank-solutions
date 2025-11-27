# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 01:01:48 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    n, m = len(grid), len(grid[0])

    def possible_arm_lengths(i, j):
        length = 0
        while True:
            for dx, dy in [(-length,0),(length,0),(0,-length),(0,length)]:
                ni, nj = i+dx, j+dy
                if ni<0 or ni>=n or nj<0 or nj>=m or grid[ni][nj]!='G':
                    return length-1
            length += 1

    # generate all pluses: (center_i, center_j, arm_length, area)
    pluses = []
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='G':
                l = possible_arm_lengths(i,j)
                for arm in range(0,l+1):
                    area = 1 + 4*arm
                    pluses.append((i,j,arm,area))
    
    pluses.sort(key=lambda x: -x[3])  # largest area first
    max_product = 0

    def cells_of_plus(i,j,arm):
        cells = set()
        cells.add((i,j))
        for l in range(1,arm+1):
            cells.update([(i+l,j),(i-l,j),(i,j+l),(i,j-l)])
        return cells

    for idx1 in range(len(pluses)):
        i1,j1,arm1,area1 = pluses[idx1]
        cells1 = cells_of_plus(i1,j1,arm1)
        for idx2 in range(idx1+1,len(pluses)):
            i2,j2,arm2,area2 = pluses[idx2]
            cells2 = cells_of_plus(i2,j2,arm2)
            if cells1.isdisjoint(cells2):
                max_product = max(max_product, area1*area2)
                break  # next largest area2 can't be bigger
    return max_product

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
