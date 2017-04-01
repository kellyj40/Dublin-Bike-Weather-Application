#Server.py
from flask import Flask, render_template, request
from data_request import *
app = Flask(__name__)

@app.route('/')
def index():
    db_queries_home = database_queries()
    locations = db_queries_home.get_locations()
    current_data = db_queries_home.current_info()
    return render_template('index.html', locations=locations, current_data=current_data)


@app.route('/location')
def location_selection():
    db_queries_locations = database_queries()
    path = request.url
    useless, number_of_station = path.split("=")
    name_of_place = db_queries_locations.get_station_name(number_of_station)
    most_recent_data = db_queries_locations.current_info()
    all_data=most_recent_data[number_of_station]
    return render_template('dubikes.html', name_of_place=name_of_place, all_data=all_data)

# @app.route('/location')
# def location_selection():
#     path = request.url
#     useless, number = path.split("=")
#     name_of_place, all_data = get_info(number)
#     return render_template('dubikes.html', name_of_place=name_of_place, all_data=all_data)

if __name__ == "__main__":
    app.run(debug=True)

