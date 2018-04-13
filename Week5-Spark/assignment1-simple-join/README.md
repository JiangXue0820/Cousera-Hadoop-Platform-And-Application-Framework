# Week 5: Spark - Assignment 1: Simple Join

In this programming assignment we will implement in Spark the same code in the programming assignment in module 4 lesson 2 to perform a join of 2 different wordcount datasets.

## Steps for completing the task:
### 1. Verify datasets
Make sure the 2 files are available in the HDFS folder (here define the directory as `input/`) by running this command in the terminal (not in PySpark!):
```
hdfs dfs -ls input/
```
The directory should contain 2 files:
```
input/join1_FileA.txt
input/join1_FileB.txt
```
If the files are not added into HDFS yet, using the following command to move both files from local directory to HDFS, where `dir1` is the local directory and `dir2` is the directory in HDFS:
```
hdfs dfs -put dir1 dir2
```
### 2.Load datasets
- Open the pyspark shell and load the datasets you created for the previous assignment from HDFS
```
fileA = sc.textFile("input/join1_FileA.txt")
fileB = sc.textFile("input/join1_FileB.txt")
```
- Make sure the file content is correct by using `.collect()`:
```
fileA.collect()
Out[]: [u'able,991', u'about,11', u'burger,15', u'actor,22']
```

### 3.Create Mappers
- Mapper for fileA: [split_fileA.py](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/blob/master/Week5-Spark/assignment1-simple-join/split_fileA.py). The function splits fileA.txt and outputs `(word, total-count)` pairs.
- Mapper for fileB: [split_fileB.py](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/blob/master/Week5-Spark/assignment1-simple-join/split_fileB.py). The function splits fileB.txt and outputs `(word, date day-count)` pairs.
- Map transformation for both files:
```
fileA_data = fileA.map(split_fileA)
fileB_data = fileB.map(split_fileB)
```

### 4.Run join
- The goal is to join the two datasets using the words as keys and print for each word the wordcount for a specific date and then the total output from A. Spark implements the join transformation that given a RDD of (K, V) pairs to be joined with another RDD of (K, W) pairs, returns a dataset that contains (K, (V, W)) pairs.
```
fileB_joined_fileA = fileB_data.join(fileA_data)
```
- Verify the result
```
fileB_joined_fileA.collect()
```

### 5.Final output
- [join_output.txt](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/blob/master/Week5-Spark/assignment1-simple-join/join_output.txt)



