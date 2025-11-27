# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 23:50:09 2025

@author: recam
"""

#!/bin/python3
def insertionSort1(n, arr):
    value = arr[-1]
    i = n -2
    
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
        
    arr[i + 1] = value
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
