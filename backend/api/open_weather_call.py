import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

from models.ForecastModel import ForecastModel

# Carrega variáveis de ambiente do arquivo .env.local
dotenv_path = Path(__file__).resolve().parents[1] / "env" / ".env.local"
load_dotenv(dotenv_path)

def get_forecast_open_weather(location):
    """
    Obtém a previsão do tempo atual para uma determinada localização usando a API OpenWeather.

    Args:
        location (LocationModel): Objeto contendo latitude e longitude da localização.

    Returns:
        ForecastModel: Objeto contendo os dados da previsão do tempo para o dia atual.
    """
    api_key = os.getenv("API_OPENWEATHER")  # Chave da API do OpenWeather

    # Monta a URL da requisição para previsão atual
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
    except Exception as e:
        # Em caso de erro na requisição, retorna mensagem com erro e código HTTP
        return (f"Erro {e} na requisição: {response.status_code}")
    
    forecast_data = response.json()

    print(forecast_data)  # Para debug, imprime os dados da API

    # Converte o timestamp Unix para objeto datetime
    date = forecast_data["dt"]
    dt_converted = datetime.fromtimestamp(date)

    # Extrai dados do JSON retornado
    temperature = forecast_data["main"]["temp"]
    minTemperature = forecast_data["main"]["temp_min"]
    maxTemperature = forecast_data["main"]["temp_max"]
    humidity = forecast_data["main"]["humidity"]
    precipitation = forecast_data.get("rain", {}).get("1h", 0.0)
    rain_probability = forecast_data.get("clouds", {}).get("all", 0)
    wind_speed = forecast_data.get("wind", {}).get("speed", 0.0)

    location_api = forecast_data["name"]

    # Caso o objeto location não tenha o nome do lugar preenchido, atualiza
    if not location.place:
        location.place = location_api
        

    # Cria e retorna um objeto ForecastModel com os dados extraídos
    forecast = ForecastModel(
        location = location,
        date = dt_converted,
        temperature = temperature,
        minTemperature = minTemperature,
        maxTemperature = maxTemperature,
        humidity = humidity,
        precipitation = precipitation,
        rain_probability = rain_probability,
        wind_speed = wind_speed
    )

    return forecast


def forecast_weekly(location):
    """
    Obtém a previsão do tempo para 7 dias (semana) para uma determinada localização usando a API OpenWeather.

    Args:
        location (LocationModel): Objeto contendo latitude e longitude da localização.

    Returns:
        list[ForecastModel] | str: Lista de objetos ForecastModel contendo a previsão diária para a semana,
                                   ou mensagem de erro em caso de falha na requisição.
    """
    api_key = os.getenv("API_OPENWEATHER")  # Chave da API do OpenWeather

    # Monta a URL da requisição para previsão semanal (7 dias)
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&appid={api_key}&units=metric&cnt=7"

    try:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Garante que o status HTTP seja 200 OK
        except Exception as e:
            return f"Erro ao fazer requisição: {e}"
    
        weekly_data = response.json()

        forecast_list = []

        # Itera sobre a lista de previsões retornada pela API
        for item in weekly_data.get("list", []):
            dt_unix = item.get("dt")
            dt_converted = datetime.fromtimestamp(dt_unix)

            main = item.get("main", {})
            wind = item.get("wind", {})
            clouds = item.get("clouds", {})
            rain = item.get("rain", {})

            # Cria objeto ForecastModel para cada dia da previsão semanal
            forecast = ForecastModel(
                location=location,
                date=dt_converted,
                temperature=main.get("temp", 0.0),
                minTemperature=main.get("temp_min", 0.0),
                maxTemperature=main.get("temp_max", 0.0),
                humidity=main.get("humidity", 0),
                precipitation=rain.get("3h", 0.0),
                rain_probability=clouds.get("all", 0),
                wind_speed=wind.get("speed", 0.0)
            )

            forecast_list.append(forecast)
        return forecast_list
    except Exception as e:
        return f"Erro {e} ao tentar retornar a lista de previsões"
