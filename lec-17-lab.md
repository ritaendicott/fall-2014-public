# Lab for lecture 17

Download the last.fm dataset from 
http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-360K.html

The goal of this lab is to develop a basic algorithm to make music recommendation to users based
on their usage of last.fm

### Data format

The data is formatted one entry per line as follows (tab separated "\t"):
```
File usersha1-artmbid-artname-plays.tsv:
user-mboxsha1 \t musicbrainz-artist-id \t artist-name \t plays

File usersha1-profile.tsv:
user-mboxsha1 \t gender (m|f|empty) \t age (int|empty) \t country (str|empty) \t signup (date|empty)
```

### Item based recommendations

Method in which we find similarities between items (artists) to make recommendations. 

One was of computing similarities between two artists (A and B) is by computing the following metric.

```
| User who listen to A AND B | / |Users who listen to A or B|
```


Our last.fm file has

user \t artist-id \t artist-name \t plays

* Step 1: Create a new data set with
   user \t artist-id \t artist-id-total
   where artist-id-total are the number of user who pay to artist-id.

* Step 2: From the dataset in step 1 create a new dataset
   user \t (artist-id1, artist-id1-total), (artist-id2, artist-id2-total) ...
   that is, all the artists played by user

* Step 3: From the datset in step 2 create the following dataset
  (artist-id1, artist-id2) \t (intercept-id1-id2, artist-id1-total, artist-id2-total)
  where intercept-id1-id2 are the number of users who listen to  artist-id1 AND artist-id2

Submit your solutions to bcources.
