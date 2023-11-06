---
title: "Install spark environment under Conda"
excerpt: "Install the spark under the Conda environment, some details you may loss... <br/><img src='/images/spark.png' width='500' height='300'>"
collection: solving
---

1. JAVA, need setting environment variables path.
   JAVA_HOME/CLASSPATH/PATH
2. HADOOP, need setting environment variables path. Decompress the file as an administrator. Otherwise, a decompression error may occur
   HADOOP_HOME/PATH
   winutils!!!!IMPORTANT!!! **hadoop.dll** and **winutils.exe**
3. SPARK, need setting environment variables path.

[tips_1](https://stackoverflow.com/questions/41851066/exception-in-thread-main-java-lang-unsatisfiedlinkerror-org-apache-hadoop-io): After putting hadoop.dll and winutils in hadoop/bin folder and adding the folder of hadoop to PATH, we also need to put hadoop.dll into the C:\Windows\System32 folder

[tips_2](https://blog.csdn.net/Sun_shine99/article/details/130276488): All of the above tools require version mappings...like...spark-3.5.0-bin-hadoop3-scala2.13
   
