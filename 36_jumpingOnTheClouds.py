# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:17:54 2025

@author: recam
"""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    position = 0
    
    while True:
        position = (position + k) % n
        energy -= 1 + 2 * c[position]
        
        if position == 0:
            break
            
    return energy
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
