# Word count with Hadoop streaming 

http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

Try running the mapper in the first Shakespeare sonnet
```
python word_count_mapper.py < shakes_chunk_1.txt 
```

To reproduce what mapReduce would do using word_count_mapper.py  and word_count_reducer.py with this data.

```
python word_count_mapper.py < shakes_chunk_1.txt >  mapper_1_out.txt
# sorting 
sort  mapper_1_out.txt > reducer_1_input.txt
python word_count_reducer.py < reducer_1_input.txt
```

We can work with more files
```
python word_count_mapper.py < shakes_chunk_1.txt >  mapper_1_out.txt
python word_count_mapper.py < shakes_chunk_2.txt >  mapper_2_out.txt
python word_count_mapper.py < shakes_chunk_3.txt >  mapper_3_out.txt
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



