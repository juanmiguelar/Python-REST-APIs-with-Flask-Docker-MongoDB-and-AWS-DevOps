import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hithere')
def hithere():
    return "hi there"

@app.route('/bye')
def bye():
    return "bye"    

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)