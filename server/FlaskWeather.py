from flask import Flask, request
from flask_cors import CORS
from FetchWeather import FetchWeather as fw
from LogWrapper import log_request

app = Flask(__name__)
CORS(app)


@app.route("/")
@log_request
def hello():
    return "Hello, World!"

@app.route("/weather")
@log_request
def search():
    qcity  = request.args.get('city')
    qunits = request.args.get('units')
    return fw(qcity,qunits).fetch()


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)