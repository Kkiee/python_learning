import os
os.environ['JAVA_HOME'] = r'D:\develop\Java\jdk-21'
os.environ['PYSPARK_PYTHON'] = r'C:\Users\18218\anaconda3\envs\pyspark310\python.exe'
os.environ['HADOOP_HOME'] = "D:/BaiduNetdiskDownload/hadoop-3.0.0"

from pyspark import SparkContext, SparkConf

conf= SparkConf().setMaster("local[4]").setAppName("test")

print("正在启动 Spark，首次约需 20 秒，请稍等...")
sc = SparkContext(conf=conf)

# map flatmap
rdd_a=sc.parallelize([1,2,3,4,5])
rdd1=rdd_a.map(lambda x: x*10 ).map(lambda x: x+5)
print(rdd1.collect())

#reduceByKey
rdd_b=sc.parallelize([('男',99),('男',100),('女',100),('女',101)])
rdd2=rdd_b.reduceByKey(lambda x,y:x+y)
print(rdd2.collect())

#filter
rdd3=rdd_a.filter(lambda x:x % 2==0)
print(rdd3.collect())

#distinct
rdd_c = sc.parallelize([1,1,3,3,8,8,10])
rdd4 = rdd_c.distinct()
print(rdd4.collect())

#sortBy


sc.stop()