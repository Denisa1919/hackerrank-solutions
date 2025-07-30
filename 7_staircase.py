# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 21:41:19 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
   for i in range(1, n + 1):
     spaces = ' ' * (n - i)
     hashes = '#' * i
     print(spaces + hashes)
     
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
