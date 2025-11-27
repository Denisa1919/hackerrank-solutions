# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:56:48 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", 
               "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
               "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
               "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
               "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    
    if m == 0:
        return f"{numbers[h]} o' clock"
    elif m == 15:
        return f"quarter past {numbers[h]}"
    elif m == 30:
        return f"half past {numbers[h]}"
    elif m == 45:
        next_hour = numbers[h % 12 + 1]
        return f"quarter to {next_hour}"
    elif m < 30:
        minute_word = "minute" if m == 1 else "minutes"
        return f"{numbers[m]} {minute_word} past {numbers[h]}"
    else:
        next_hour = numbers[h % 12 + 1]
        minutes_to = 60 - m
        minute_word = "minute" if minutes_to == 1 else "minutes"
        return f"{numbers[minutes_to]} {minute_word} to {next_hour}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
