# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 23:55:38 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    expected = "SOS"
    count = 0
    
    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
