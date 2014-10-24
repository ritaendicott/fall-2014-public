AWS Instructions
================

# Objectives
Learn how to work with AWS

## Instructions

### aws account login
https://s157-uq2023f.aws.amazon.com/console

### To run a mapReduce job

* 

### To upload and download data from S3 get s3cmd
* http://s3tools.org/download

* For mac you can use brew
```
brew install s3cmd
```
* For linux (VM)
```
sudo apt-get install -y s3cmd
```
You need to configure s3cmd. For this you need your access key and secret key from your amazon account. 
```
s3cmd --configure
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

