#!/usr/bin/env python

# Running this mapper with the identity reducer
# -reducer org.apache.hadoop.mapred.lib.IdentityReducer

import random
import sys

bucket = ""
for line in sys.stdin:
    line = line.strip()
    prob = random.random()
    if prob < 0.6:
        bucket = "train"
    elif prob >= 0.6 and prob < 0.8:
        bucket = "validation"
    else:
        bucket = "test"
    print '%s\t%s\t%s' % (str(round(prob, 4)), bucket, line)
