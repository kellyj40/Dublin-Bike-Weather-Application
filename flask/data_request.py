import pymysql

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