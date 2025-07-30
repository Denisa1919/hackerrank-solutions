# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:36:20 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    total_bill = sum(bill)
    
    cost_anna_ate = total_bill - bill[k]
    
    anna_should_pay = cost_anna_ate // 2
    
    if b == anna_should_pay:
        print("Bon Appetit")
    else:
        print(b - anna_should_pay)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
