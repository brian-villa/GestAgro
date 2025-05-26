from backend.models import LocationModel
import datetime
import uuid

class ForecastModel:
    def __init__(self, location: LocationModel, date, temperature, humidity, precipation, rain_probability):
        self._id = uuid.uuid4()
        self.location = location
        self._date = date
        self._temperature = temperature
        self._humidity = humidity
        self._precipitation = precipation 
        self._rain_probability = rain_probability   