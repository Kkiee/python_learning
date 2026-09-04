import os
os.environ['JAVA_HOME'] = r'D:\develop\Java\jdk-21'
os.environ['PYSPARK_PYTHON'] = r'C:\Users\18218\anaconda3\envs\pyspark310\python.exe'
os.environ['HADOOP_HOME'] = "D:/BaiduNetdiskDownload/hadoop-3.0.0"


from pyspark import SparkContext, SparkConf
import json

conf= SparkConf().setMaster("local[4]").setAppName("test")

print("正在启动 Spark，首次约需 20 秒，请稍等...")
sc = SparkContext(conf=conf)

#需求1: 城市销售额排名
#1.1 读取文件得到RDD
file_rdd = sc.textFile("D:/orders.txt")
#1.2 取出一个个JSON字符串
json_str_rdd = file_rdd.flatMap(lambda x: x.split("|"))
#1.3 将一个个JSON字符串转换为字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))
#1.4 取出城市和销售额数据 (城市, 销售额)
city_with_money_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))
#1.5 按城市分组按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a, b: a + b)
#1.6 按销售额聚合结果进行排序
result1_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print("需求1的结果:", result1_rdd.collect())

#需求3: 北京市售出商品类别去重
#3.1 过滤北京市的数据
beijing_data_rdd = dict_rdd.filter(lambda x: x['areaName'] == '北京')
#3.2 取出全部商品类别
result3_rdd = beijing_data_rdd.map(lambda x: x['category']).distinct()
print("需求3的结果:", result3_rdd.collect())

sc.stop()