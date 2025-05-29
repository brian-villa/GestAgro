from models.LocationModel import LocationModel
from models.ForecastModel import ForecastModel

class ForecastWeekModel:
    def __init__(self, location: LocationModel, forecasts: list[ForecastModel]):
        self._localtion = location
        self._forecasts = forecasts

        