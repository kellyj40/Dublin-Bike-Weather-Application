from sqlalchemy import create_engine
from pandas import DataFrame
import datetime

engine2 = create_engine(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                               password='goodchat', db='DublinBikes')
connection2 = engine2.connect()
day = datetime.datetime.today().weekday()
station_number = 6
var = connection2.execute("SELECT hour, AVG(available_bikes) FROM Bike_Data WHERE number = '{0}' AND weekday = {1} GROUP BY hour;".format(station_number, day))
df = DataFrame(var.fetchall())
df.columns = var.keys()
