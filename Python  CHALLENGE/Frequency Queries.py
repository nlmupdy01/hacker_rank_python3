#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    res = []
    fre = defaultdict(int)
    for x in queries:
        if x[0] == 1:
            fre[x[1]] += 1
        elif x[0] == 2:
            if x[1] in fre and fre[x[1]] > 0:
                fre[x[1]] -= 1
        else:
            res.append(1 if x[1] in set(fre.values()) else 0)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()