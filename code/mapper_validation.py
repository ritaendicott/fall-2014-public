#!/usr/bin/env python

# Running this mapper with the identity reducer
# -reducer org.apache.hadoop.mapred.lib.IdentityReducer

import sys

bucket = ""
for line in sys.stdin:
    line = line.strip()
    lines = line.split("\t")
    if lines[1] == "validation":
        print line
