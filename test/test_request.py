import scrapper
from nose.tools import *
#from nose.tools import assert_not_equal
from scrapper import *


def test_requests():
    # this function tests that we are getting a response from the api, and that the response is in the format that we expect
    data = request()
    eq_(type(data), list, "json format not correct")
    eq_(type(data[0]), dict, "dictionary format not correct")


def test_RDS():
    # this test checks that the type of 'conn' is a successful pymysql connection
    conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                           password='goodchat', db='DublinBikes')
    eq_(type(conn), pymysql.connections.Connection, "no database connected")


def test_sql():
    # test that we can access  data from the RDS database using SQL selection queries
    conn = pymysql.connect(host='dublinbikes.clbms7pd8xjt.us-west-2.rds.amazonaws.com', user='goodchat',
                           password='goodchat', db='DublinBikes')
    cur = conn.cursor()
    cur.execute("""SELECT name From Bike_Data WHERE number = 1 AND last_update = 1489622323000;""")
    for row in cur.fetchall():
        eq_(row[0], 'CHATHAM STREET', 'Data not correct')
    conn.close()


def test_json_dictionary():
    # test that we can correctly access the json data using the syntax of a python dictionary
    data = request()
    eq_(data[0]['name'], 'SMITHFIELD NORTH', "data not correct")
    assert_not_equal(data[0]['number'], 87, "data not correct")
    eq_(data[1]['position']['lat'], 53.353462, "data not correct")
    eq_(data[2]['number'], 32, "data not correct")

