from models.LocationModel import LocationModel
from models.ForecastModel import ForecastModel

class ForecastWeekModel:
    """
    Representa a previsão do tempo para uma semana em uma determinada localização.

    :param location: Instância de LocationModel representando a localização da previsão.
    :param forecasts: Lista de ForecastModel com as previsões diárias da semana.
    """

    def __init__(self, location: LocationModel, forecasts: list[ForecastModel]):
        """
        Inicializa a instância de ForecastWeekModel com a localização e lista de previsões.

        :param location: Localização da previsão.
        :param forecasts: Lista das previsões diárias (objetos ForecastModel).
        """
        self._localtion = location
        self._forecasts = forecasts
