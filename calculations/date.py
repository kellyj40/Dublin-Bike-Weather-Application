import datetime
import pymysql

conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user = 'goodchat', password = 'goodchat', db = 'DublinBikes')

cur = conn.cursor()
query = """SELECT available_bikes, last_update FROM Bike_Data  WHERE number = '%s';"""
cur.execute(query % (42))
conn.commit()
for row in cur.fetchall():
    real_time = datetime.datetime.fromtimestamp(row[1]/1000).strftime('%m-%d %H:%M')
    day, tim = real_time.split()
    mon, date = day.split('-')
    hour, min = tim.split(':')
    print(date, hour, row[0])
    # print(real_time)

conn.close()
