from abc import ABC, abstractmethod
from models.ForecastModel import ForecastModel

class SuggestionStrategy(ABC):
    @abstractmethod
    def get_suggest(self, forecast: ForecastModel) -> str:
        pass

class WindStrategy(SuggestionStrategy):
    def get_suggest(self, forecast: ForecastModel) -> str:
        wind = forecast.wind_speed["speed"]

        if wind > 40:
            return "Ventos extremos. Evitar operação."
        elif wind > 25:
            return "Ventos fortes. Verificar estufas e equipamentos."
        elif wind > 15:
            return "Ventos moderados. Adiar pulverizações."
        elif wind > 8:
            return "Vento leve - realizar pulverizações."
        else:
            return "Condições ideais para  qualquer operação agrícola."    
    
class RainStrategy(SuggestionStrategy):
    def get_suggest(self, forecast):
        rain = forecast.rain_probability

        if rain > 80:
            return "Alta probabilidade de chuva. Suspender irrigação e adiar colheitas."
        elif rain > 60:
            return "Possibilidade de chuva. Monitorar o tempo antes de qualquer ação."
        elif rain > 30:
            return "Chuva pouco provável. Operações com cautela"
        elif rain > 10:
            return "Baixa chance de chuva. Boas condições para a maioria das atividades."
        else:
            return "Sem previsão de chuva. Ideal para colheita e preparo de solo"   

class PlantingStrategy(SuggestionStrategy):
    def get_suggest(self, forecast:ForecastModel) -> str:
        temperature = forecast.temperature
        tempMax = 30
        tempMin = 10
        
        if temperature > tempMax:
            return f"Temperatura em {temperature}°C muito alta! Cubra a platação para evitar a perda da plantação por excesso de sol e aumente a frequência de irrigação"
        elif temperature < tempMin:
            return f"Temperatura muito baixa, {temperature}°C! Cubra a plantação, evite o máximo o contacto com o exterior e reduza a irrigação"
        else:
            return f"Condições de temperatura ideias neste momento! Fique atento a outros fatores climáticos"

class HarvestStrategy(SuggestionStrategy):
    def get_suggest(self, forecast: ForecastModel) -> str:
        if forecast.rain_probability > 60 or forecast.precipitation > 5:
            return "Risco de chuva alto. Adiar colheita."
        elif forecast.wind_speed["speed"] > 25:
            return "Vento forte. Evitar colheita."
        elif forecast.temperature < 10:
            return "Temperatura muito baixa. Risco para a colheita"
        else:
            return "Condições ideais para colheita!"