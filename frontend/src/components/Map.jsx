import React, { useState, useRef, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet';
import { useNavigate } from 'react-router-dom';

function Mapa() {
  const [coords, setCoords] = useState(null);
  const navigate = useNavigate();

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
      markerRef.current.openPopup();
    }, [position]);

    const handleClosePopup = () => {
      markerRef.current.closePopup();
    };

    const handleConfirm = () => {
      navigate('/Previsao'); // redireciona para a página WeatherPage
    };

    return (
      <Marker position={position} ref={markerRef}>
        <Popup>
          <div className="flex flex-col justify-center items-center">
            <span className="font-extralight">Você quis dizer:</span>
            <span className="font-bold"> Nome do local </span>
            <div className="w-full mt-2 flex justify-around">
              <button
                className="bg-green-600 text-white px-2 py-1 rounded transition-transform transform hover:scale-105 hover:bg-green-500"
                onClick={handleConfirm}
              >
                Sim!
              </button>

              <button
                className="bg-red-600 text-white px-2 py-1 rounded transition-transform transform hover:scale-105 hover:bg-red-500"
                onClick={handleClosePopup}
              >
                Não
              </button>
            </div>
          </div>
        </Popup>
      </Marker>
    );
  }

  return (
    <MapContainer
      center={[41.14885307335451, -8.613168053501965]}
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
