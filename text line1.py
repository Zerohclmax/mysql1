import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute('USE TEXT1')
cursor.execute('SHOW TABLES')
data = cursor.fetchone()
data1 = cursor.fetchone()
data2 = cursor.fetchone()
print(data,data1,data2)
db.close()
