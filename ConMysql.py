import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='test',
)

cur = conn.cursor()

sql = "insert into piaoniu_page (title,dt,address,url) values ('%s','%s','%s','%s')" % ('1','2','3','4')

cur.execute(sql)

conn.commit()

cur.close()

conn.close()