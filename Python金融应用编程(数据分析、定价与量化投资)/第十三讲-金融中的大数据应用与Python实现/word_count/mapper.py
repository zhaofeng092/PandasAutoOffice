#!/usr/bin/python

import sys

for line in sys.stdin:
    for word in line.strip().split():
        print "%s\t%d" % (word,1)
