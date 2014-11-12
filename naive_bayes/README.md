How to write a naive bayes on MapReduce.  
================
This is for a CTR problem.
### Step 1
For every feature you are interested in write a MapReduce jobs that computes the aggregate impressions and clicks for every feature and value. This runs on the training set.
```
value \t feature \t clicks \t impressions
# Example
10040	advert_id	0	6
1007	advert_id	0	1
10110295	ad_id	0	1
10110317	ad_id	0	1
10110333	ad_id	0	1
10110372	ad_id	0	1
10110402	ad_id	0	2
```

### Step 2
Write a script (regular python script) that computes
```
Pr(feature = value | click), Pr(feature = value |no-click), Pr(click), Pr(no_click),
Pr(feature = "UNK" | click), Pr(feature = "UNK" |no-click)
```
for every feature and every value. 
Pr(feature = "UNK" | click), Pr(feature = "UNK" |no-click) are used to match values that do not appear in the training set.

Save this in a file
```
advert_id 10040 0.00184842883549 0.00377969762419
advert_id 1007 0.00184842883549 0.00107991360691
ad_id 10110295 0.00109170305677 0.000898069151325
ad_id 10110317 0.00109170305677 0.000898069151325
ad_id 10110333 0.00109170305677 0.000898069151325
ad_id 10110372 0.00109170305677 0.000898069151325
ad_id 10110402 0.00109170305677 0.00134710372699
ad_id UNK 0.00109170305677 0.000449034575662
advert_id UNK 0.00184842883549 0.000539956803456
Total Total 0.033185840708 0.966814159292
```

### Step 3
Write a mapper that loads file with probabilities and computes Pr(click | Data). This runs on validation / test data.

* Use this code as a starting point: https://github.com/ucb-stat-157/fall-2014-public/blob/master/naive_bayes/nb_step2_mapper.py
* To run this you need to send the probability file to every mapper task. You do this by using the -cacheFile option in the "Arguments". Here is an example:
```
-cacheFile s3://stat157-uq85def/home/yannet/code/testing_nb/sample_prob.txt#sample_prob.txt
```
The general form is: 
-cacheFile <s3 bucket>/file.txt#reference
where reference is used in the python script to open the file.
```
with open("reference") as reference_file:
```
* The reducer on step 3 is the "identify reducer", you can used 
```
org.apache.hadoop.mapred.lib.IdentityReducer
```
* the output of this step should be something like
```
Pr(Click | Data) \t Clicks \t Impressions
or
Pr(Click | Data) \t click  ## this would be for a simple impression 
```
* Here is a screen shot on how run it in aws.
https://github.com/ucb-stat-157/fall-2014-public/blob/master/naive_bayes/ScreenShotAWS.png

### Step 4
Compute validation / test AUC. You could use a library in R or python.






