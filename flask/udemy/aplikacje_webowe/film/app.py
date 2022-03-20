from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return '<h1>We are programmers</h1>'


@app.route('/cantor/<string:currency>/<int:amount>')
def cantor(currency, amount):
    message = f"<h1> You selected {currency} and amount {amount}</h1>"
    return message


@app.route('/exchange')
def exchange():

    body: '''
        <form id="exchange_form" action="/exchange_process" method="POST">
            <label for="currency">Currency</label>
            <input type="text" id="currency" name="currency" value="EUR"><br>
            <label for="amount">Amount</label>
            <input type="text" id="amount" name="amount" value="100"><br>
            <input type="submit" value="Send">
        </form>
        
    '''
    return body


@app.route('/exchange_process', methods=['POST'])
def exchange_process():

    currency = "EUR"
    if "currency" in request.form:
        currency = request.form["currency"]

    amount = 100
    if "amount" in request.form:
        amount = request.form["amount"]

    body = f'You want to exchange {amount} {currency}'

    return body


if __name__ == '__main__':
    app.run()
