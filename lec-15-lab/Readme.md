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
Write a mapper and a reducer to:
1. Compute a histogram of words length.
2. 
