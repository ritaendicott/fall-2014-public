from operator import itemgetter
import sys
# This reducer counts the number of occurences of an ID in the training and test instances.
current_id = None
current_c1 = 0
current_c2 = 0
idnum = None
c1 = 0
c2 = 0
for line in sys.stdin:
	line = line.strip()
	words  = line.split('\t')
	idnum = words[0]
	c1 = words[1]
	c2 = words[2]
	# c1 is 1 when the ID is in a training instance
	# c2 is 1 when the ID is in a test instance
	if current_id == idnum:
		current_c1 += int(c1)
		current_c2 += int(c2)
	else:
		if current_id:
			print '%s\t%d\t%d' %(current_id, current_c1, current_c2)

		current_id = idnum
		current_c1 = int(c1)
		current_c2 = int(c2)

if current_id:
	print '%s\t%d\t%d' %(current_id, current_c1, current_c2)