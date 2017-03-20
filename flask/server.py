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
    useless,number = path.split("=")
    return render_template('dubikes.html', number=number)


if __name__ == "__main__":
    app.run(debug=True)

