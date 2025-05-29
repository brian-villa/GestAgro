from models.LocationModel import LocationModel
from models.TempLocationModel import TempLocationModel

class LocationFactory:
    @staticmethod
    def from_place(place: str):
        return LocationModel(place)
        
    @staticmethod
    def from_lat_lon(lat, lon):
        return TempLocationModel(lat, lon)