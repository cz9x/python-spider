import MySQLdb

conn = MySQLdb.connect(host='43.241.220.35', port=3306, user='root', passwd='zhaime2015', db='spider',
                           use_unicode=True, charset="utf8")

cur = conn.cursor()

sql = 'select city_code from tpp_city_list'

try:
    cur.execute(sql)

    result = cur.fetchall()

    for row in result:
        name = row[0]
        print name

except:
    print "Error"

conn.close()