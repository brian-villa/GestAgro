# from models.LocationModel import LocationModel
# from api import open_weather_call
# from strategies.SuggestionStrategy import WindStrategy, RainStrategy, TemperatureStrategy, HumidityStrategy, PrecipitationStrategy
# from models.SuggestionModel import SuggestionModel
from flask import Flask
from controllers.ForecastController import forecast_flask
from controllers.LocationController import location_flask

# def main():
#     place = "Braga"
#     location = LocationModel(place)

#     print(f"Local: {location.place}")
#     print(f"Latitude: {location.latitude}")
#     print(f"Longitude: {location.longitude}") 

#     forecast = open_weather_call.get_forecast_open_weather(location) 
#     print(forecast)

#     strategies = [
#         ("Vento", WindStrategy()),
#         ("Chuva", RainStrategy()),
#         ("Temperatura", TemperatureStrategy()),
#         ("Humidade", HumidityStrategy()),
#         ("Precipitação", PrecipitationStrategy())
#     ]

#     for name, strategy in strategies:
#         suggestion = SuggestionModel(forecast, strategy)
#         result = suggestion.run()
#         print(f"\n{name}: {result}")

# if __name__ == "__main__":
#     main()


app = Flask(__name__)
app.register_blueprint(forecast_flask)
app.register_blueprint(location_flask)

if __name__ == "__main__":
    app.run(debug=True)

