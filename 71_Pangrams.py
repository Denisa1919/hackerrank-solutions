# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:00:13 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower().replace(" ", "")
    letters = set(s)
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
