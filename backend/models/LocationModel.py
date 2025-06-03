import requests
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(__file__).resolve().parents[1] / "env" / ".env.local"
load_dotenv(dotenv_path)

class LocationModel:
    """
    Modelo que representa uma localização geográfica, com base no nome do lugar.
    A latitude e longitude são obtidas por meio da API OpenCage.

    :param place: Nome da localidade para a qual se deseja obter coordenadas.
    """

    @staticmethod
    def name_to_geolocation(name, key):
        """
        Converte o nome de uma localidade em coordenadas geográficas (latitude e longitude)
        utilizando a API do OpenCage.

        :param name: Nome da localidade (string).
        :param key: Chave de API do OpenCage (string).
        :return: Tupla (latitude, longitude) ou mensagem de erro (string).
        """
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
        """
        Inicializa a instância de LocationModel, buscando automaticamente
        a latitude e longitude correspondentes ao lugar fornecido.

        :param place: Nome da localidade.
        """
        self._place = place
        self._lat = None
        self._lon = None

        self.set_value()

    @property
    def place(self):
        """
        Retorna o nome da localidade.

        :return: Nome do local (string).
        """
        return self._place
    
    @place.setter
    def place(self, new_place):
        """
        Define um novo nome de localidade e atualiza suas coordenadas geográficas.

        :param new_place: Novo nome do local.
        :raises ValueError: Se o nome fornecido for inválido.
        """
        if not isinstance(new_place, str) or len(new_place.strip()) == 0:
            raise ValueError("É preciso um lugar para obter uma previsão do tempo!")
        self._place = new_place
        self.set_value()

    @property
    def latitude(self):
        """
        Retorna a latitude do local.

        :return: Latitude (float).
        """
        return self._lat
    
    @property
    def longitude(self):
        """
        Retorna a longitude do local.

        :return: Longitude (float).
        """
        return self._lon
    
    def set_value(self):
        """
        Atualiza latitude e longitude com base no nome da localidade atual.

        :raises EnvironmentError: Se a chave da API não estiver definida.
        """
        key = os.getenv("API_GEOLOCATION")
        if not key:
            raise EnvironmentError("Chave não definida no arquivo .env")
        
        lat, lon = self.name_to_geolocation(self._place, key)
        self._lat = lat
        self._lon = lon
    
    def __str__(self):
        """
        Retorna uma representação formatada da instância LocationModel.

        :return: String formatada com os dados da localização.
        """
        return (f"LocationModel(\n"
                f"  Place: '{self._place}'\n"
                f"  Latitude: {self._lat}\n"
                f"  Longitude: {self._lon}\n"
                f")")
