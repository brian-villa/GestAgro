from models.factories.LocationFactory import LocationFactory

def test_from_place():
    """
    Testa se a função from_place cria corretamente um objeto Location a partir do nome do lugar.
    Verifica se a latitude e longitude são retornadas e se o nome do lugar contém 'Porto'.
    """
    location = LocationFactory.from_place("Porto")
    assert location.latitude is not None       # Latitude deve estar definida
    assert location.longitude is not None      # Longitude deve estar definida
    assert "Porto" in location.place            # O nome do local deve conter 'Porto'

def test_from_lat_lon():
    """
    Testa se a função from_lat_lon cria corretamente um objeto Location a partir das coordenadas.
    Verifica se o nome do lugar é retornado e se as coordenadas batem com as passadas (com precisão de 2 casas decimais).
    """
    location = LocationFactory.from_lat_lon(41.14, -8.61)
    assert location.place is not None           # O nome do local deve ser definido
    assert round(location.latitude, 2) == 41.14  # Latitude deve ser próxima do valor passado
    assert round(location.longitude, 2) == -8.61 # Longitude deve ser próxima do valor passado
