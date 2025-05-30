from strategies.SuggestionStrategy import WindStrategy
from types import SimpleNamespace

def test_strategy_generates_suggestion():
    forecast = SimpleNamespace(wind_speed={"speed": 35})
    strategy = WindStrategy()
    suggestion = strategy.get_suggest(forecast)
    
    assert suggestion["message"] != ""
    assert suggestion["priority"] >= 1
