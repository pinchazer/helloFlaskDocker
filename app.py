from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('im in')
    return 'Hello, M8!'


