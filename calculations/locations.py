import datetime
import pymysql
import pprint as pp

conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat', password='goodchat', db='DublinBikes')

cur = conn.cursor()
cur.execute("""SELECT number, name, lat, lng FROM Bike_Data GROUP BY number;""")
conn.commit()
location_info = []
for row in cur.fetchall():
    location_info.append({"number": row[0], "name": row[1], "lat": row[2], "lng": row[3]})
cur.close()
pp.pprint(location_info)
