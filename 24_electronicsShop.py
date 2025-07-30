# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:41:18 2025

@author: recam
"""

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    max_spent = -1
    
    for keyboard_price in keyboards:
        
        for drive_price in drives:
            current_sum = keyboard_price + drive_price
            
            if current_sum <= b:
                max_spent = max(max_spent, current_sum)
                
    return max_spent
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
