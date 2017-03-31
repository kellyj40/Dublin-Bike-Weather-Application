import pymysql

def test_function():
    return "hello"

def get_locations():
    conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                           password='goodchat', db='DublinBikes')
    cur = conn.cursor()
    cur.execute("""SELECT number, name, lat, lng FROM Static_Data;""")
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
    query_string = "SELECT name FROM Static_Data WHERE number =  '{val}'".format(val=val)
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

def current_info():
    conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                           password='goodchat', db='DublinBikes')
    cur = conn.cursor()
    data=[]
    query_string = "SELECT * FROM Bike_Data GROUP BY number ORDER BY last_update;"
    cur.execute(query_string)
    conn.commit()
    data={} #creating python dictionary to store the data for each stop number
    for row in cur.fetchall():
        data[str(row[0])]=row[1:]
    cur.close()
    return data
