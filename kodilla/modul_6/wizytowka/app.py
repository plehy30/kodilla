from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/o_mnie')
def ja():  # put application's code here
    return render_template("o_mnie.html")


@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():  # put application's code here

    request.method == 'POST'
    print(f'Otrzymaliśmy wiadomość: {request.form}')
    return render_template("kontakt.html")
    # if request.method == 'GET':
    #     print("We received GET")
    #     return render_template("kontakt.html")
    # elif request.method == 'POST':
    #     print("We received POST")
    #     print(request.form)
    #     return redirect("/")



