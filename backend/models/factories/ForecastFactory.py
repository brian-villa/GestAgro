from api.open_weather_call import get_forecast_open_weather, forecast_weekly 
from models.ForecastModel import ForecastModel
from models.ForecastWeekModel import ForecastWeekModel
from models.LocationModel import LocationModel

class ForecastFactory:
    @staticmethod
    def dailyForecast(location: LocationModel) -> ForecastModel:
        return get_forecast_open_weather(location)

    @staticmethod
    def weeklyForecast(location: LocationModel) -> list[ForecastWeekModel]:
        return forecast_weekly(location)