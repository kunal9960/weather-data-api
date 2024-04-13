import pandas
from flask import Flask, render_template

app = Flask("Website")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/<station>/<date>/")
def about(station, date):
    temperature = 23
    return {"Station": station,
            "Date": date,
            "Temperature": temperature}


app.run(debug=True)
