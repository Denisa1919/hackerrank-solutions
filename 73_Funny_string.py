# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:03:08 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    ord_s = [ord(c) for c in s]
    
    ord_r = ord_s[::-1]
    
    
    for i in range(1, len(s)):
        if abs(ord_s[i] - ord_s[i-1]) != abs(ord_r[i] - ord_r[i-1]):
            return "Not Funny"
            
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
