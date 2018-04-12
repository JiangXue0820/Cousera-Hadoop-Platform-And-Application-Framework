# [Week 4: Introduction to Map/Reduce](https://www.coursera.org/learn/hadoop/home/week/4)

[MapReduce](https://en.wikipedia.org/wiki/MapReduce) is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.

A MapReduce program is composed of **map** functions and **reduce** functions. **Map** performs filtering and sorting by reading in the data and outputing `(key, value)` pairs. Haddop then shuffels and groups the `(key, value)` pairs where pairs with the same key value are group together. The intermediate data is passed to **reducer**. **Reducer** then performs a summary operation. The key contribution of the map/reduce framework is its scalability and fault tolerance as it uses distributed servers and runs the various tasks in parallel.

There are two programming assignments for the lessons of Week 4:

- [Wordcount](https://github.com/JiangXue0820/Cousera-Hadoop-Platform-And-Application-Framework/tree/master/Week4-Map-Reduce/assignment1-Wordcount)
- Joining Data
  - Simple Join
  - Advanced Join
