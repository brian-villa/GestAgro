import React from "react";
import { Icon } from '@iconify/react';
import { useLocation } from "react-router-dom";

function WeatherPage(){

    const location = useLocation();
    const data = location.state?.forecastData;

    console.log("Dados recebidos:", data);

    return (
        <>
            <form action="" className="w-full flex justify-center">
                <input
                    type="text"
                    id="cidadeTxt"
                    placeholder="Digite a sua cidade"
                    className={`border-2 rounded-full p-4 w-[65%] mb-5 text-xl transition-all duration-350 ease-in-out
                        focus:outline-none focus:scale-103 focus:bg-white/10
                        hover:scale-103 hover:bg-white/10 font-extralight`}
                />
            </form>

            <div className="w-[65%] flex flex-col items-center p-4 rounded-lg shadow-lg bg-gradient-to-b from-blue-900 to-blue-500 ">
                <div className="flex justify-between mb-5 w-[90%]">
                    <h2 className="">Nascer do sol:</h2>
                    <h1 className="font-bold text-4xl">{data.location?.place}</h1>
                    <h2 className="">Pôr do sol:</h2>
                </div>

                <div className="flex items-baseline">
                    <h1 className="font-bold text-7xl">{Math.round(data.forecast?.temperature) || "--"}°</h1>
                </div>            
                <div className="grid grid-cols-2 md:grid-cols-3 gap-2 mt-8 pb-8">
                    {[ //cria um objeto com cada campo que irá ser colocado
                        { icon: "wi:thermometer", label: "Máx", value: `${Math.round(data.forecast?.maxTemperature) || "0" }°` },
                        { icon: "wi:rain", label: "Chuva", value: `${data.forecast?.precipitation || "0" } mm` },
                        { icon: "wi:humidity", label: "Umidade", value: `${data.forecast?.humidity || "0" }%` },
                        { icon: "wi:thermometer-exterior", label: "Mín", value: `${Math.round(data.forecast?.minTemperature) || "0" }°` },
                        { icon: "wi:showers", label: "Prob. Chuva", value: `${data.forecast?.rain_probability || "0" }%` },
                        { icon: "wi:strong-wind", label: "Vento", value: `${Math.round(data.forecast?.wind_speed.speed)} km/h` ||  "--"},
                    ].map((item, index) => ( // cada div pai sera mais 1 no index para buscar o seu respectivo item
                        <div
                            key={index}
                            className="flex items-center justify-center rounded-lg bg-gradient-to-b from-blue-900 to-blue-800 min-w-[20%] min-h-[30%] py-1 px-4 shadow-md"
                        >
                            <Icon icon={item.icon} className="w-8 h-8 text-white mr-2" />
                            <span className="text-white text-sm font-semibold">{item.label}:</span>
                            <span className="text-white text-lg font-light ml-2">{item.value}</span>
                        </div>
                        // nao costumo usar essa abordagem, mas aqui se tornou necessario por conta da repeticao de codigo
                    ))}
                </div>
                <div className="w-full border-t-3 border-white rounded-full" />
            </div>
            <div className="w-[65%] h-[15%] flex justify-between mt-1">
                <div className="w-[60%] flex flex-col items-center p-2 rounded-lg shadow-lg bg-gradient-to-b from-blue-500 to-blue-900 ">
                    <div className="flex w-full">
                        <h1 className="font-bold text ">Previsão para as próximas horas</h1>

                    </div>
                    <div className="w-full border-t-3 border-white rounded-full"/>
                    
                </div>   
                <div className="w-[39.5%] flex flex-col items-center p-4 rounded-lg shadow-lg bg-gradient-to-b from-blue-500 to-blue-900  ">
                    
                </div>           
            </div>
        </>
    );
}

export default WeatherPage;
