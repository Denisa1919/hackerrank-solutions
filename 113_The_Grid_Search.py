# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:58:02 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
    R, C = len(G), len(G[0])
    r, c = len(P), len(P[0])

    for i in range(R - r + 1):
        for j in range(C - c + 1):
            # Check if top-left corner matches first row of P
            if G[i][j:j+c] == P[0]:
                match = True
                for k in range(1, r):
                    if G[i+k][j:j+c] != P[k]:
                        match = False
                        break
                if match:
                    return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
