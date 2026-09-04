# -*- coding: utf-8 -*-
# PySpark 在 PyCharm 里运行的最小示例
import os
import sys

# 1) Spark 需要 Java 17/21（JDK 26 不支持）。在代码里指定即可，不用改系统环境变量
os.environ['JAVA_HOME'] = r'D:\develop\Java\jdk-21'

# 2) 指定 Spark 的 Python 解释器（必须是装了 pyspark 的那个）。
#    用 sys.executable 自动填当前解释器；也可以写死路径，例如：
#    os.environ['PYSPARK_PYTHON'] = r'D:\Pythonproject\.venv\Scripts\python.exe'
os.environ['PYSPARK_PYTHON'] = sys.executable

from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[2]').appName('pycharm_test').getOrCreate()

df = spark.createDataFrame([(1, 'a'), (2, 'b')], ['id', 'v'])
df.show()

spark.stop()
print('PySpark OK')