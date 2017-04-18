from sqlalchemy import create_engine
from pandas import DataFrame
import datetime
import pymysql


class LocationQueries:
    def __init__(self):
        URI = "dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com"
        PORT = "3306"
        DB = "DublinBikes"
        USER = "goodchat"
        PASSWORD = "goodchat"
        self.engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)


    def test_query(self):
        query_string = "SELECT * FROM Bike_Data;"
        res = self.engine.execute(query_string).fetchall()
        return res

    def historical(self):
        connection2 = self.engine.connect()
        day = datetime.datetime.today().weekday()
        station_number = 6
        var = connection2.execute("SELECT hour, AVG(available_bikes) FROM Bike_Data WHERE number = '{0}' AND weekday = {1} GROUP BY hour;".format(station_number, day))
        df = DataFrame(var.fetchall())
        df.columns = var.keys()
        return df
