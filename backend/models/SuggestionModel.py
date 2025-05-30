from models import ForecastModel
from strategies import SuggestionStrategy

class SuggestionModel:
    """
    Modelo responsável por aplicar uma estratégia de sugestão com base em previsões meteorológicas.

    :param forecasts: Instância de ForecastModel com a previsão do tempo.
    :param strategy: Instância de SuggestionStrategy que define a lógica de sugestão.
    """

    def __init__(self, forecasts: ForecastModel, strategy: SuggestionStrategy):
        """
        Inicializa o modelo com uma previsão e uma estratégia.

        :param forecasts: Previsão meteorológica (ForecastModel).
        :param strategy: Estratégia para gerar sugestões (SuggestionStrategy).
        """
        self._forecast = [forecasts]
        self._strategy = strategy

    def run(self) -> str:
        """
        Executa a estratégia de sugestão com base nas previsões.

        :return: Texto com a sugestão gerada.
        """
        return self._strategy.get_suggest(self._forecast)
