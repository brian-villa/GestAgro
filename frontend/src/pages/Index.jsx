import React, { useState, useEffect } from "react";
import Mapa from "../components/Map";

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

  useEffect(() => {
    // Sequência para ativar fade-in gradualmente ( maneira ideal seria usar propriedade delay do tailwind, porem isso afetaria o hover tbm *aceito sugestoes*)
    setTimeout(() => setFadeInH1(true), 100);      // h1 100ms
    setTimeout(() => setFadeInInput(true), 650);   // input 550ms
    setTimeout(() => setFadeInP(true), 850);       // p 750ms
    setTimeout(() => setFadeInMapa(true), 1050);   // mapa 950ms
  });

  return (
    <div className="flex flex-col items-center h-full w-full">
      <h1
        className={`font-bold text-3xl mb-3 transition-opacity duration-700 ease-in-out cursor-default ${ 
          fadeInH1 ? "opacity-100" : "opacity-0"
        }`}
      >
        {frase}
      </h1>

      <form action="" className="w-full flex justify-center">
        <input
          type="text"
          id="cidadeTxt"
          placeholder="Digite a sua cidade e descubra"
          className={`border-2 rounded-full p-4 w-1/2 mb-3 text-xl transition-all duration-350 ease-in-out
            focus:outline-none focus:scale-103 focus:bg-white/10
            hover:scale-103 hover:bg-white/10 font-extralight ${
              fadeInInput ? "opacity-100" : "opacity-0"
            }`}
        />
      </form>

      <p
        className={`text-2xl text-center font-medium transition-opacity duration-350 ease-in-out cursor-default ${
          fadeInP ? "opacity-100" : "opacity-0"
        }`}
      >
        Ou <br />selecione a sua zona no mapa e nós tratamos do resto!
      </p>

      <div
        className={`w-2/4 h-3/6 border-2 mt-4 rounded-lg shadow-lg transition-all duration-350 ease-in-out hover:scale-108 ${
          fadeInMapa ? "opacity-100" : "opacity-1"
        }`}
      >
        <Mapa />
      </div>
    </div>
  );
}

export default Index;
