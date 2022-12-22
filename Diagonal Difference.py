import math
import os
import random
import re
import sys

def countingSort(arr):
    l=max(arr)
    ar=[0]*100
    for i in arr:
        ar[i]+=1
    return ar

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()