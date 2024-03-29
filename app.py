from flask import Flask, request
import hashlib

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
