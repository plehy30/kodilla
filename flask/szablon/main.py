from flask import Flask

app = Flask(__name__)
from flask import render_template,request,redirect


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        print("We received GET")
        return render_template("form.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/")
