# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:13:40 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    def is_palindrome(st):
        return st == st[::-1]
        
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            
            if is_palindrome(s[i+1: j +1]):
                return i
            elif is_palindrome(s[i:j]):
                return j
            else:
                return -1
        i += 1
        j -= 1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
