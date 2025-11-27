# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:55:31 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(" ", "")
    L = len(s)
    
    # Compute grid dimensions
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    
    if rows * cols < L:
        rows += 1
    
    # Build encrypted message
    encrypted = []
    for c in range(cols):
        word = ''
        for r in range(rows):
            index = r * cols + c
            if index < L:
                word += s[index]
        encrypted.append(word)
    
    return ' '.join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
