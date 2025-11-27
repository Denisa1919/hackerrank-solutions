# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 01:04:21 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    n = len(arr)
    # Prepare 100 buckets for numbers 0-99
    buckets = [[] for _ in range(100)]
    
    for i, (num, string) in enumerate(arr):
        num = int(num)
        # Replace string with '-' if in first half
        if i < n//2:
            string = '-'
        buckets[num].append(string)
    
    # Flatten the buckets
    output = []
    for bucket in buckets:
        output.extend(bucket)
    
    print(" ".join(output))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
