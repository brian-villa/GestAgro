from models import ForecastModel
from strategies import SuggestionStrategy

class SuggestionModel:
    def __init__(self, forecasts: ForecastModel, strategy: SuggestionStrategy):
        self._forecast = [forecasts]
        self._strategy = strategy

    def run(self) -> str:
        return self._strategy.get_suggest(self._forecast)