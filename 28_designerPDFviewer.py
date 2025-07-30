# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 14:46:25 2025

@author: recam
"""

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    max_height_in_word = 0
    
    for char in word:
        
        char_index = ord(char) - ord('a')
        current_char_height = h[char_index]
        
        max_height_in_word =max(max_height_in_word, current_char_height)
        
        word_lenght =len(word)
        highlighted_area = max_height_in_word * word_lenght
        
    return highlighted_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
