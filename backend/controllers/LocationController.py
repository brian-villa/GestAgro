from flask import jsonify, request, Blueprint
from models.factories.LocationFactory import LocationFactory
from strategies.SuggestionStrategy import WindStrategy, RainStrategy, TemperatureStrategy, PrecipitationStrategy, HumidityStrategy
from api.open_weather_call import get_forecast_open_weather

location_flask = Blueprint("location", __name__)

@location_flask.route("/location", methods=["POST"])
def location():
    data = request.json
    place = data.get("place")

    if not place:
        return jsonify({"error": "Place is required"}), 400
    
    try:
        location = LocationFactory.from_place(place=place)
        forecast = get_forecast_open_weather(location)

        strategies = [
            WindStrategy(),
            RainStrategy(),
            TemperatureStrategy(),
            PrecipitationStrategy(),
            HumidityStrategy(),
        ]

        suggestions = [strat.get_suggest(forecast) for strat in strategies]

        return jsonify({
            "location": {
                "place": place,
                "latitude": location.latitude,
                "longitude": location.longitude
            },
            "forecast": {
                "date": forecast.date,
                "temperature": forecast.temperature,
                "humidity": forecast.humidity,
                "precipitation": forecast.precipitation,
                "rain_probability": forecast.rain_probability,
                "wind_speed": forecast.wind_speed
            },
            "suggestions": suggestions
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500





