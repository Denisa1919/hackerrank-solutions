# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:30:41 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
  
    num_fives = n
    while num_fives >= 0:
        if num_fives % 3 == 0 and (n - num_fives) % 5 == 0:
            print('5' * num_fives + '3' * (n - num_fives))
            return
        num_fives -= 5
    print(-1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
