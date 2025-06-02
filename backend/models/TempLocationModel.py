class TempLocationModel:
    """
    Modelo temporário de localização utilizado quando as coordenadas (latitude e longitude)
    já são conhecidas, mas o nome do local ainda não foi definido.

    :param lat: Latitude do local (float).
    :param lon: Longitude do local (float).
    """

    def __init__(self, lat, lon):
        """
        Inicializa a instância de TempLocationModel com latitude e longitude.

        :param lat: Latitude (float).
        :param lon: Longitude (float).
        """
        self._lat = lat
        self._lon = lon
        self._place = ""

    @property
    def latitude(self):
        """
        Retorna a latitude do local.

        :return: Latitude (float).
        """
        return self._lat

    @latitude.setter
    def latitude(self, new_lat):
        """
        Define uma nova latitude.

        :param new_lat: Nova latitude (float).
        """
        self._lat = new_lat

    @property
    def longitude(self):
        """
        Retorna a longitude do local.

        :return: Longitude (float).
        """
        return self._lon

    @longitude.setter
    def longitude(self, new_lon):
        """
        Define uma nova longitude.

        :param new_lon: Nova longitude (float).
        """
        self._lon = new_lon

    @property
    def place(self):
        """
        Retorna o nome do local (caso tenha sido definido).

        :return: Nome do local (string).
        """
        return self._place

    @place.setter
    def place(self, new_place):
        """
        Define o nome do local.

        :param new_place: Novo nome (string).
        """
        self._place = new_place

    def __str__(self):
        """
        Retorna uma representação formatada da instância TempLocationModel.

        :return: String formatada com os dados do local.
        """
        return (f"TempLocationModel(\n"
                f"  Place: '{self._place}'\n"
                f"  Latitude: {self._lat}\n"
                f"  Longitude: {self._lon}\n"
                f")")
