#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    # Write your code here
    for i in range(n):
        for j in range(i+1):
            print("#",end="")
        print()
        # for j in range(n-1):
        #     print("#")
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
