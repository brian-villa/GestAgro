import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

from models.ForecastModel import ForecastModel

dotenv_path = Path(__file__).resolve().parents[1] / "env" / ".env.local"
load_dotenv(dotenv_path)

def get_forecast_open_weather(location):
    api_key = os.getenv("API_OPENWEATHER")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
    except Exception as e:
        return (f"Erro {e} na requisição: {response.status_code}")
    
    forecast_data = response.json()

    print(forecast_data)

    
    date = forecast_data["dt"]
    dt_converted = datetime.fromtimestamp(date)

    temperature = forecast_data["main"]["temp"]
    humidity = forecast_data["main"]["humidity"]
    precipitation = forecast_data.get("rain", {}.get("1h", 0.0))
    rain_probability = forecast_data.get("clouds", {}).get("all", 0)
    wind_speed = forecast_data.get("wind", {}.get("speed", 0.0))

    location_api = forecast_data["name"]

    if not location.place:
        location.place = location_api
        

    #criar objeto Forecast
    forecast = ForecastModel(
        location = location,
        date = dt_converted,
        temperature = temperature,
        humidity = humidity,
        precipitation = precipitation,
        rain_probability = rain_probability,
        wind_speed = wind_speed
    )

    return forecast


