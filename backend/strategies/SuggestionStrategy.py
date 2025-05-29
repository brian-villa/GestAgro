from abc import ABC, abstractmethod
from models.ForecastModel import ForecastModel

class SuggestionStrategy(ABC):
    @abstractmethod
    def get_suggest(self, forecast: ForecastModel) -> dict:
        pass

    def __init__(self, message: str = "", icon: str = "", priority: str = ""):
        self.message = message
        self.icon = icon
        self.priority = priority

    def to_dict(self):
        return {
            "message": self.message,
            "icon": self.icon,
            "priority": self.priority
        }

class WindStrategy(SuggestionStrategy):
    def get_suggest(self, forecast: ForecastModel) -> dict:
        wind_speed = forecast.wind_speed["speed"]

        if wind_speed > 40:
            self.message = "Ventos extremos."
            self.icon = "wi:storm-warning"
            self.priority = 5
        elif wind_speed > 25:
            self.message = "Ventos fortes."
            self.icon = "wi:strong-wind"
            self.priority = 4
        elif wind_speed > 15:
            self.message = "Ventos moderados."
            self.icon = "wi:windy"
            self.priority = 3
        elif wind_speed > 8:
            self.message = "Vento leve"
            self.icon = "wi:wind-beaufort-3"
            self.priority = 2
        else:
            self.message = "Sem vento."
            self.icon = "wi:day-sunny"
            self.priority = 1

        return self.to_dict()    
    
class RainStrategy(SuggestionStrategy):
    def get_suggest(self, forecast) -> dict:
        rain = forecast.rain_probability

        if rain > 80:
            self.message = "Alta probabilidade de chuva."
            self.icon = "wi:rain"
            self.priority = 5
        elif rain > 60:
            self.message = "Possibilidade de chuva."
            self.icon = "wi:showers"
            self.priority = 4
        elif rain > 30:
            self.message = "Chuva pouco provável."
            self.icon = "wi:cloud"
            self.priority = 2
        elif rain > 10:
            self.message = "Baixa chance de chuva."
            self.icon = "wi:day-cloudy"
            self.priority = 2
        else:
            self.message = "Sem previsão de chuva."
            self.icon = "wi:day-sunny"
            self.priority = 1

        return self.to_dict()  

class TemperatureStrategy(SuggestionStrategy):
    def get_suggest(self, forecast: ForecastModel) -> dict:
        temperature = forecast.temperature

        if temperature > 35:
            self.message = "Temperatura muito alta! Risco de insolação."
            self.icon = "wi:hot"
            self.priority = 5
        elif temperature > 25:
            self.message = "Temperatura quente. Use protetor solar."
            self.icon = "wi:day-sunny"
            self.priority = 4
        elif temperature > 10:
            self.message = "Temperatura amena. Condições amenas."
            self.icon = "wi:cloud"
            self.priority = 1
        elif temperature > 0:
            self.message = "Temperatura baixa. Risco de geada em regiões frias."
            self.icon = "wi:snowflake-cold"
            self.priority = 4
        else:
            self.message = "Temperatura muito baixa! Risco de neve."
            self.icon = "wi:snow"
            self.priority = 5
            

        return self.to_dict()

class PrecipitationStrategy(SuggestionStrategy):
    def get_suggest(self, forecast: ForecastModel) -> dict:
        precipitation = forecast.precipitation

        if precipitation > 20:
            self.message = "Chuvas fortes. Evite sair de casa."
            self.icon = "wi:rain"
            self.priority = 5
        elif precipitation > 5:
            self.message = "Chuvas moderadas. Leve guarda chuva."
            self.icon = "wi:showers"
            self.priority = 4
        elif precipitation > 0:
            self.message = "Chuvas leves. Leve um casaco."
            self.icon = "wi:cloud-rain"
            self.priority = 3
        else:
            self.message = "Sem precipitação prevista."
            self.icon = "wi:day-sunny"
            self.priority = 1

        return self.to_dict()
    
class HumidityStrategy(SuggestionStrategy):
        def get_suggest(self, forecast: ForecastModel) -> dict:
            humidity = forecast.humidity

            if humidity > 80:
                self.message = "Umidade muito alta! Pode causar desconforto, sensação de calor e aumentar risco de mofo em casa."
                self.icon = "wi:humidity"
                self.priority = 5
            elif humidity > 60:
                self.message = "Umidade elevada. Mantenha ambientes ventilados."
                self.icon = "wi:day-humidity"
                self.priority = 4
            elif humidity > 40:
                self.message = "Umidade agradável para atividades ao ar livre e conforto respiratório."
                self.icon = "wi:day-sunny"
                self.priority = 1
            elif humidity > 20:
                self.message = "Umidade baixa. Cuidado com ressecamento das vias respiratórias."
                self.icon = "wi:day-cloudy"
                self.priority = 4
            else:
                self.message = "Umidade muito baixa! Hidrate-se bem e use umidificadores para evitar desconforto."
                self.icon = "wi:dry"
                self.priority = 5

            return self.to_dict()

