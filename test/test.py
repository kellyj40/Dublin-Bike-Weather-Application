import pymysql
conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                           password='goodchat', db='DublinBikes')
cur = conn.cursor()
cur.execute("""SELECT name FROM Bike_Data WHERE number = 1 AND last_update = 1489622323000;""")
for row in cur.fetchall():
    print(row[0])
conn.close()