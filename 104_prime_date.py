# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 23:41:53 2025

@author: recam
"""

import re

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return [0, 31,28,31,30,31,30,31,31,30,31,30,31][month]

def find_prime_dates(d1, m1, y1, d2, m2, y2):
    result = 0

    while True:
        x = d1 * 100 + m1
        x = x * 1000 + y1
        if x % 4 == 0 and x % 7 == 0:
            result += 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        d1 += 1
        if d1 > days_in_month(m1, y1):
            d1 = 1
            m1 += 1
            if m1 > 12:
                m1 = 1
                y1 += 1
    return result

line = input()
date = list(map(int, re.split('-| ', line)))

d1, m1, y1, d2, m2, y2 = date
print(find_prime_dates(d1, m1, y1, d2, m2, y2))
