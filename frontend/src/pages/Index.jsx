import React, { useState, useEffect } from "react";
import Mapa from "../components/Map";
import { useNavigate } from 'react-router-dom';

function Index() {
  const frases = [
    "Será que vem chuva por aí?",
    "Vai dar praia hoje?",
    "Devo preparar o guarda-chuva?",
    "Hoje é dia de casaco ou camiseta?",
    "Chuva ou sol no fim de semana?",
    "Céu aberto ou nublado?",
    "Guarda-chuva ou óculos de sol?"
  ];

  const [frase] = useState(() => {
    return frases[Math.floor(Math.random() * frases.length)]; 
  });

  const [fadeInH1, setFadeInH1] = useState(false);
  const [fadeInInput, setFadeInInput] = useState(false);
  const [fadeInP, setFadeInP] = useState(false);
  const [fadeInMapa, setFadeInMapa] = useState(false);
  const [cidade, setCidade] = useState(null);
  const navigate = useNavigate(); 

  useEffect(() => {
    // Sequência para ativar fade-in gradualmente ( maneira ideal seria usar propriedade delay do tailwind, porem isso afetaria o hover tbm *aceito sugestoes*)
    setTimeout(() => setFadeInH1(true), 100);      // h1 100ms
    setTimeout(() => setFadeInInput(true), 650);   // input 550ms
    setTimeout(() => setFadeInP(true), 850);       // p 750ms
    setTimeout(() => setFadeInMapa(true), 1050);   // mapa 950ms
  });

  async function fetchLocationName(cidade) {
    try {
      const response = await fetch("http://localhost:5000/location", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ place: cidade})
      });

      const data = await response.json();
      return data;

    } catch (error) {
      setLocationName("Erro ao buscar local");
      return null;
    } 
  }

  const handleConfirm = async (e) => {
    e.preventDefault();

    const data = await fetchLocationName(cidade);

    if (data) {
      navigate('/forecast', { state: { forecastData: data } });
    }
  };

  return (
    <div className="flex flex-col items-center h-full w-full">
      
      <h1
        className={`font-bold text-center text-3xl mb-3 transition-opacity duration-700 ease-in-out cursor-default ${ 
          fadeInH1 ? "opacity-100" : "opacity-0"
        }`}
      >
        {frase}
      </h1>

      <form onSubmit={handleConfirm} className="w-full flex justify-center">
        <input
          type="text"
          id="cidadeTxt"
          value={cidade || ""}
          onChange={(e) => setCidade(e.target.value)}
          onKeyPress={(e) => {
            if (!/[a-zA-ZÀ-ÿ\s]/.test(e.key)) {
              e.preventDefault();
            }
          }} 
          autoComplete="off"
          placeholder={"Digite a sua cidade e descubra"}
          className={`border-2 text-center rounded-full p-4 w-[80%] sm:w-1/2 mb-3 text-xl transition-all duration-350 ease-in-out
            focus:outline-none focus:scale-103 focus:bg-white/10
            hover:scale-103 hover:bg-white/10 font-extralight ${
              fadeInInput ? "opacity-100" : "opacity-0"
            }`}
        />
      </form>

      <p
        className={`text-2xl w-[95%] text-center font-medium transition-opacity duration-350 ease-in-out cursor-default ${
          fadeInP ? "opacity-100" : "opacity-0"
        }`}
      >
        Ou <br />selecione a sua zona no mapa e nós tratamos do resto!
      </p>

      <div
        className={`w-[80%] sm:w-1/2 h-3/6 border-2 mt-4 rounded-lg shadow-lg transition-all duration-350 ease-in-out hover:scale-108 ${
          fadeInMapa ? "opacity-100" : "opacity-1"
        }`}
      >
        <Mapa />
      </div>
    </div>
  );
}

export default Index;
