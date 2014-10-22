Statistics 157: 
================

Homework 8: Reproducible and Collaborative Data Science


Write mapReduce jobs for the following:
```
1. Histogram of number of books rated by user. (I don't need the plot.)

You need two mapReduce jobs. 
Name you files: mapper_numbooks_1.py, reducer_numbooks_1.py,
                mapper_numbooks_2.py, reducer_numbooks_2.py
```

Data: "BX-Book-Ratings.csv" from http://www2.informatik.uni-freiburg.de/~cziegler/BX/
Each line in the final output should contain the number of books rated by that user, number of users.

5 \t 10 # 10 users rated exactly 5 books.

```
2. CTR by age group. (User a mapReduce join)

This question also needs two iterations of mapreduce.
Name the files: mapper_ctr_1.py, reducer_ctr_1.py,
                mapper_ctr_2.py, reducer_ctr_2.py
```

Data:
The data files are smallinstances.txt and smalluser.txt. (These are subset of the filesuserid_profile.txt and instances.txt from https://www.kddcup2012.org/c/kddcup2012-track2)

Each line of the final has the age group and the CTR for that age group 



