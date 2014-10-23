# Lab for lecture 17

Download the last.fm dataset from 
http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/lastfm-360K.html

The goal of this lab is to develop a basic algorithm to make music recommendation to users based
on their usage of last.fm

### Data Format

The data is formatted one entry per line as follows (tab separated "\t"):
```
File usersha1-artmbid-artname-plays.tsv:
user-mboxsha1 \t musicbrainz-artist-id \t artist-name \t plays

File usersha1-profile.tsv:
user-mboxsha1 \t gender (m|f|empty) \t age (int|empty) \t country (str|empty) \t signup (date|empty)
```




Submit your solutions to bcources.
