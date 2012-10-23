#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    if len(line) >3:
        #print line.strip().split('\t')
        (pyid, cata, weight) = line.strip().split('\t')
        w = float(weight)
        if int(w) <1000 and re.search("[0-9]{5}",cata) and len(pyid) > 9 and re.search("([a-zA-Z0-9_~])",pyid):
            print "%s\t%s\t%s" % (pyid, cata, weight)

