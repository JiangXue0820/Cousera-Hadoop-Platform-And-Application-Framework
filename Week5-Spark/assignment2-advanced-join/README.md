# Week 5: Spark - Assignment 2: Advanced Join

In this assignment we will use the data generated in the second part of the programming assignment of module 4 lesson 2. The gennum files contain show names and their viewers, genchan files contain show names and their channel. We want to find out the total number of viewers across all shows for the channel BAT.

## Steps for completing the task:
### 1. Verify input data
Make sure the 6 files are available in the HDFS folder (here define the directory as `input/`) by running this command in the terminal (not in PySpark!):
```
hdfs dfs -ls input/
```
The directory should contain 6 files:
```
input/join2_genchanA.txt
input/join2_genchanB.txt
input/join2_genchanC.txt
input/join2_gennumA.txt
input/join2_gennumB.txt
input/join2_gennumC.txt
```
Otherwise use following command to move files from local directory to HDFS, where `dir1` is the local directory and `dir2` is the directory in HDFS:
```
hdfs dfs -put dir1 dir2
```

### 2. Read Files
- Read shows files: 
  The gennum files contain show names and number of viewers. We can read them into Spark with a pattern matching using the `?` mark:
```
show_views_file = sc.textFile("input/join2_gennum?.txt")
```
- Read channel files:
  The genchan files contain show names and channel. We can read them into Spark with a pattern matching using the `?` mark:
```
show_channel_file = sc.textFile("input/join2_genchan?.txt")
```

### 3. Parse Files
- [split_show_views.py: ](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/blob/master/Week5-Spark/assignment2-advanced-join/split_show_views.py) The function splits gennum files and outputs `(show, views)` pairs.
- [split_show_channel.py: ](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/blob/master/Week5-Spark/assignment2-advanced-join/split_show_views.py) The function splits genchan files and outputs `(show, channel)` pairs.
- Use the functions to transform the input RDD as following:
```
show_views = show_views_file.map(split_show_views)
show_channel = show_channel_file.map(split_show_channel)
```

### 4. Join the 2 datasets
```
joined_dataset = show_channel.join(show_views)
```

### 5. Extract channel as key
- [extract_channel_views.py: ](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/blob/master/Week5-Spark/assignment2-advanced-join/extract_channel_views.py)We want to find the total viewers by channel, so we need to create an RDD with the channel as key and all the viewer counts, whichever is the show. 
- Apply this function to the joined dataset to create an RDD of channel and views:
```
channel_views = joined_dataset.map(extract_channel_views)
```

### 6. Sum across all channels
- [calculate_sum.py: ](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/blob/master/Week5-Spark/assignment2-advanced-join/calculate_sum.py)The function sums all of the viewers for each channel.
- Collect the final result.
```
channel_views.reduceByKey(sum_channel_views).collect()
```

### 7. Final output
- [channel_views_output.txt](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/blob/master/Week5-Spark/assignment2-advanced-join/channel_views_output.txt)






