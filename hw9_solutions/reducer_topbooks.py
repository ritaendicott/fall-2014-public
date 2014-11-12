from operator import itemgetter
import sys

current_isbn = None
current_count = 0
isbn = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    items = line.split('\t')
    isbn = items[0]
    
    if current_isbn == isbn:
        current_count += 1
    else:
        if current_isbn:
            print '%s\t%d' % (current_isbn, current_count)
        current_isbn = isbn
        current_count = 1

# do not forget to output the last word if needed!
if current_isbn == isbn:
    print '%s\t%d' % (current_isbn, current_count)