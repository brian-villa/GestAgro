from models import LocationModel
import uuid

class ForecastModel:
    def __init__(self, location: LocationModel, date, temperature, humidity, precipitation, rain_probability, wind_speed):
        self._id = uuid.uuid4()
        self.location = location
        self._date = date
        self._temperature = temperature
        self._humidity = humidity
        self._precipitation = precipitation 
        self._rain_probability = rain_probability
        self._wind_speed = wind_speed  

    @property
    def date(self):
        return self._date

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def precipitation(self):
        return self._precipitation

    @property
    def rain_probability(self):
        return self._rain_probability

    @property
    def wind_speed(self):
        return self._wind_speed
    
    def __str__(self):
        return (f"ForecastModel(\n"
                f"  ID: {self._id}\n"
                f"  Location: {self.location}\n"
                f"  Date: {self._date}\n"
                f"  Temperature: {self._temperature}°C\n"
                f"  Humidity: {self._humidity}%\n"
                f"  Precipitation: {self._precipitation}mm\n"
                f"  Rain Probability: {self._rain_probability}%\n"
                f"  Wind Speed: {self._wind_speed}%\n"
                f")")