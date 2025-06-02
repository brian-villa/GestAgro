import asyncio
import websockets
import json
from api.body_data import BodyData
from models.factories.LocationFactory import LocationFactory
from models.factories.ForecastFactory import ForecastFactory
from strategies.SuggestionStrategy import WindStrategy, RainStrategy, TemperatureStrategy, PrecipitationStrategy, HumidityStrategy

body_data = BodyData()

class WebSocketServer:
    """
    Classe que implementa um servidor WebSocket para envio contínuo de dados meteorológicos
    e sugestões baseadas em localização e prioridade.

    Args:
        host (str): Endereço onde o servidor irá escutar conexões (default: "localhost").
        port (int): Porta onde o servidor irá escutar conexões (default: 5001).
    """

    def __init__(self, host="localhost", port=5001):
        self._host = host
        self._port = port

    async def send_update(self, websocket):
        """
        Envia periodicamente atualizações com dados de previsão do tempo e sugestões
        para o cliente conectado via websocket.

        Args:
            websocket: conexão websocket ativa.
        """
        while True:
            try:
                # Protege o acesso aos dados compartilhados
                with body_data.lock:
                    location = body_data.location
                    priority = body_data.priority

                # Se não há localização definida, espera 1 segundo e tenta novamente
                if location is None:
                    await asyncio.sleep(1)
                    continue

                # Obtém previsão diária e semanal
                forecast = ForecastFactory.dailyForecast(location=location)
                week_forecast = ForecastFactory.weeklyForecast(location=location)

                # Estratégias para sugestões baseadas na previsão
                strategies = [
                    WindStrategy(),
                    RainStrategy(),
                    TemperatureStrategy(),
                    PrecipitationStrategy(),
                    HumidityStrategy(),
                ]

                # Filtra sugestões por prioridade
                suggestions = [
                    s for s in (strat.get_suggest(forecast) for strat in strategies)
                    if s.get("priority", 0) >= priority
                ]

                # Monta o dicionário com dados para envio
                forecast_data = {
                    "location": {
                        "latitude": location.latitude,
                        "longitude": location.longitude,
                        "place": location.place,
                    },
                    "forecast": {
                        "date": str(forecast.date),
                        "temperature": forecast.temperature,
                        "minTemperature": forecast.minTemperature,
                        "maxTemperature": forecast.maxTemperature,
                        "sunrise": forecast.sunrise.isoformat() if forecast.sunrise else None,
                        "sunset": forecast.sunset.isoformat() if forecast.sunset else None,
                        "humidity": forecast.humidity,
                        "precipitation": forecast.precipitation,
                        "rain_probability": forecast.rain_probability,
                        "wind_speed": forecast.wind_speed
                    },
                    "weekly_forecast": [day.to_dict() for day in week_forecast],
                    "suggestions": suggestions
                }

                # Envia os dados serializados em JSON para o cliente
                await websocket.send(json.dumps(forecast_data))

                # Aguarda 30 segundos para a próxima atualização
                await asyncio.sleep(30)

            except Exception as e:
                # Em caso de erro, envia mensagem de erro e encerra loop
                await websocket.send(json.dumps({"error": str(e)}))
                break

    async def connection(self, websocket):
        """
        Gerencia a conexão websocket com o cliente, recebendo parâmetros iniciais
        e iniciando o envio periódico de atualizações.

        Args:
            websocket: conexão websocket ativa.
        """
        try:
            # Aguarda mensagem JSON do cliente com parâmetros
            message = await websocket.recv()
            payload = json.loads(message)

            # Atualiza dados compartilhados com lock
            with body_data.lock:
                body_data.priority = payload.get("priority", 0)

                if payload.get("type") == "forecast" and "latitude" in payload and "longitude" in payload:
                    body_data.location = LocationFactory.from_lat_lon(payload["latitude"], payload["longitude"])
                elif payload.get("type") == "location" and "place" in payload:
                    body_data.location = LocationFactory.from_place(payload["place"])
                else:
                    await websocket.send(json.dumps({"error": "Parâmetros ausentes place, lat e lon"}))
                    return

            print(f"Cliente conectado. Iniciando envio de dados para {body_data.location.place}")
            # Inicia envio contínuo de atualizações
            await self.send_update(websocket)

        except websockets.ConnectionClosed:
            print("Conexão encerrada")

        except Exception as e:
            print(f"Erro na conexão: {e}")

    def run(self):
        """
        Inicializa e executa o servidor WebSocket assincronamente,
        aceitando conexões no host e porta configurados.
        """
        async def start():
            async with websockets.serve(self.connection, self._host, self._port):
                print(f"Servidor WebSocket rodando em ws://{self._host}:{self._port}")
                await asyncio.Future()  # Mantém o servidor rodando indefinidamente

        asyncio.run(start())
