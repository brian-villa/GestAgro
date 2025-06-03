
from backend.main import main

def test_forecast_endpoint(mocker):
    """
    Testa o endpoint '/forecast' da API Flask.

    Utiliza mocks para simular a criação de objetos Location e Forecast,
    evitando chamadas reais à API externa ou à base de dados.

    Args:
        mocker: fixture do pytest-mock para aplicar mocks.
    """

    # Cria cliente de teste do Flask para simular requisições HTTP
    client = main.test_client()

    # Cria mock do objeto Location com atributos simulados
    mock_location = mocker.Mock()
    mock_location.latitude = 41.14
    mock_location.longitude = -8.61
    mock_location.place = "Porto"
    mock_location.to_dict.return_value = {
        "latitude": 41.14,
        "longitude": -8.61,
        "place": "Porto"
    }
    
    # Cria mock do objeto Forecast com dados simulados
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
    
    # Lista simulada de previsão semanal com 7 elementos iguais ao mock_forecast
    mock_week = [mock_forecast for _ in range(7)]

    # Substitui as funções da fábrica para retornar os mocks criados
    mocker.patch("models.factories.LocationFactory.LocationFactory.from_lat_lon", return_value=mock_location)
    mocker.patch("models.factories.ForecastFactory.ForecastFactory.dailyForecast", return_value=mock_forecast)
    mocker.patch("models.factories.ForecastFactory.ForecastFactory.weeklyForecast", return_value=mock_week)
    
    # Faz requisição POST ao endpoint /forecast com dados de latitude e longitude
    res = client.post("/forecast", json={"latitude": 41.14, "longitude": -8.61})

    # Imprime a resposta para debug
    print(res.data)
    
    # Verifica se o status HTTP é 200 (OK)
    assert res.status_code == 200

    # Verifica se o JSON de resposta contém a chave 'forecast'
    assert "forecast" in res.json

    # Verifica se o JSON de resposta contém a chave 'suggestions'
    assert "suggestions" in res.json
