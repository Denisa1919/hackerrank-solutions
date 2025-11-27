# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:17:41 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    from collections import Counter
    
    freq = Counter(s)
    
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    
    if odd_count > 1:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
