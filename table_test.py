# import pymysql
# def extract(x):
#     x = x.strip("{}")
#     number, name, address = x.split( )
#     number, name = number.strip(","), name.strip(",")
#     _, number = number.split(":")
#     _, name = name.split(":")
#     _, address = address.split(":")
#     return[int(number), name, address]
#
# fake_json = '{"number":1211345, "name":John, "address":ucd}'
# var = extract(fake_json)
# conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user = 'goodchat', password = 'goodchat', db = 'DublinBikes')
#
# cur = conn.cursor()
# query = """INSERT INTO Bike_Data(number, name, address) VALUES ("%s","%s","%s");"""
# cur.execute(query % (var[0],var[1],var[2]))
# conn.commit()
# # for row in cur.fetchall():
# #     print(row[0])
#
# conn.close()
#
