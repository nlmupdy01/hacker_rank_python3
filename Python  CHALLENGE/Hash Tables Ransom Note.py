#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dict = {}
    for word in magazine:
        dict[word] = dict.get(word,0) + 1
    for word in note:
        if dict.get(word,0) == 0:
            print('No')
            return
        else:
            dict[word] -= 1
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)