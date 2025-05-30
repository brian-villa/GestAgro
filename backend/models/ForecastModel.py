from models import LocationModel
import uuid

class ForecastModel:
    """
    Representa a previsão do tempo para uma determinada localização e data.

    :param location: Instância de LocationModel representando a localização da previsão.
    :param date: Data da previsão (objeto datetime ou string).
    :param temperature: Temperatura média prevista (float ou int).
    :param minTemperature: Temperatura mínima prevista.
    :param maxTemperature: Temperatura máxima prevista.
    :param humidity: Umidade relativa do ar (%).
    :param precipitation: Quantidade de precipitação prevista (mm).
    :param rain_probability: Probabilidade de chuva (%).
    :param wind_speed: Velocidade do vento (unidade conforme especificado).
    """

    def __init__(self, location: LocationModel, date, temperature, minTemperature, maxTemperature, humidity, precipitation, rain_probability, wind_speed):
        """
        Inicializa uma instância de ForecastModel com os dados da previsão.

        :param location: Localização da previsão.
        :param date: Data da previsão.
        :param temperature: Temperatura média.
        :param minTemperature: Temperatura mínima.
        :param maxTemperature: Temperatura máxima.
        :param humidity: Umidade relativa.
        :param precipitation: Precipitação em mm.
        :param rain_probability: Probabilidade de chuva.
        :param wind_speed: Velocidade do vento.
        """
        self.location = location
        self._date = date
        self._temperature = temperature
        self._minTemperature = minTemperature
        self._maxTemperature = maxTemperature
        self._humidity = humidity
        self._precipitation = precipitation 
        self._rain_probability = rain_probability
        self._wind_speed = wind_speed  

    @property
    def date(self):
        """Retorna a data da previsão."""
        return self._date

    @property
    def temperature(self):
        """Retorna a temperatura média prevista."""
        return self._temperature
    
    @property
    def minTemperature(self):
        """Retorna a temperatura mínima prevista."""
        return self._minTemperature
    
    @property
    def maxTemperature(self):
        """Retorna a temperatura máxima prevista."""
        return self._maxTemperature

    @property
    def humidity(self):
        """Retorna a umidade relativa do ar prevista (%)."""
        return self._humidity

    @property
    def precipitation(self):
        """Retorna a quantidade de precipitação prevista (mm)."""
        return self._precipitation

    @property
    def rain_probability(self):
        """Retorna a probabilidade de chuva prevista (%)."""
        return self._rain_probability

    @property
    def wind_speed(self):
        """Retorna a velocidade do vento prevista."""
        return self._wind_speed
    
    def to_dict(self):
        """
        Converte o objeto ForecastModel em um dicionário.

        :return: Dicionário com os dados da previsão.
        """
        return {
            "date": self.date.isoformat() if hasattr(self.date, 'isoformat') else self.date,
            "temperature": self.temperature,
            "minTemperature": self.minTemperature,
            "maxTemperature": self.maxTemperature,
            "humidity": self.humidity,
            "precipitation": self.precipitation,
            "rain_probability": self.rain_probability,
            "wind_speed": self.wind_speed,
        }
    
    def __str__(self):
        """
        Representação em string formatada da previsão.

        :return: String com os dados da previsão formatados.
        """
        return (f"ForecastModel(\n"
                f"  Location: {self.location}\n"
                f"  Date: {self._date}\n"
                f"  Temperature: {self._temperature}°C\n"
                f"  Min Temperature: {self._minTemperature}°C\n"
                f"  Max Temperature: {self._maxTemperature}°C\n"
                f"  Humidity: {self._humidity}%\n"
                f"  Precipitation: {self._precipitation}mm\n"
                f"  Rain Probability: {self._rain_probability}%\n"
                f"  Wind Speed: {self._wind_speed}\n"
                f")")
