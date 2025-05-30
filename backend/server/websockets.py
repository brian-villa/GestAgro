import asyncio
import websockets
import json
from api.body_data import BodyData
from models.factories.LocationFactory import LocationFactory
from models.factories.ForecastFactory import ForecastFactory
from strategies.SuggestionStrategy import WindStrategy, RainStrategy, TemperatureStrategy, PrecipitationStrategy, HumidityStrategy

body_data = BodyData()

class WebSocketServer:
    def __init__(self, host="localhost", port=5001):
        self._host = host
        self._port = port

    async def send_update(self, websocket):
        while True:
            try:
                with body_data.lock:
                    location = body_data.location
                    priority = body_data.priority

                if location is None:
                    await asyncio.sleep(1)
                    continue

                forecast = ForecastFactory.dailyForecast(location=location)
                week_forecast = ForecastFactory.weeklyForecast(location=location)

                strategies = [
                    WindStrategy(),
                    RainStrategy(),
                    TemperatureStrategy(),
                    PrecipitationStrategy(),
                    HumidityStrategy(),
                ]

                suggestions = [
                    s for s in (strat.get_suggest(forecast) for strat in strategies)
                    if s.get("priority", 0) >= priority
                ]

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
                        "humidity": forecast.humidity,
                        "precipitation": forecast.precipitation,
                        "rain_probability": forecast.rain_probability,
                        "wind_speed": forecast.wind_speed
                    },
                    "weekly_forecast": [day.to_dict() for day in week_forecast],
                    "suggestions": suggestions
                }

                await websocket.send(json.dumps(forecast_data))
                await asyncio.sleep(30)

            except Exception as e:
                await websocket.send(json.dumps({"error": str(e)}))
                break

    async def connection(self, websocket):
        try:
            message = await websocket.recv()
            payload = json.loads(message)

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
            await self.send_update(websocket)

        except websockets.ConnectionClosed:
            print("Conexão encerrada")

        except Exception as e:
            print(f"Erro na conexão: {e}")

    def run(self):
        async def start():
            async with websockets.serve(self.connection, self._host, self._port):
                print(f"Servidor WebSocket rodando em ws://{self._host}:{self._port}")
                await asyncio.Future()  # executa para sempre

        asyncio.run(start())
