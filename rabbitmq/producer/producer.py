from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello, this is our first flask website"

@app.route('/one')
def healthcheck():
    return True

@app.route('/two')
def insert():
    return True

@app.route('/three')
def delete():
    return True

@app.route('/four')
def read():
    return True

if __name__ =='__main__':
    app.run(debug = True)