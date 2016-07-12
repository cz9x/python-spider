import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='test',
)

cur = conn.cursor()

aa = cur.execute("select * from test.test")

info = cur.fetchmany(aa)

for i in info:
    print i

cur.close()

conn.close()