# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 23:44:46 2025

@author: recam
"""

def findZigZagSequence(a, n):
    a.sort()
    mid = n // 2 
     # Middle index
    # Swap the middle and last element
    a[mid], a[n-1] = a[n-1], a[mid]

    # Reverse the second half after the middle
    st = mid + 1
    ed = n - 2  # because last element is already in middle
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1

    print(*a)  # print space-separated in one line
    return

test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)