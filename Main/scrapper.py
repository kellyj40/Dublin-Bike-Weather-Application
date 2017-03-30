import requests
import json
import pymysql
import time
import sys
import traceback

NAME="Dublin"
STATIONS="https://api.jcdecaux.com/vls/v1/stations"
# with open("/../../API_key.txt", "r") as api_file:
APIKEY="ad351367503efe038d411efe65ed53d1d53044e8"

def main():
    store(request())


def request():
    try:
        r = requests.get(STATIONS, params={"apiKey": APIKEY, "contract": NAME})
        return json.loads(r.text)
    except:
        print("this is the error", traceback.format_exc())

def store(json_data):
    try:
        conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                               password='goodchat', db='DublinBikes')
        connect(conn, json_data)
        conn.close()
    except:
        pass


def connect(conn, json_data):
    cur = conn.cursor()
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS `DublinBikes`.`Bike_Data`(`number` INT NOT NULL,`banking` VARCHAR(45),
        `bonus` VARCHAR(45),`status` VARCHAR(45),`contract_name` VARCHAR(45),`bike_stands` INT(11),`available_bike_stands`
         INT(11),`available_bikes` INT(11),`last_update` BIGINT(20), PRIMARY KEY (`number`,`last_update`));""")
        conn.commit()
        cur.execute("""CREATE TABLE IF NOT EXISTS `DublinBikes`.`Static_Data`(`number` INT NOT NULL,`name` VARCHAR(45),
                `address` VARCHAR(45),`lat` VARCHAR(45),`lng` VARCHAR(45), PRIMARY KEY (`number`));""")
        conn.commit()
    except:
        print("there is no error joe")
        pass
    for i in range(0, len(json_data)):
        query = """INSERT INTO Bike_Data(number, banking, bonus, status, contract_name, bike_stands, available_bike_stands,
         available_bikes, last_update) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s");"""
        query2 = """INSERT INTO Static_Data(number, name, address, lat, lng) VALUES ("%s","%s","%s","%s","%s");"""
        try:
            cur.execute(query % (json_data[i]['number'],
                                 json_data[i]['banking'],
                                 json_data[i]['bonus'], json_data[i]['status'], json_data[i]['contract_name'],
                                 json_data[i]['bike_stands'], json_data[i]['available_bike_stands'],
                                 json_data[i]['available_bikes'], json_data[i]['last_update']))
            conn.commit()
            cur.execute(query2 % (json_data[i]['number'],
                                 json_data[i]['name'],
                                 json_data[i]['address'], json_data[i]['position']['lat'], json_data[i]['position']['lng']))
            conn.commit()
        except pymysql.err.IntegrityError as e:
            continue
        except:
            file = open('errors_store.txt', 'a')
            file.write(str(sys.exc_info()[0]) + '\n')
            file.close()
main()
