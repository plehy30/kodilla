from flask import Flask

app = Flask(__name__)

@app.route('/blog/<id>')
def blog(id):
    return f'This is blog entry #{id}'