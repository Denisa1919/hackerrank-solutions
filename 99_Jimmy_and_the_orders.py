# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 00:36:26 2025

@author: recam
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    

    finish_times = [(i+1, orders[i][0] + orders[i][1])
     for i in range(len(orders))]
    
    # Sort by finish time, then by order number
    finish_times.sort(key=lambda x: (x[1], x[0]))
    
    # Return only the order numbers
    return [order[0] for order in finish_times]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
