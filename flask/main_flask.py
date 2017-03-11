from flask import Flask, render_template
app = Flask(__name__)

#Multiple urls for single function, so homepage changes depending on whether they are logged in or not
@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("dubikes.html", user=user)

@app.route("/locations")
def locations():
    places = ["Connolly", "Grafton", "Newbridge", "kildare is part of the pale"]
    return render_template("locations.html", places=places)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
