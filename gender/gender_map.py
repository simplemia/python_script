#!/usr/bin/env python

import sys

for line in sys.stdin:
    if len(line) >8:
        (pyid, cata, weight) = line.strip().split('\t')
        print "%s\t%s\t%s" % (pyid, cata, weight)

