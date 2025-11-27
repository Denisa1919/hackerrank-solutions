# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 23:54:35 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    result = ''
    k = k % 26
    
    for char in s:
        if char.islower():
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            
        elif char.isupper():
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            
        else:
            result += char
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
