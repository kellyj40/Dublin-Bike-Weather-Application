import pymysql
import datetime
import time
import closest_neighbour
from pandas import DataFrame as df

class database_queries:

    def __init__(self):
        self.conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                               password='goodchat', db='DublinBikes')

    def get_locations(self):
        cur = self.conn.cursor()
        cur.execute("""SELECT number, name, lat, lng FROM Static_Data ORDER BY name;""")
        self.conn.commit()
        location_info = []
        for row in cur.fetchall():
            location_info.append(row)
        cur.close()
        return location_info

    def get_info(self, val):
        cur = self.conn.cursor()
        query_string = "SELECT name FROM Static_Data WHERE number =  '{val}'".format(val=val)
        cur.execute(query_string)
        self.conn.commit()
        for row in cur.fetchall():
            place = row
            break

        query_string = "SELECT * FROM Bike_Data WHERE number =  '{val}'".format(val=val)
        cur.execute(query_string)
        self.conn.commit()
        information = []
        for row in cur.fetchall():
            information.append(row)

        cur.close()
        return place, information

    def get_station_name(self, station_number):
        cur = self.conn.cursor()
        #Get name and position of location
        query_string = "SELECT number, name, lat, lng FROM Static_Data WHERE number =  '{val}'".format(val=station_number)
        cur.execute(query_string)
        place = cur.fetchall()
        query_string = "SELECT number, name, lat, lng FROM Static_Data;"
        cur.execute(query_string)
        all_locations = cur.fetchall()
        neighbours = closest_neighbour.find_closest_neighbours(place,all_locations)
        #Get current data
        query_string = "SELECT * FROM Current_Data WHERE number =  '{val}'".format(val=station_number)
        cur.execute(query_string)
        data = {}  # creating python dictionary to store the data for each stop number
        row  = cur.fetchall()[0]
        data[str(row[0])] = list(row[1:])
        #Calculate the last update
        data[str(row[0])][7] = int(datetime.datetime.fromtimestamp(int(time.time()) - (data[str(row[0])][7] / 1000)).strftime('%M'))
        cur.close()
        return place[0], data, neighbours

    def current_info(self):
        cur = self.conn.cursor()
        query_string = "SELECT * FROM Current_Data;"
        cur.execute(query_string)
        self.conn.commit()
        data = {} #creating python dictionary to store the data for each stop number
        for row in cur.fetchall():
            data[str(row[0])] = list(row[1:])
            data[str(row[0])][7] = int(datetime.datetime.fromtimestamp(int(time.time())-(data[str(row[0])][7]/1000)).strftime('%M'))
        cur.close()
        return data

    def weather_info(self):
        cur = self.conn.cursor()
        query_string = "SELECT * FROM weather_Data;"
        cur.execute(query_string)
        self.conn.commit()
        data = {}  # creating python dictionary to store the data for each stop number
        for row in cur.fetchall():
            data[str(row[0])] = list(row[1:])
            data[str(row[0])][4] = int(
                datetime.datetime.fromtimestamp(int(time.time()) - (data[str(row[0])][4])).strftime('%M'))
        return data

    def historical_data_day(self, station_number, day = None):
        if day is None:
            day = datetime.datetime.today().weekday()
        cur = self.conn.cursor()
        query_string = "SELECT hour, AVG(available_bikes) FROM Bike_Data WHERE number = '{0}' AND weekday = {1} GROUP BY hour;".format(station_number, day)
        cur.execute(query_string)
        self.conn.commit()
        data = []
        for row in cur.fetchall():
            data.append([row[0], int(row[1])])
        return data

    def historical_data_week(self, station_number):
        cur = self.conn.cursor()
        query_string = "SELECT weekday, AVG(available_bikes), AVG(available_bike_stands) FROM Bike_Data WHERE number = '{0}' GROUP BY weekday;".format(
            station_number)
        cur.execute(query_string)
        self.conn.commit()
        data = []
        for row in cur.fetchall():
            data.append([row[0], int(row[1]), int(row[2])])
        return data