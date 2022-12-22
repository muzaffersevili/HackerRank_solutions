import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    prim = 0
    sec = 0
    for i in range(len(arr[0])):
        prim = prim + arr[i][i]
        sec = sec + arr[i][len(arr[0]) - 1 - i]

    return abs(prim - sec)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()