import sys

max_5 = [('',0),('',0),('',0),('',0),('',0)]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    #print line
    words = line.split("\t")
    count_max = [c for w,c in max_5]
    if int(words[1]) > min(count_max):
        min_index = count_max.index(min(count_max))
        max_5.remove(max_5[min_index])
        max_5.append((words[0],words[1]))

for mem in max_5:
    print "%d\t%s\t%s" % (1,mem[0],mem[1])