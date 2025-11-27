# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:01:47 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    if len(s) == 1:
        print("NO")
        return
        
    for i in range(1, len(s)//2 + 1):
        first = int(s[:i])
        seq = str(first)
        
        while len(seq) < len(s):
            first += 1
            seq += str(first)
        
        if seq == s:
            print("YES", s[:i])
            return
        
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
