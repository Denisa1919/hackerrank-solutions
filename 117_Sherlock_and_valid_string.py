# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 01:05:11 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    freq = Counter(s)
    freq_count = Counter(freq.values())
    
    if len(freq_count) == 1:
        return "YES"
    elif len(freq_count) == 2:
        key1, key2 = freq_count.keys()
        val1, val2 = freq_count[key1], freq_count[key2]
        
        if (key1 == 1 and val1 == 1) or (key2 == 1 and val2 == 1):
            return "YES"
        elif (abs(key1 - key2) == 1) and ((key1 > key2 and val1 == 1) or (key2 > key1 and val2 == 1)):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
