#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(arr):
    # Write your code here
    if not arr:
        return 0

    max_count = arr.count(max(arr))
    return len(str(max(arr))) * max_count

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)

# def max_number_length_with_repeats(arr):
#     if not arr:
#         return 0
#
#     max_count = arr.count(max(arr))
#     return len(str(max(arr))) * max_count
#
# # Example usage:
# numbers = [3, 3, 2, 1]
# result = max_number_length_with_repeats(numbers)
# print(result)
