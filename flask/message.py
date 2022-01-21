from flask import Flask

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def post_message():
    return "OK"