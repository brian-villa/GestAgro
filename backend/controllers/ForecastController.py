from flask import jsonify, request, Blueprint
from models.ForecastModel import ForecastModel
from models.factories.LocationFactory import LocationFactory
from api.open_weather_call import get_forecast_open_weather

forecast_flask = Blueprint("forecast", __name__)

@forecast_flask.route("/forecast", methods=["POST"])
def forecast():
    data = request.json
    lat = data.get("latitude")
    lon = data.get("longitude")

    if lat is None or lon is None:
        return jsonify({"error": "Latitude e Longitude estão vazios"}), 400
    
    try:
        location = LocationFactory.from_lat_lon(lat=lat, lon=lon)
        forecast = get_forecast_open_weather(location=location)

        return jsonify({
            "location": {
                "latitude": location.latitude,
                "longitude": location.longitude,
                "place": location.place
            },
            "forecast": {
                "date": forecast.date,
                "temperature": forecast.temperature,
                "humidity": forecast.humidity,
                "precipitation": forecast.precipitation,
                "rain_probability": forecast.rain_probability,
                "wind_speed": forecast.wind_speed
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
