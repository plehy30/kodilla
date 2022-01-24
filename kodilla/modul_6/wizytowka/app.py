from flask import Flask, render_template

app = Flask(__name__)


@app.route('/o_mnie')
def ja():  # put application's code here
    return render_template("o_mnie.html")

@app.route('/kontakt')
def kontakt():  # put application's code here
    return render_template("kontakt1.html")


if __name__ == '__main__':
    app.run()
