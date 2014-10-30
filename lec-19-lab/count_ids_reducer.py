#!/usr/bin/env python

from operator import itemgetter
import sys

current_id_type = None
id_type = None
id_set = set()

for line in sys.stdin:
    line = line.strip()
    id_type, this_id = line.split('\t')

    if current_id_type == id_type:
        id_set.add(this_id)
    else:
        if current_id_type:
            print '%s\t%s' % (current_id_type, len(id_set))
        id_set = set()
        id_set.add(this_id)
        current_id_type = id_type
        

# do not forget to output the last word if needed!
if current_id_type == id_type:
    print '%s\t%s' % (current_id_type, len(id_set))
