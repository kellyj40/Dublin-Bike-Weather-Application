#Server.py
from flask import Flask, render_template
from data_request import *
app = Flask(__name__)



@app.route('/')
def index():
    locations = get_locations()
    return render_template('index.html', locations=locations)

if __name__ == "__main__":
    app.run(debug=True)

