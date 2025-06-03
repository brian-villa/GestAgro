from backend.models.LocationModel import LocationModel
from backend.models.TempLocationModel import TempLocationModel

class LocationFactory:
    """
    Fábrica para criação de objetos de localização.

    Esta classe fornece métodos estáticos para instanciar objetos de localização
    com base em diferentes tipos de entrada (nome do local ou coordenadas).
    """

    @staticmethod
    def from_place(place: str) -> LocationModel:
        """
        Cria um objeto LocationModel a partir do nome de um local.

        Args:
            place (str): Nome do local (ex: "Porto").

        Returns:
            LocationModel: Instância representando a localização fornecida.
        """
        return LocationModel(place)
        
    @staticmethod
    def from_lat_lon(lat: float, lon: float) -> TempLocationModel:
        """
        Cria um objeto TempLocationModel a partir de coordenadas geográficas.

        Args:
            lat (float): Latitude da localização.
            lon (float): Longitude da localização.

        Returns:
            TempLocationModel: Instância representando a localização temporária com coordenadas.
        """
        return TempLocationModel(lat, lon)
