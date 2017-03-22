#Server.py
from flask import Flask, render_template, request
from data_request import *
app = Flask(__name__)

@app.route('/')
def index():
    locations = get_locations()
    return render_template('index.html', locations=locations)

@app.route('/location')
def location_selection():
    path = request.url
    useless, number = path.split("=")
    name_of_place, all_data = get_info(number)
    return render_template('dubikes.html', name_of_place=name_of_place, all_data=all_data)


# if __name__ == "__main__":
#     app.run(debug=True)

