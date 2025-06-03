from flask import jsonify, request, Blueprint
from backend.models.factories.LocationFactory import LocationFactory
from backend.models.factories.ForecastFactory import ForecastFactory
from backend.strategies.SuggestionStrategy import (
    WindStrategy,
    RainStrategy,
    TemperatureStrategy,
    PrecipitationStrategy,
    HumidityStrategy
)


# Define o blueprint da rota de previsão
forecast_flask = Blueprint("forecast", __name__)

@forecast_flask.route("/forecast", methods=["POST"])
def forecast():
    """

    Rota para obter a previsão do tempo com base em latitude e longitude.

    Esta rota espera um JSON com os dados de latitude, longitude e uma prioridade mínima para sugestões.

    Corpo da requisição (JSON):

    {
    "latitude": float,
    "longitude": float,
    "priority": int (opcional)
    }

    Returns:
        JSON: Contém informações sobre a localização, previsão diária, previsão semanal e sugestões baseadas nas condições climáticas.

    """
    
    data = request.json
    lat = data.get("latitude")
    lon = data.get("longitude")
    priority = data.get("priority", 0)

    # Validação: latitude e longitude são obrigatórios
    if lat is None or lon is None:
        return jsonify({"error": "Latitude e Longitude estão vazios"}), 400

    try:
        # Criação do modelo de localização a partir de latitude e longitude
        location = LocationFactory.from_lat_lon(lat=lat, lon=lon)

        # Obtém a previsão do dia e a semanal
        forecast = ForecastFactory.dailyForecast(location=location)
        week_forecast = ForecastFactory.weeklyForecast(location=location)

        # Define as estratégias de sugestão baseadas no clima
        strategies = [
            WindStrategy(),
            RainStrategy(),
            TemperatureStrategy(),
            PrecipitationStrategy(),
            HumidityStrategy(),
        ]

        # Executa cada estratégia e filtra as sugestões com base na prioridade mínima
        suggestions = [
            s for s in (strat.get_suggest(forecast) for strat in strategies)
            if s.get("priority", 0) >= priority
        ]

        # Converte a previsão semanal em uma lista de dicionários
        weekly_forecast = [day.to_dict() for day in week_forecast]

        # Retorna a resposta JSON com os dados coletados e processados
        return jsonify({
            "location": {
                "latitude": location.latitude,
                "longitude": location.longitude,
                "place": location.place
            },
            "forecast": {
                "date": forecast.date,
                "temperature": forecast.temperature,
                "minTemperature": forecast.minTemperature,
                "maxTemperature": forecast.maxTemperature,
                "humidity": forecast.humidity,
                "precipitation": forecast.precipitation,
                "rain_probability": forecast.rain_probability,
                "wind_speed": forecast.wind_speed,
                "sunrise": forecast.sunrise.isoformat() if forecast.sunrise else None,
                "sunset": forecast.sunset.isoformat() if forecast.sunset else None
            },

            "weekly_forecast": weekly_forecast,
            "suggestions": suggestions
        })

    except Exception as e:
        # Em caso de erro, retorna código 500 com a mensagem da exceção
        return jsonify({"error": str(e)}), 500