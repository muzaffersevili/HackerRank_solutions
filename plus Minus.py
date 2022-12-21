#!/bin/python3
import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos, zero, neg = 0, 0, 0
    l = len(arr)
    for i in range(l):
        if (arr[i] < 0):
            neg = neg + 1
        elif (arr[i] == 0):
            zero = zero + 1
        else:
            pos = pos + 1

    print(pos / l)
    print(neg / l)
    print(zero / l)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
