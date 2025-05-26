from models import ForecastModel

class SuggestionModel:
    def __init__(self, forecast: ForecastModel, action_suggest):
        self._forecast = forecast
        self._action_suggest = action_suggest
        