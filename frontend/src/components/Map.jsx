import React, { useState, useRef, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet';
import { useNavigate } from 'react-router-dom';

function Mapa() {
  const [coords, setCoords] = useState(null);
  const [locationName, setLocationName] = useState(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

 
  useEffect(() => {  // Busca o nome do local quando coordenadas mudarem (useEffect)
    if (coords) {
      fetchLocationName(coords.lat, coords.lng);
    }
  }, [coords]);

  const [forecastData, setForecastData] = useState(null); 

  async function fetchLocationName(lat, lng) {
    setLoading(true);

    try {
      const response = await fetch("http://localhost:5000/forecast", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ latitude: lat, longitude: lng })
      });

      const data = await response.json();
      setForecastData(data); 
      setLocationName(data.location?.place);
    } catch (error) {
      setLocationName("Erro ao buscar local");
    } finally {
      setLoading(false);
    }
  }

  function LocationMarker() {
    useMapEvents({
      click(e) {
        setCoords(e.latlng);
      },
    });
    return null;
  }

  function MarkerWithPopup({ position }) {
    const markerRef = useRef(null);

    useEffect(() => {
      if (markerRef.current) {
        markerRef.current.openPopup();
      }
    }, [position]);

    const handleClosePopup = () => {
      markerRef.current.closePopup();
    };

  const handleConfirm = () => {
    navigate('/forecast', { state: { forecastData} }); //vai pra pagina previsao e armazena os dados do backend 
  };


    return (
      <Marker position={position} ref={markerRef}>
        <Popup>
          <div className="flex flex-col justify-center items-center">
            <span className="font-extralight">Você quis dizer:</span>
            <span className="font-bold">
              {loading ? "Carregando..." : locationName}
            </span>
            <div className="w-full mt-2 flex justify-around">
              <button
                className="bg-green-600 text-white px-2 py-1 rounded cursor-pointer transition-transform transform hover:scale-105 hover:bg-green-500 disabled:opacity-50"
                onClick={handleConfirm}
                disabled={loading}  // se loading verdadeiro ele fica disabled
              >
                Sim!
              </button>

              <button
                className="bg-red-600 text-white px-2 py-1 rounded cursor-pointer transition-transform transform hover:scale-105 hover:bg-red-500 disabled:opacity-50"
                onClick={handleClosePopup}
                disabled={loading}  // se loading verdadeiro ele fica disabled
              >
                Não.
              </button>
            </div>
          </div>
        </Popup>
      </Marker>
    );
  }

  return (
    <MapContainer
      center={[41.14885307335451, -8.613168053501965]} // localizacao do porto
      zoom={11}
      className="w-full h-full rounded-lg"
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; OpenStreetMap contributors"
      />
      <LocationMarker />
      {coords && <MarkerWithPopup position={coords} />}
    </MapContainer>
  );
}

export default Mapa;
