# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:45:49 2025

@author: recam
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
def gameOfStones(n):
    if n % 7 in [0, 1]:
        return "Second"
    else:
        return "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
