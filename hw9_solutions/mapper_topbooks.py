import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    #print line
    line = line.replace('"', '').strip()
    if isinstance(line,unicode):
    	continue
    words = line.split(";")
    if len(words) == 3:
    	print '%s\t%s' % (words[1], 1)