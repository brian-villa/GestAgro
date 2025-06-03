from backend.api.open_weather_call import get_forecast_open_weather, forecast_weekly 
from backend.models.ForecastModel import ForecastModel
from backend.models.ForecastWeekModel import ForecastWeekModel
from backend.models.LocationModel import LocationModel

class ForecastFactory:
    """
    Classe responsável por fornecer previsões do tempo com base em uma localização.

    Esta classe utiliza a API OpenWeather encapsulada em funções auxiliares para
    obter tanto a previsão diária quanto a semanal.
    """

    @staticmethod
    def dailyForecast(location: LocationModel) -> ForecastModel:
        """
        Retorna a previsão diária do tempo para uma determinada localização.

        Args:
            location (LocationModel): Objeto que representa a localização desejada.

        Returns:
            ForecastModel: Objeto contendo os dados da previsão diária do tempo.
        """
        return get_forecast_open_weather(location)

    @staticmethod
    def weeklyForecast(location: LocationModel) -> list[ForecastWeekModel]:
        """
        Retorna a previsão semanal do tempo para uma determinada localização.

        Args:
            location (LocationModel): Objeto que representa a localização desejada.

        Returns:
            list[ForecastWeekModel]: Lista de objetos contendo os dados de previsão para cada dia da semana.
        """
        return forecast_weekly(location)
