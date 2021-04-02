from flask import Flask



app = Flask(__name__)



@app.route('/')
def hello():
    return "Hello World!"
@app.route('/epsi')
def hello_epsi ():
    return "epsi is the best"
f __name__ == '__main__':
    app.run()