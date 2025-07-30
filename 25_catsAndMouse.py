# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:43:04 2025

@author: recam
"""

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distance_catA_to_mouseC = abs(x - z)
    
    distance_catB_to_mouseC = abs(y - z)
    
    if distance_catA_to_mouseC < distance_catB_to_mouseC:
        
        return "Cat A"
    
    elif distance_catB_to_mouseC < distance_catA_to_mouseC:
        return "Cat B"
        
    else:
        return "Mouse C"
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
