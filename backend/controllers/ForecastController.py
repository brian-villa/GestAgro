from flask import jsonify, request, Blueprint
from models.factories.LocationFactory import LocationFactory
from models.factories.ForecastFactory import ForecastFactory
from strategies.SuggestionStrategy import WindStrategy, RainStrategy, TemperatureStrategy, PrecipitationStrategy, HumidityStrategy
import threading
import os
import requests

forecast_flask = Blueprint("forecast", __name__)

@forecast_flask.route("/forecast", methods=["POST"])
def forecast():
    data = request.json
    lat = data.get("latitude")
    lon = data.get("longitude")
    priority = data.get("priority", 0)

    if lat is None or lon is None:
        return jsonify({"error": "Latitude e Longitude estão vazios"}), 400
    
    try:
        location = LocationFactory.from_lat_lon(lat=lat, lon=lon)
        forecast = ForecastFactory.dailyForecast(location=location)
        week_forecast = ForecastFactory.weeklyForecast(location=location)

        strategies = [
            WindStrategy(),
            RainStrategy(),
            TemperatureStrategy(),
            PrecipitationStrategy(),
            HumidityStrategy(),
        ]

        suggestions = [
            s for s in (strat.get_suggest(forecast) for strat in strategies)
            if s.get("priority", 0) >= priority
        ]
        weekly_forecast = [day.to_dict() for day in week_forecast]

        

        return jsonify({
            "location": {
                "latitude": location.latitude,
                "longitude": location.longitude,
                "place": location.place
            },
            "forecast": {
                "date": forecast.date,
                "temperature": forecast.temperature,
                "minTemperature": forecast.minTemperature,
                "maxTemperature": forecast.maxTemperature,
                "humidity": forecast.humidity,
                "precipitation": forecast.precipitation,
                "rain_probability": forecast.rain_probability,
                "wind_speed": forecast.wind_speed
            },
            "weekly_forecast": weekly_forecast,
            "suggestions": suggestions
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    