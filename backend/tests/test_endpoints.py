import json
from main import app

def test_forecast_endpoint(mocker):
    client = app.test_client()

    mock_location = mocker.Mock()
    mock_location.latitude = 41.14
    mock_location.longitude = -8.61
    mock_location.place = "Porto"
    mock_location.to_dict.return_value = {
        "latitude": 41.14,
        "longitude": -8.61,
        "place": "Porto"
    }
    
    mock_forecast = mocker.Mock()
    mock_forecast.date = "2025-05-29"
    mock_forecast.temperature = 25.5
    mock_forecast.minTemperature = 20
    mock_forecast.maxTemperature = 30
    mock_forecast.humidity = 60
    mock_forecast.precipitation = 10
    mock_forecast.rain_probability = 50
    mock_forecast.wind_speed = {"speed": 15}
    mock_forecast.to_dict.return_value = {
        "date": "2025-05-29",
        "temperature": 25.5,
        "minTemperature": 20,
        "maxTemperature": 30,
        "humidity": 60,
        "precipitation": 10,
        "rain_probability": 50,
        "wind_speed": {"speed": 15}
    }
    
    mock_week = [mock_forecast for _ in range(7)]

    mocker.patch("models.factories.LocationFactory.LocationFactory.from_lat_lon", return_value=mock_location)
    mocker.patch("models.factories.ForecastFactory.ForecastFactory.dailyForecast", return_value=mock_forecast)
    mocker.patch("models.factories.ForecastFactory.ForecastFactory.weeklyForecast", return_value=mock_week)
    
    res = client.post("/forecast", json={"latitude": 41.14, "longitude": -8.61})
    print(res.data)
    
    assert res.status_code == 200
    assert "forecast" in res.json
    assert "suggestions" in res.json