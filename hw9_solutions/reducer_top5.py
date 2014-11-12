from operator import itemgetter
import sys

current_isbn = None
max_5_pair = [('',0),('',0),('',0),('',0),('',0)]
isbn = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    items = line.split('\t')
    isbn = items[1]
    try:
        int_count = int(items[2])
    except ValueError:
        continue

    count_l = [c for i,c in max_5_pair]
    if int_count > min(count_l):
        #new max found
        min_index = count_l.index(min(count_l))
        #print min_index, max_5_pair
        max_5_pair.remove(max_5_pair[min_index])
        max_5_pair.append((items[1],int_count))

for i,c in max_5_pair:
    print '%s\t%s' %(i,c)