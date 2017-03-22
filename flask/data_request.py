import pymysql

def test_function():
    return "hello"

def get_locations():
    conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                           password='goodchat', db='DublinBikes')
    cur = conn.cursor()
    cur.execute("""SELECT number, name, lat, lng FROM Bike_Data GROUP BY number;""")
    conn.commit()
    location_info = []
    for row in cur.fetchall():
        location_info.append(row)
    cur.close()
    return location_info

def get_info(val):
    conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                           password='goodchat', db='DublinBikes')
    cur = conn.cursor()
    query_string = "SELECT name FROM Bike_Data WHERE number =  '{val}'".format(val=val)
    cur.execute(query_string)
    conn.commit()
    for row in cur.fetchall():
        place = row
        break

    query_string = "SELECT * FROM Bike_Data WHERE number =  '{val}'".format(val=val)
    cur.execute(query_string)
    conn.commit()
    information = []
    for row in cur.fetchall():
        information.append(row)

    cur.close()
    return place, information

