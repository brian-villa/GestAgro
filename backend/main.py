from models.LocationModel import Location

def main():
    place = "Aguçadoura"
    location = Location(place)

    print(f"Local: {location.place}")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")  

if __name__ == "__main__":
    main()
