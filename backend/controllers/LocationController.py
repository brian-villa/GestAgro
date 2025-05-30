from flask import jsonify, request, Blueprint
from models.factories.LocationFactory import LocationFactory
from models.factories.ForecastFactory import ForecastFactory
from strategies.SuggestionStrategy import WindStrategy, RainStrategy, TemperatureStrategy, PrecipitationStrategy, HumidityStrategy
import threading

location_flask = Blueprint("location", __name__)

@location_flask.route("/location", methods=["POST"])
def location():
    data = request.json
    place = data.get("place")
    priority = data.get("priority", 0)

    if not place:
        return jsonify({"error": "Place is required"}), 400
    
    try:
        location = LocationFactory.from_place(place=place)
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
        daily_forecast = [day.to_dict() for day in week_forecast]


        return jsonify({
            "location": {
                "place": place,
                "latitude": location.latitude,
                "longitude": location.longitude
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
            "daily_forecast": daily_forecast,
            "suggestions": suggestions
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500





