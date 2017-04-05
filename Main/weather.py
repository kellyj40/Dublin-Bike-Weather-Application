import requests
import json
import pymysql
import time
import sys
import traceback


def main():
    store_weather(request_weather())

def request_weather():
    try:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Dublin,IE&APPID=e4f662351f66a1cf726d30653c696b28')
        return json.loads(r.text)
    except:
        print("this is the error", traceback.format_exc())


def store_weather(json_data):
    try:
        conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                               password='goodchat', db='DublinBikes')
        connect_weather(conn, json_data)
        conn.close()
    except:
        pass


def connect_weather(conn, json_data):
    cur = conn.cursor()
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS `DublinBikes`.`weather_Data`(`name` VARCHAR(45) NOT NULL,`temp` VARCHAR(45),
        `windspeed` VARCHAR(45),`weatherdescription` VARCHAR(45),`icon` VARCHAR(45),`updated` BIGINT(20),
        PRIMARY KEY (`name`));""")
        conn.commit()
    except:
        print("Weather_Data query failed")

    query = """INSERT INTO weather_Data(name, temp, windspeed, weatherdescription, icon, updated)
    VALUES ("%s","%s","%s","%s","%s","%s") ON DUPLICATE KEY UPDATE `name`=VALUES(`name`), `temp`=VALUES(`temp`),
    `windspeed`=VALUES(`windspeed`),`weatherdescription`=VALUES(`weatherdescription`),`icon`=VALUES(`icon`),
    `updated`=VALUES(`updated`);"""
    try:
        cur.execute(query % (json_data['name'], json_data['main']['temp'], json_data['wind']['speed'],
                             json_data['weather'][0]['description'], json_data['weather'][0]['icon'], int(time.time())))
        conn.commit()
    except pymysql.err.IntegrityError:
        pass
    except:
        print("weather data_base error")

main()
