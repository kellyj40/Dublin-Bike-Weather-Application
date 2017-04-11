from sqlalchemy import create_engine
from pandas import DataFrame
import datetime
import pymysql

def test_pandas():
    URI= "dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com"
    PORT = "3306"
    DB = "DublinBikes"
    USER = "goodchat"
    PASSWORD = "goodchat"
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USER, PASSWORD, URI, PORT, DB), echo=True)

    query_string = "SELECT * FROM Bike_Data;"
    res = engine.execute(query_string).fetchall()
    print(res)



    connection2 = engine.connect()
    day = datetime.datetime.today().weekday()
    station_number = 6
    var = connection2.execute("SELECT hour, AVG(available_bikes) FROM Bike_Data WHERE number = '{0}' AND weekday = {1} GROUP BY hour;".format(station_number, day))
    df = DataFrame(var.fetchall())
    df.columns = var.keys()
    return df
