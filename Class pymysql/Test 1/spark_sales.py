# -*- coding: utf-8 -*-
# 用 PySpark 分析 2011 年 1、2 月销售数据（和 main.py 同源数据，换成 Spark 实现）
import os
import sys

os.environ['JAVA_HOME'] = r'D:\develop\Java\jdk-21'      # Spark 需要 JDK 17/21
os.environ['PYSPARK_PYTHON'] = sys.executable            # Windows 没有 python3，必须指定

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.master('local[2]').appName('sales_analysis').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

# 1月：逗号分隔的文本文件
df1 = (spark.read.text(r'D:\2011年1月销售数据.txt')
       .select(F.split('value', ',').alias('c'))
       .select(
           F.col('c')[0].alias('date'),
           F.col('c')[1].alias('order_id'),
           F.col('c')[2].cast('int').alias('money'),
           F.col('c')[3].alias('province')
       ))

# 2月：JSON Lines 文件
df2 = spark.read.json(r'D:\2011年2月销售数据JSON.txt')

# 合并两个月的数据
all_df = df1.unionByName(df2)
print('总记录数:', all_df.count())
print('总销售额:', all_df.agg(F.sum('money')).collect()[0][0])

# 按日汇总销售额（和 main.py 的 data_dict 结果一致）
daily = (all_df.groupBy('date')
         .agg(F.sum('money').alias('total_money'))
         .orderBy('date'))
print('== 每日销售额（前 5 天）==')
daily.show(5)

# 各省销售额 Top10
province_top = (all_df.groupBy('province')
                .agg(F.sum('money').alias('total_money'))
                .orderBy(F.desc('total_money')))
print('== 各省销售额 Top10 ==')
province_top.show(10)

spark.stop()
print('SPARK_SALES_OK')