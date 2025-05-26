import requests
import os
import uuid
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(__file__).resolve().parents[1] / "env" / ".env.local"
load_dotenv(dotenv_path)

class Location:
    @staticmethod
    def name_to_geolocation(name, key):
        url = f"https://api.opencagedata.com/geocode/v1/json?q={name}&key={key}"
        response = requests.get(url)
        data = response.json()

        if data["results"]:
            lat = data["results"][0]["geometry"]["lat"]
            lon = data["results"][0]["geometry"]["lng"]
            return lat, lon
        else:
            return f"localização {name} não encontrada"
        
    def __init__(self, place):
        self._id = uuid.uuid4()
        self._place = place
        self._lat = None
        self._lon = None
        self._forecasts = []

        self.set_value()

    @property
    def id(self):
        return self._id

    @property
    def place(self):
        return self._place
    
    @place.setter
    def place(self, new_place):
        if not isinstance(new_place, str) or len(new_place.strip()) == 0:
            return ValueError("Nome não pode ser uma string vazia")
        self._place = new_place
        self.set_value()

    @property
    def latitude(self):
        return self._lat
    
    @property
    def longitude(self):
        return self._lon
    
    def set_value(self):
        key = os.getenv("API_GEOLOCATION")
        if not key:
            return EnvironmentError("chave não definida no arquivo .env")
        
        lat, lon = self.name_to_geolocation(self._place, key)
        self._lat = lat
        self._lon = lon

    

    
        
    