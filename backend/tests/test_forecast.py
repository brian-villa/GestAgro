from models.factories.LocationFactory import LocationFactory
from models.factories.ForecastFactory import ForecastFactory

def test_daily_forecast_returns_valid_data():
    location = LocationFactory.from_place("São Paulo")
    forecast = ForecastFactory.dailyForecast(location)
    
    assert forecast.temperature is not None
    assert 0 <= forecast.rain_probability <= 100
    assert forecast.date is not None
