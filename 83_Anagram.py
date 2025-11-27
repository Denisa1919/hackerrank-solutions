# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:14:57 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
        
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    from collections import Counter
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    changes = 0
    for ch in c1:
        if c1[ch] > c2.get(ch, 0):
            changes += c1[ch] - c2.get(ch, 0)
            
    return changes
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
