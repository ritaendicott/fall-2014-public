# Hadoop streaming
Hadoop streaming is a utility that comes with the Hadoop distribution. The utility allows you to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer. The mapper and the reducer are executables that read the input from stdin (line by line) and emit the output to stdout. The utility will create a Map/Reduce job, submit the job to an appropriate cluster, and monitor the progress of the job until it completes. (more info: http://hadoop.apache.org/docs/r1.2.1/streaming.html)

* The mapper takes lines from the input and converts them into key/value pairs.
* By default, the prefix of a line up to the first tab character is the key and the rest of the line (excluding the tab character) will be the value

# Word count with Hadoop streaming 

http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

Try running the mapper in the first Shakespeare sonnet
```
python word_count_mapper.py < data/shakes_chunk_1.txt 
```

To reproduce what mapReduce would do using word_count_mapper.py  and word_count_reducer.py with this data.

```
python word_count_mapper.py < data/shakes_chunk_1.txt >  mapper_1_out.txt
# sorting 
sort  mapper_1_out.txt > reducer_1_input.txt
python word_count_reducer.py < reducer_1_input.txt
```

We can work with more files
```
python word_count_mapper.py < data/shakes_chunk_1.txt >  mapper_1_out.txt
python word_count_mapper.py < data/shakes_chunk_2.txt >  mapper_2_out.txt
python word_count_mapper.py < data/shakes_chunk_3.txt >  mapper_3_out.txt
# concatenate all mapper ouputs
cat mapper_1_out.txt mapper_2_out.txt mapper_3_out.txt  > mapper_out.txt
# sorting 
sort  mapper_out.txt > reducer_input.txt
python word_count_reducer.py < reducer_input.txt
```
#Exercises

Exercise 1:
Write a mapper and a reducer to compute a histogram of words length.
 
Exercise 2:
Download dataset book rating dataset http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip

Answer the following questions by writting mapReduce jobs.
* How different are books rated in different cities?  Compute average rate per book per city/country. Use cities with at least 10 users. (mapper_cities.py, reducer_cities.py)
* Find the top 30 rated authors. (mapper_authors.py, reducer_authors.py)
* Find users that rated the same author multiple times. 

Submit your solutions to bcources.



