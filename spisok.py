#!/usr/bin/python
import sys

a = []

for line in sys.stdin:
    a.append(line)

a.sort(reverse=True)
print(a)
