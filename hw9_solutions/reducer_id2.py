from operator import itemgetter
import sys

current_key = None
current_count = 0
idnum = None
key = 0
out = dict()

for line in sys.stdin:
	line = line.strip()
	words  = line.split('\t')
	key = words[1]
	# Here we count the number of lines that have "0,1", "1,0" and "1,1"
	if current_key == key:
		current_count += 1
	else:
		if current_key:
			out[current_key] = out.get(current_key,0) + current_count

		current_key = key
		current_count = 1

if current_key:
	out[current_key] = out.get(current_key,0) + current_count

# Final output
print "Number of unique Ids in test data:", out['0,1']
print "Number of unique Ids in training data:", out['1,0']
print "Percentage of new Ids:", round((out['0,1'] - out['1,1'])/float(out['0,1']), 5)
