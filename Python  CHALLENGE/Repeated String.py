#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

k = s.count("a")*(n/len(s))
k += s[:n%len(s)].count("a")
print k