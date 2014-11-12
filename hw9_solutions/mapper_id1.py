import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
   	items = line.split('\t')
    # By default the number of unique query ids are printed.
    id_val = items[8]
    # When the mapper is executed as python mapper_id1.py user < train_test.txt
    if sys.argv[1] == 'user':
    	id_val = items[12]
    #output id + 1,0 for training instances
    if items[0] == 'train':
        print '%s\t%d\t%d' % (items[8],1,0)
    # output id + 0,1 for test instances
    else:
    	print '%s\t%d\t%d' % (items[8],0,1)