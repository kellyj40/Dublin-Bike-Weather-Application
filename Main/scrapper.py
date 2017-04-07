#!/home/ubuntu/anaconda3/bin/python
import requests
import json
import pymysql
import time
import sys
import traceback
import datetime

NAME="Dublin"
STATIONS="https://api.jcdecaux.com/vls/v1/stations"
with open("API_key.txt", "r") as api_file:
    APIKEY=api_file.read()
    def main():
        store(request())
        main2()
    def request():
        try:
            r = requests.get(STATIONS, params={"apiKey": APIKEY, "contract": NAME})
            with open('backup_data.txt', 'a') as file: #storing data in backup text file
                file.write(r.text)
                file.close()
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
             INT(11),`available_bikes` INT(11),`last_update` BIGINT(20), `weekday` INT(11), `hour` INT(11), PRIMARY KEY (`number`,`last_update`));""")
            conn.commit()
        except:
            print("Bike_Data query failed")
        try:
            cur.execute("""CREATE TABLE IF NOT EXISTS `DublinBikes`.`Static_Data`(`number` INT NOT NULL,`name` VARCHAR(45),
                    `address` VARCHAR(45),`lat` VARCHAR(45),`lng` VARCHAR(45), PRIMARY KEY (`number`));""")
            conn.commit()
        except:
            print("Static_Data query failed")
        try:
            cur.execute("""CREATE TABLE IF NOT EXISTS `DublinBikes`.`Current_Data`(`number` INT NOT NULL,`banking` VARCHAR(45),
            `bonus` VARCHAR(45),`status` VARCHAR(45),`contract_name` VARCHAR(45),`bike_stands` INT(11),`available_bike_stands`
            INT(11),`available_bikes` INT(11),`last_update` BIGINT(20), PRIMARY KEY (`number`));""")
            conn.commit()
        except:
            print("Current_Data query failed")
        for i in range(0, len(json_data)):
            query = """INSERT INTO Bike_Data(number, banking, bonus, status, contract_name, bike_stands, available_bike_stands,
             available_bikes, last_update, weekday, hour) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");"""
            query3 = """INSERT INTO DublinBikes.Current_Data(number, banking, bonus, status, contract_name, bike_stands, available_bike_stands,
                            available_bikes, last_update) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s")
                            ON DUPLICATE KEY UPDATE
                            `banking`=VALUES(`banking`),
                            `bonus`=VALUES(`bonus`),
                            `status`=VALUES(`status`),
                            `contract_name`=VALUES(`contract_name`),
                            `bike_stands`=VALUES(`bike_stands`),
                            `available_bike_stands`=VALUES(`available_bike_stands`),
                            `available_bikes`=VALUES(`available_bikes`),
                            `last_update`=VALUES(`last_update`);"""
            query2 = """INSERT INTO Static_Data(number, name, address, lat, lng) VALUES ("%s","%s","%s","%s","%s");"""
            try:
                cur.execute(query % (json_data[i]['number'],
                                     json_data[i]['banking'],
                                     json_data[i]['bonus'], json_data[i]['status'], json_data[i]['contract_name'],
                                     json_data[i]['bike_stands'], json_data[i]['available_bike_stands'],
                                     json_data[i]['available_bikes'], json_data[i]['last_update'],
                                     datetime.datetime.fromtimestamp(json_data[i]['last_update']/ 1000).weekday(),
                                     datetime.datetime.fromtimestamp(json_data[i]['last_update'] / 1000).hour))
                conn.commit()
            except pymysql.err.IntegrityError:
                continue
            except:
                file = open('errors_store.txt', 'a')
                file.write(str(sys.exc_info()[0]) + '\n')
                file.close()
            try:
                cur.execute(query3 % (json_data[i]['number'],
                                      json_data[i]['banking'],
                                      json_data[i]['bonus'], json_data[i]['status'], json_data[i]['contract_name'],
                                      json_data[i]['bike_stands'], json_data[i]['available_bike_stands'],
                                      json_data[i]['available_bikes'], json_data[i]['last_update']))
                conn.commit()
            except pymysql.err.IntegrityError:
                continue
            except:
                file = open('errors_store.txt', 'a')
                file.write(str(sys.exc_info()[0]) + '\n')
                file.close()
            try:
                cur.execute(query2 % (json_data[i]['number'],
                                      json_data[i]['name'],
                                      json_data[i]['address'], json_data[i]['position']['lat'], json_data[i]['position']['lng']))
                conn.commit()
            except pymysql.err.IntegrityError:
                continue
            except:
                file = open('errors_store.txt', 'a')
                file.write(str(sys.exc_info()[0]) + '\n')
                file.close()

    def main2():
        store_weather(request_weather())


    def request_weather():
        try:
            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?q=Dublin,IE&APPID=e4f662351f66a1cf726d30653c696b28')
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
                                 json_data['weather'][0]['description'], json_data['weather'][0]['icon'],
                                 int(time.time())))
            conn.commit()
        except pymysql.err.IntegrityError:
            pass
        except:
            print("weather data_base error")
    main()
api_file.close()
