#!/usr/bin/env python

from operator import itemgetter
import sys

current_ad_id = None
ad_id = None
clicks = 0
impressions = 0

for line in sys.stdin:
    line = line.strip()
    ad_id, click, impr = line.split('\t')

    if current_ad_id == ad_id:
        clicks += int(click)
        impressions += int(impr)
    else:
        if current_ad_id:
            #ctr = float(int(clicks))/ (float(int(impressions)) + 0.001)
            print '%s\t%s\t%s' % (current_ad_id, clicks, impressions)
        clicks = int(click)
        impressions = int(impr)
        current_ad_id = ad_id
        

# do not forget to output the last word if needed!
if current_ad_id == ad_id:
    #ctr = float(int(clicks))/ (float(int(impressions)) + 0.001)
    print '%s\t%s\t%s' % (current_ad_id, clicks, impressions)
