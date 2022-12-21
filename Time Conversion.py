import math
import os
import random
import re
import sys


def timeConversion(s):
    if (int(s[:2]) < 12):
        if (s[-2:] == "PM"):
            s = str(int(s[:2]) + 12) + s[2:-2]
        else:
            s = s[0:-2]
    elif (int(s[:2]) == 12):
        if (s[-2:] == "PM"):
            s = s[0:-2]
        elif (s[-2:] == "AM"):
            s = str(int(s[:2]) - 12) + s[2:-2]

    if (s[1] == ":"):
        s = "0" + s

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()