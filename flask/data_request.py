import pymysql
class database_queries:
    def __init__(self):
        self.conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                               password='goodchat', db='DublinBikes')

    def get_locations(self):
        cur = self.conn.cursor()
        cur.execute("""SELECT number, name, lat, lng FROM Static_Data;""")
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
        query_string = "SELECT name FROM Static_Data WHERE number =  '{val}'".format(val=station_number)
        cur.execute(query_string)
        self.conn.commit()
        for row in cur.fetchall():
            place = row
            break
        return place

    def current_info(self):
        cur = self.conn.cursor()
        query_string = "SELECT * FROM (SELECT * FROM DublinBikes.Bike_Data ORDER BY last_update DESC) as mytable GROUP BY mytable.number;"
        cur.execute(query_string)
        self.conn.commit()
        data={} #creating python dictionary to store the data for each stop number
        for row in cur.fetchall():
            data[str(row[0])]=row[1:]
        cur.close()
        return data
