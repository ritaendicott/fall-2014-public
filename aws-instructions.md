AWS Recipies
================
### Recipe for transfering data from one bucket to another using EC2 

* Install and configure s3cmd (for the s3 bucket that has the data)
* cp the data using s3cmd get
* If your data is large > 7G
  * You need to mount a volume first
  * Follow instructions below
* Configure s3cmd for the s3 bucket to cp the data
* Use s3cmd put


I followed these instructions
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

```
df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1      7.8G  7.4G  384K 100% /
none            4.0K     0  4.0K   0% /sys/fs/cgroup
udev             15G   12K   15G   1% /dev
tmpfs           3.0G  336K  3.0G   1% /run
none            5.0M     0  5.0M   0% /run/lock
none             15G     0   15G   0% /run/shm
none            100M     0  100M   0% /run/user
/dev/xvdb        74G   15G   56G  21% /mnt
```

Disk devices and their mount points
```
 lsblk
NAME    MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
xvda    202:0    0   8G  0 disk
└─xvda1 202:1    0   8G  0 part /
xvdb    202:16   0  75G  0 disk /mnt
xvdc    202:32   0  75G  0 disk
```
I wanted to use xvdb that has 75G

```
sudo file -s /dev/xvdb
sudo mkdir /data
sudo mount /dev/xvdb /data
```

I copied my .zip file to /data. Install zip, unziped the data and use s3cmd to pass it to the other s3 bucket.


