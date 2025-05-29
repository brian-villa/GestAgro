from flask import Flask
from controllers.ForecastController import forecast_flask

app = Flask(__name__)
app.register_blueprint(forecast_flask)

if __name__ == "__main__":
    app.run(debug=True)
