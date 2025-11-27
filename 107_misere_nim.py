# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:49:00 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Write your code here
    if all(pile == 1 for pile in s):
        return "Second" if len(s) % 2 != 0 else "First"
    
    xor_sum = 0
    for pile in s:
        xor_sum ^= pile

    return "Second" if xor_sum == 0 else "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
