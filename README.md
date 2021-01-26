# Data-Analysis-with-Hadoop
1. Get data from Stack Exchange
2. Load them with PIG
3. Query them with Hive
4. Calculate TF-IDF with MapReduce/Pig/Hive
## Requirements:
1. Acquire the top 200,000 posts by viewcount (see notes on Data Acquisition)
2. Using Pig or MapReduce, extract, transform and load the data as applicable
3. Using Hive and/or MapReduce, get:
- I. The top 10 posts by score
- II. The top 10 users by post score
- III. The number of distinct users, who used the word “Hadoop” in one of their posts
4. Using Mapreduce/Pig/Hive calculate the per-user TF-IDF (just submit the top10 terms for each of the top 10 users from Query 3.II)
