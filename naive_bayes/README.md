How to write a naive bayes algorithm in MapReduce 
================
### Step 1
For every feature you are interested in write a MapReduce jobs that computes the aggregate impressions and clicks for every feature and value.
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










