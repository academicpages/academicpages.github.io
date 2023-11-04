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
---  
tips: After putting hadoop.dll and winutils in hadoop/bin folder and adding the folder of hadoop to PATH, we also need to put hadoop.dll into the C:\Windows\System32 folder
---
3. SPARK, need setting environment variables path.
---
tips: All of the above tools require version mappings...like...spark-3.5.0-bin-hadoop3-scala2.13
---
 
