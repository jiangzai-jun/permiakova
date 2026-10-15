#!/usr/bin/python3
import sys
lines = [] 
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

for line in sorted (lines):
    print(line)

for line in sorted (lines, reverse=True):
    print(line)
