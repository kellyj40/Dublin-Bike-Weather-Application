#Server.py
from flask import Flask, render_template, request
from data_request import *
app = Flask(__name__)

@app.route('/')
def index():
    db_queries_home = database_queries()
    locations = db_queries_home.get_locations()
    for i in range(len(locations)):
        locations[i]=list(locations[i])
        locations[i][1] = str(locations[i][1]).title()  # converting place names to camel case
    current_data = db_queries_home.current_info()
    weather = db_queries_home.weather_info()

    return render_template('index.html', locations=locations, current_data=current_data, weather=weather)

@app.route('/location')
def location_selection():
    db_queries_locations = database_queries()
    path = request.url
    _, number_of_station = path.split("=")
    name_of_place, most_recent_data, neighbours = db_queries_locations.get_station_name(number_of_station)  # Get name from static
    all_data = most_recent_data[number_of_station]
    day = None
    historical_data_day = db_queries_locations.historical_data_day(number_of_station, day)
    historical_data_week = db_queries_locations.historical_data_week(number_of_station)
    name_of_place = list(name_of_place)
    weather = db_queries_locations.weather_info()
    for i in range(len(name_of_place)):
        name_of_place[i]=str(name_of_place[i]).title() #converting place names to camel case
    return render_template('dubikes.html', name_of_place=name_of_place, all_data=all_data,
                           neighbours=neighbours, historical_data_day=historical_data_day,
                           historical_data_week=historical_data_week, weather=weather)

if __name__ == "__main__":
    app.run(debug=True)