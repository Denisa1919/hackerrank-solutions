# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:35:18 2025

@author: recam
"""


import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def is_leap_julian(year):
    return year % 4 ==0
def is_leap_gregorian(year):
    return (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0)
def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        
        return f"26.09.{year}"
    elif year < 1918:
        if is_leap_julian(year):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
            
    else:
        if is_leap_gregorian(year):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()