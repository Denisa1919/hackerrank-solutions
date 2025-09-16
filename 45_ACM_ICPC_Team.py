# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:36:16 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    
    n = len(topic)
    max_topics = 0
    team_count = 0
    
    for i in range(n):
        for j in range(i + 1, n ):
            combined = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            
            if combined > max_topics:
                max_topics = combined
                team_count = 1
            elif combined == max_topics:
                team_count += 1
                
    return [max_topics, team_count]   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
