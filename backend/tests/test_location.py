from models. factories.LocationFactory import LocationFactory

def test_from_place():
    location = LocationFactory.from_place("Porto")
    assert location.latitude is not None
    assert location.longitude is not None
    assert "Porto" in location.place

def test_from_lan_lon():
    location = LocationFactory.from_lat_lon(41.14, -8.61)
    assert location.place is not None
    assert round(location.latitude, 2) == 41.14
    assert round(location.longitude, 2) == -8.61

    