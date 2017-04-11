#Server.py
from flask import Flask, render_template, request
from data_request import *
app = Flask(__name__)
import location_request

@app.route('/')
def index():
    db_queries_home = database_queries()
    locations = db_queries_home.get_locations()
    current_data = db_queries_home.current_info()
    weather = db_queries_home.weather_info()

    return render_template('index.html', locations=locations, current_data=current_data, weather=weather)


@app.route('/test')
def test():
    df = location_request.test_pandas()
    print(df)

@app.route('/location')
def location_selection():
    db_queries_locations = database_queries()
    path = request.url
    _, number_of_station = path.split("=")
    name_of_place, most_recent_data, neighbours = db_queries_locations.get_station_name(number_of_station)  # Get name from static
    all_data = most_recent_data[number_of_station]
    day = None
    historical_data = db_queries_locations.historical_data(number_of_station, day)
    name_of_place = list(name_of_place)
    place_lower = name_of_place[1]
    name_of_place[1] = place_lower.lower()
    return render_template('dubikes.html', name_of_place=name_of_place, all_data=all_data, neighbours=neighbours, historical_data=historical_data)

# @app.route('/location')
# def location_selection():
#     path = request.url
#     useless, number = path.split("=")
#     name_of_place, all_data = get_info(number)
#     return render_template('dubikes.html', name_of_place=name_of_place, all_data=all_data)

if __name__ == "__main__":
    app.run(debug=True)

