import React, { useState, useRef, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap, useMapEvents } from 'react-leaflet';
import L from 'leaflet';

function Mapa() {
  const [coords, setCoords] = useState(null);

  function LocationMarker()  
  {useMapEvents({
      click(e) {
        setCoords(e.latlng);
      },
    });

    return null;
  }

  function MarkerWithPopup({ position }) {   {/*Estava enfrentando um erro que fazia o popup nao aparecer junto do marcador*/}
    const markerRef = useRef(null);

    useEffect(() => { 
        markerRef.current.openPopup(); 
    }, [position]);  {/*Agora sempre que o position muda (position = coords) ele usa o useRef para abrir o popup manualmente*/}

    const handleClosePopup = () => {
      markerRef.current.closePopup();  
    };

    return (
      <Marker position={position} ref={markerRef}>
        <Popup>
            <div className='flex flex-col justify-center items-center'>
                <span className='font-extralight'>Você quis dizer:</span>
                <span className='font-bold'> Nome do local </span>
                <div className=' w-full mt-2 flex justify-around'> 
                    <button className='bg-green-600 text-white px-2 py-1 rounded transition-transform transform
                    hover:scale-105 hover:bg-green-500'
                    >
                        Sim!
                    </button>

                    <button className='bg-red-600 text-white px-2 py-1 rounded transition-transform transform
                    hover:scale-105 hover:bg-red-500'
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
      {coords && <MarkerWithPopup position={coords} />} {/*Se coords nao for nulo ele roda o component*/}
    </MapContainer>
  );
}

export default Mapa;
