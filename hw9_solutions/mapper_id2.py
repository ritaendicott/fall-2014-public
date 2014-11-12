import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    count1 = int(items[1])
    count2 = int(items[2])
    # We do not care about the number of occurences,
    # We just need to know if an ID occurred in test/train.
    # So, we will reduce any non-zero value to 1.
    if count1:
    	count1 = 1
    if count2:
    	count2 = 1
    # Note that a 1 is added as a dummy key to force all lines to one reducer.
    # The output is of the format 
    # 1 <TAB> 0,1   for an ID that occurs in test file alone
    # 1 <TAB> 1,0   for an ID that occurs in training file alone
    # 1 <TAB> 1,1   for an ID that occurs in both files.
    print '1\t%s,%s' %(count1, count2)
