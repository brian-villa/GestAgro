from flask import Flask
from flask_cors import CORS
from controllers.ForecastController import forecast_flask
from controllers.LocationController import location_flask

class FlaskAPI:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.app.register_blueprint(forecast_flask)
        self.app.register_blueprint(location_flask)
    
    def run(self):
        self.app.run(debug=True, use_reloader=False, port=5000)
