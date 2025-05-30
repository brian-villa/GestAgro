from models.factories.LocationFactory import LocationFactory
from models.factories.ForecastFactory import ForecastFactory

def test_daily_forecast_returns_valid_data():
    """
    Testa se a função dailyForecast retorna dados válidos para uma determinada localização.

    O teste verifica se:
    - A temperatura retornada não é None
    - A probabilidade de chuva está no intervalo esperado (0 a 100%)
    - A data da previsão não é None
    """

    # Cria um objeto Location a partir do nome do lugar "Porto"
    location = LocationFactory.from_place("Porto")
    
    # Obtém a previsão diária para a localização criada
    forecast = ForecastFactory.dailyForecast(location)
    
    # Verifica se a temperatura está presente (não é None)
    assert forecast.temperature is not None
    
    # Verifica se a probabilidade de chuva está entre 0 e 100
    assert 0 <= forecast.rain_probability <= 100
    
    # Verifica se a data da previsão está presente (não é None)
    assert forecast.date is not None
