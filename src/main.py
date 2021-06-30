import json
from flask import Flask, request, jsonify
import models as m
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/test'
db = SQLAlchemy(app)


@app.route("/enable")
def enable():
    import pydevd_pycharm
    pydevd_pycharm.settrace('docker.for.mac.localhost', port=500, stdoutToServer=True, stderrToServer=True)
    return "enabled successfully"


@app.route("/test")
def test():
    x = 10
    b = x * 2
    b = b * x + 2
    return str(b)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
