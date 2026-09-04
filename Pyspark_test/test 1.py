import os
os.environ['JAVA_HOME'] = r'D:\develop\Java\jdk-21'
os.environ['PYSPARK_PYTHON'] = r'C:\Users\18218\anaconda3\envs\pyspark310\python.exe'
os.environ['HADOOP_HOME'] = "D:/BaiduNetdiskDownload/hadoop-3.0.0"

from pyspark import SparkContext, SparkConf

conf= SparkConf().setMaster("local[4]").setAppName("test")

print("正在启动 Spark，首次约需 20 秒，请稍等...")
sc = SparkContext(conf=conf)

rdd=sc.textFile("D:/hello.txt")
word_rdd=rdd.flatMap(lambda line: line.split())
word_with_one_rdd=word_rdd.map(lambda word: (word, 1))
result_rdd=word_with_one_rdd.reduceByKey(lambda x, y: x + y)
print(result_rdd.collect())
finall_rdd=result_rdd.sortBy(lambda x: x[1], ascending=False,numPartitions=1)
print(finall_rdd.collect())

sc.stop()