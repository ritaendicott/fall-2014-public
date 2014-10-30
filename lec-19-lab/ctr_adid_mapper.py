#!/usr/bin/env python


import sys


FIELDS = ["click", "impression", "display_url", "ad_id", "advertiser_id",\
          "depth", "position", "query_id", "keyword_id", "title_id",\
          "description_id", "user_id"]

def parse_line(line):
    line = line.strip()
    fields = line.split('\t')
    field_dic = {}
    for i in range(0, len(FIELDS)):
        field_dic[FIELDS[i]] = fields[i]
    return field_dic

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    print '%s\t%s\t%s' % (fields[3], fields[0], fields[1])
