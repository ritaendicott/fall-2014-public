Statistics 157: Homework 8: Reproducible and Collaborative Data Science
================



Write mapReduce jobs for the following:

1. Histogram of number of books rated by user. (I don't need the plot.)

 Name the files: You need two mapReduce jobs. Call them mapper_numbooks_1.py, reducer_numbooks_1.py and mapper_numbooks_2.py, reducer_numbooks_2.py

Each line in the final output should contain the number of books rated by that user, number of users.

5 \t 10 # 10 users rated exactly 5 books.


2. CTR by age group. (User a mapReduce join)

This question also needs two iterations of mapreduce.

Name the files: mapper_ctr_1.py, reducer_ctr_1.py, mapper_ctr_2.py, reducer_ctr_2.py

The data files are smallinstances.txt and smalluser.txt. hw8_data.zipView in a new window

Each line of the final has the age group and the CTR for that age group 



