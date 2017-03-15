import pymysql

conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user = 'goodchat', password = 'goodchat', db = 'DublinBikes')

cur = conn.cursor()
cur.execute("SELECT * FROM Bike_Data")
for row in cur.fetchall():
    print(row[0])

conn.close()