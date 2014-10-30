Lecture 19 Lab
================

## Objectives
Learn how run MapReduce jobs (Python streaming) in AWS

## Instructions
git pull to get the starter code for the class.


### aws account login
https://stat157-uq85def.signin.aws.amazon.com/console

### To run a mapReduce job
#### Upload your code to S3
Go to  S3
Under your home folder make the following folders
```
logs
outputs
code
```
Under "code" make the folder "word_count" and upload the files (from lec-15-lab):
```
word_count_mapper.py
word_count_reducer.py
```
Under "code" make the folder "ctr_adid" and upload the files:
```
ctr_adid_mapper.py
ctr_adid_reducer.py
```

#### Run your code on ElasticMapreduce
Open a new tab with ElasticMapreduce

* Part 1: Run your mapreduce job with the word_count and the file:
```
https://s3-us-west-2.amazonaws.com/stat157-uq85def/shared/shakes.txt
```
* Part 2: Run your mapreduce job with the CTR data and the code under code/ctr_adid

Follow the instructions from the slides from the class.
* Create a cluster
* Change cluster name
* Select log path: \<your home\>/logs
* In "Applications to be installed" remove hive and pig
* Select the number of "Core" and "Task" EC2 instances (2, 2)
* Select your EC2 key pair
* In "IAM Roles" select EMR_DefaultRole and EMR_EC2_DefaultRole 
* In "Steps" select "streaming program"
  * Add and configure steps
  * Add paths for mapper, reducer
  * Input file is here:
  * Point the output to \<your home\>/outputs/\<new folder name\>
* ADD
* CREATE CLUSTER


### To upload and download data from S3 get s3cmd
* http://s3tools.org/download

* For mac you can use brew
```
brew install s3cmd
```

sample commands
```
# List your buckets
s3cmd ls
# List the content of your bucket
s3cmd ls s3://logix.cz-test
# List the size of a bucket with "human readable" units
s3cmd du -H 
# Upload a file into your bucket
s3cmd put addressbook.xml s3://logix.cz-test/addrbook.xml
# Download a file
s3cmd get s3://logix.cz-test/addrbook.xml addressbook-2.xml
# delete files
s3cmd del s3://logix.cz-test/test.txt
```

