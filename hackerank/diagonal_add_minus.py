#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDiffe
#
# rence' function below.
#


# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    diagonal_1 = [arr[i][i] for i in range(n)]
    diagonal_2 = [arr[i][n-1-i] for i in range(n)]
    a = sum(diagonal_1)
    b = sum(diagonal_2)
    return abs(a-b)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
