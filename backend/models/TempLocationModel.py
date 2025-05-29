class TempLocationModel:
    def __init__(self, lat, lon):
        self._lat = lat
        self._lon = lon
        self._place = ""

    @property
    def latitude(self):
        return self._lat
    
    @property
    def longitude(self):
        return self._lon
    
    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, new_place):
        self._place = new_place
        
    
    @latitude.setter
    def latitude(self, new_lat):
        self._lat = new_lat
    
    @longitude.setter
    def longitude(self, new_lon):
        self._lon = new_lon
    
    def __str__(self):
         return (f"TempLocationModel(\n"
            f"  Place: '{self._place}'\n"
            f"  Latitude: {self._lat}\n"
            f"  Longitude: {self._lon}\n"
            f")")