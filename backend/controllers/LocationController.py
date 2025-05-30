from flask import jsonify, request, Blueprint
from models.factories.LocationFactory import LocationFactory
from models.factories.ForecastFactory import ForecastFactory
from strategies.SuggestionStrategy import (
    WindStrategy,
    RainStrategy,
    TemperatureStrategy,
    PrecipitationStrategy,
    HumidityStrategy
)

# Define o blueprint da rota de localização
location_flask = Blueprint("location", __name__)

@location_flask.route("/location", methods=["POST"])
def location():
    """Rota para obter previsões meteorológicas e sugestões baseadas em uma localização.

    Esta rota espera um JSON no corpo da requisição com o nome de um local e, opcionalmente, uma prioridade mínima para filtrar sugestões.

    Corpo da requisição (JSON):

        {
            "place": "Nome do local",
            "priority": 3  # opcional
        }

    Returns:
        JSON: Informações sobre a localização, previsão atual, previsão semanal e sugestões com base em estratégias climáticas.
    """
    data = request.json
    place = data.get("place")
    priority = data.get("priority", 0)

    # Validação: se o campo 'place' não for fornecido
    if not place:
        return jsonify({"error": "Place is required"}), 400
    
    try:
        # Criação dos objetos de localização e previsão
        location = LocationFactory.from_place(place=place)
        forecast = ForecastFactory.dailyForecast(location=location)
        week_forecast = ForecastFactory.weeklyForecast(location=location)

        # Inicializa as estratégias de sugestão
        strategies = [
            WindStrategy(),
            RainStrategy(),
            TemperatureStrategy(),
            PrecipitationStrategy(),
            HumidityStrategy(),
        ]

        # Executa todas as estratégias e filtra sugestões pela prioridade
        suggestions = [
            s for s in (strat.get_suggest(forecast) for strat in strategies)
            if s.get("priority", 0) >= priority
        ]

        # Converte as previsões semanais para dicionário
        daily_forecast = [day.to_dict() for day in week_forecast]

        # Resposta final com todas as informações formatadas
        return jsonify({
            "location": {
                "place": place,
                "latitude": location.latitude,
                "longitude": location.longitude
            },
            "forecast": {
                "date": forecast.date,
                "temperature": forecast.temperature,
                "minTemperature": forecast.minTemperature,
                "maxTemperature": forecast.maxTemperature,
                "humidity": forecast.humidity,
                "precipitation": forecast.precipitation,
                "rain_probability": forecast.rain_probability,
                "wind_speed": forecast.wind_speed
            },
            "daily_forecast": daily_forecast,
            "suggestions": suggestions
        })

    except Exception as e:
        # Em caso de erro inesperado, retorna erro 500 com mensagem
        return jsonify({"error": str(e)}), 500
