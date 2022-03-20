import csv
from flask import Flask, request


def get_data_from_nbp_api():
    """1. pobranie danych z API NBP"""
    data = request.get_json("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    ...
    return data


def save_data_to_csv():
    """

    2. Zapisanie do plik CSV
    https://docs.python.org/3/library/csv.html

    """
    data = get_data_from_nbp_api()

    with open("data.csv", "w") as f:
        writer = csv.Writer(f)
        for row in data:
            writer.write()


app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])
# def kalkulator()
#     data = get_data_from_nbp_api()
#     waluty = data[...]
#
#     if request.method == "GET":
#         return render_template("kalkulator.html", waluty=waluty)
#     elif request.method == "POST":
#         waluta = request.POST.get("waluta")
#         kwota = request.POST.get("kwota")
#         wynik =
#         return render_template("kalkulator.html", wynik=wynik)


if __name__ == '__main__':
    app.run()
