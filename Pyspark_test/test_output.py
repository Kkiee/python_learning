import json
import os
import shutil
from pyspark import SparkConf, SparkContext

# 配置环境变量
os.environ['JAVA_HOME'] = r'D:\develop\Java\jdk-21'
os.environ['PYSPARK_PYTHON'] = r'C:\Users\18218\anaconda3\envs\pyspark310\python.exe'
os.environ['HADOOP_HOME'] = r'D:\BaiduNetdiskDownload\hadoop-3.0.0'

# 初始化 SparkConf
conf = SparkConf()
conf.setMaster("local[4]")
conf.setAppName("PySpark")
conf.set( "spark.default.parallelism", "1")
print("正在启动 Spark，首次约需 20 秒，请稍等...")
sc = SparkContext(conf=conf)

# 读取文件转换成RDD
file_rdd = sc.textFile("D:/BaiduNetdiskDownload/search_log.txt")

# 需求1: 热门搜索时间段Top3(小时精度)
result1 = file_rdd.map(lambda x: (x.split("\t")[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)
print("需求1的结果:", result1)

# 需求2: 热门搜索词Top3
result2 = file_rdd.map(lambda x: (x.split("\t")[2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)
print("需求2的结果:", result2)

# 需求3: 统计黑马程序员关键字在什么时段被搜索的最多
result3 = file_rdd.map(lambda x: x.split("\t")).\
    filter(lambda x: x[2] == '黑马程序员').\
    map(lambda x: (x[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(1)
print("需求3的结果:", result3)

# 需求4: 将数据转换为JSON格式，写出到文件中
# 先删除旧的输出目录（saveAsTextFile 不允许覆盖已存在的目录）
shutil.rmtree("D:/output_json", ignore_errors=True)
file_rdd.map(lambda x: x.split("\t")).\
    map(lambda x: {"time": x[0], "user_id": x[1], "key_Word": x[2], "rank1": x[3], "rank2": x[4], "url": x[5]}).\
    saveAsTextFile("D:/output_json")

sc.stop()
print("全部完成")