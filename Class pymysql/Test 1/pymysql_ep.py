from pymysql import connect

conn = connect(
    host="localhost",
    port=3306,
    user="root",
    password="20051003xuhao",
    autocommit=True
)

# print(conn.get_server_info())

cursor=conn.cursor()
conn.select_db("test")
cursor.execute("create table if not exists test_pymysql(id int,name varchar(255));")
cursor.execute("insert into test_pymysql values(1,'周杰伦');")
cursor.execute("select * from test_pymysql;")
results:tuple=cursor.fetchall()
for l in results:
    print(l)

conn.close()