# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:16:16 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    from collections import Counter
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    deletions = 0
    
    all_chars = set(c1.keys()).union(set(c2.keys()))
    
    for ch in all_chars:
        deletions += abs(c1.get(ch, 0) - c2.get(ch, 0))
        
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
