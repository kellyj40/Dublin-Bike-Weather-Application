import pymysql
import datetime
import time

def add_day_hour():
	
	conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                               password='goodchat', db='DublinBikes')
	cur = conn.cursor()
	query_string = "SELECT number, last_update FROM DublinBikes.Bike_Data WHERE number > 3 AND number < 10;"
	cur.execute(query_string)
	conn.commit()
	
	for row in cur.fetchall():
		cur = conn.cursor()
		query_string = "UPDATE DublinBikes.Bike_Data SET weekday={0}, hour={1} WHERE number={2} AND last_update={3};".format(datetime.datetime.fromtimestamp(row[1]/1000).weekday(), datetime.datetime.fromtimestamp(row[1]/1000).hour, row[0], row[1])
		cur.execute(query_string)
		conn.commit()
	
	conn.close()
	
	
add_day_hour()