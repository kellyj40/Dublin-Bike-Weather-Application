import requests
import json
import pymysql
import time
import sys

NAME="Dublin"
STATIONS="https://api.jcdecaux.com/vls/v1/stations"
APIKEY="ad351367503efe038d411efe65ed53d1d53044e8"


def main():
    try:
        r = requests.get(STATIONS, params={"apiKey": APIKEY, "contract": NAME})
        store(json.loads(r.text))
    except:
        print(requests.traceback.format_exc())
    #time.sleep(5 * 60)


def store(json_data):
    try:
        conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                               password='goodchat', db='DublinBikes')
        connect(conn, json_data)
        conn.close()
    except:
        pass


def connect(conn, json_data):
    for i in range(0, len(json_data)):
        cur = conn.cursor()
        query = """INSERT INTO Bike_Data(number, name, address, lat, lng, banking, bonus, status, contract_name, bike_stands, available_bike_stands, available_bikes, last_update) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");"""
        try:
            cur.execute(query % (json_data[i]['number'], json_data[i]['name'], json_data[i]['address'],
                                 json_data[i]['position']['lat'], json_data[i]['position']['lng'],
                                 json_data[i]['banking'],
                                 json_data[i]['bonus'], json_data[i]['status'], json_data[i]['contract_name'],
                                 json_data[i]['bike_stands'], json_data[i]['available_bike_stands'],
                                 json_data[i]['available_bikes'], json_data[i]['last_update']))

        except pymysql.err.IntegrityError as e:
            continue
        except:
            file = open('errors_store.txt', 'a')
            file.write(str(sys.exc_info()[0]) + '\n')
            file.close()
        conn.commit()
main()
