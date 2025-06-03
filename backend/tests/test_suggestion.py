from strategies.SuggestionStrategy import WindStrategy
from types import SimpleNamespace

def test_strategy_generates_suggestion():
    """
    Testa se a WindStrategy gera uma sugestão válida com base na velocidade do vento no forecast.
    Usa SimpleNamespace para simular um objeto forecast com atributo wind_speed.
    Verifica se a mensagem da sugestão não está vazia e se a prioridade é maior ou igual a 1.
    """
    forecast = SimpleNamespace(wind_speed={"speed": 35})  # Simula forecast com vento forte
    strategy = WindStrategy()                             # Instancia a estratégia de vento
    suggestion = strategy.get_suggest(forecast)          # Gera sugestão
    
    assert suggestion["message"] != ""                    # A mensagem não pode estar vazia
    assert suggestion["priority"] >= 1                    # Prioridade deve ser relevante (>=1)
