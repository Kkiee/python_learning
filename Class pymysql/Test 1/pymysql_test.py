from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Record
from pymysql import connect
import json
import os

text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")

jan_data: list[Record] =text_file_reader.read_data()
feb_data: list[Record] =json_file_reader.read_data()
all_data: list[Record] =jan_data + feb_data

conn=connect(
    host="localhost",
    port=3306,
    user="root",
    password="20051003xuhao",
    autocommit=True
)
cursor=conn.cursor()
conn.select_db("test")
# 先删旧表再建表，避免上次运行残留的表结构不匹配
cursor.execute("drop table if exists test_pymysql;")
cursor.execute("create table if not exists test_pymysql("
               "order_date date, order_id varchar(255), money int, province varchar(20));")

# 1.把读取到的数据全部写入MySQL
for record in all_data:
    sql = (f"insert into test_pymysql(order_date, order_id, money, province) "
           f"values('{record.date}', '{record.id}', {record.money}, '{record.province}');")
    cursor.execute(sql)

# 2.读取数据库全部数据
cursor.execute("select order_date,order_id,money,province from test_pymysql;")
rows = cursor.fetchall()  # 返回元组列表 [(date,id,money,province), ...]

# 3.写入txt，一行一个json（输出到本脚本所在目录，避免受运行目录影响）
with open("mysql_export.txt", "w", encoding="UTF-8") as f:
    for row in rows:
        # 组装字典，key要和截图里面的json键对应
        dic = {
            "date": str(row[0]),   # date列是datetime.date，转成字符串
            "order_id": row[1],
            "money": row[2],
            "province": row[3]
        }
        # json.dumps转字符串，写入一行，加换行
        line = json.dumps(dic, ensure_ascii=False)
        f.write(line + "\n")

conn.close()