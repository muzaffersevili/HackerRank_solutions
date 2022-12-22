import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    k = k % 26
    for i in range(len(s)):
        char = ord(s[i])
        if (char > 64 and char < 91):
            new_asc = char + k
            if (new_asc > 90):
                new_asc -= 26
            new_chr = chr(new_asc)
            s = s[:i] + new_chr + s[i + 1:]
        elif (char > 96 and char < 123):
            new_asc = char + k
            if (new_asc > 122):
                new_asc -= 26
            new_chr = chr(new_asc)
            s = s[:i] + new_chr + s[i + 1:]

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()