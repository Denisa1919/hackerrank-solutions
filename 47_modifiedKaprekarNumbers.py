# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:39:39 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    kaprekars = []
    
    for n in range(p, q + 1):
        sq = str(n * n)
        d = len(str(n))
        
        right = int(sq[-d:]) if d <= len(sq) else int(sq)
        left = int(sq[:-d]) if sq[:-d] else 0
        
        if left + right == n:
            kaprekars.append(n)
            
    if kaprekars:
        print(" ".join(map(str, kaprekars)))
        
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
