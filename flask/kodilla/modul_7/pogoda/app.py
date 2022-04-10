import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/maths/<op>/<int:a>/<int:b>/")
def math(op, a, b):
    if op == "add":
        result = int(a) + int(b)

    return render_template("maths.html", wynik=result)


@app.route("/pogoda/", methods=["GET", "POST"])
def xxx():
    print(request.form)
    miejsce = request.form.get("location")
    location_id = requests.get(f"https://www.metaweather.com/api/location/search/?query={miejsce}")
    location_id = location_id.json()[0]["woeid"]
    response = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    weather = response.json()["consolidated_weather"]

    return render_template("maths.html", wynik=location_id, prognozy=weather)


@app.route("/pogoda/<miejsce>")
def pogoda(miejsce):
    location_id = requests.get(f"https://www.metaweather.com/api/location/search/?query={miejsce}")
    location_id = location_id.json()[0]["woeid"]
    response = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    weather = response.json()["consolidated_weather"]

    return render_template("maths.html", wynik=location_id, prognozy=weather)


if __name__ == '__main__':
    app.run()

    # http://127.0.0.1:5000/maths/add/2/3/
