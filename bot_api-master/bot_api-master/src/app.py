from flask import Flask
from flask_restful import Api
from .scraper.main import Scraper

app = Flask(__name__)
api = Api(app)

BASE_PATH = "/api/v1"

api.add_resource(Scraper, BASE_PATH)

if __name__ == '__main__':
    app.run(debug=True)