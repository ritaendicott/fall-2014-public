# Word count with Hadoop streaming 

http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

Try running the mapper in the first Shakespeare sonnet
```
python word_count_mapper.py < shakes_chunk_1.txt 
```

To reproduce what mapReduce would do in this data:

```
python word_count_mapper.py < shakes_chunk_1.txt >  mapper_1_out.txt
# sorting 
sort  mapper_1_out.txt > reducer_1_input.txt
python word_count_reducer.py < reducer_1_input.txt
```
