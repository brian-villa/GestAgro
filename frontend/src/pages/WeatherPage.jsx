import React, {useState} from "react";
import { Icon } from '@iconify/react';
import { useLocation, useNavigate} from "react-router-dom";

function WeatherPage(){

    const location = useLocation();
    const data = location.state?.forecastData;
    const [cidade, setCidade] = useState("");
    const [forecastIndex, setForecastIndex] = useState(0);
    const [indexHour, setIndexHour] = useState(3);
    const navigate = useNavigate();
    

    const sunriseTime = new Date(data.forecast?.sunrise).toLocaleTimeString("pt-BR", {
        hour: "2-digit",
        minute: "2-digit"
    });

    const sunsetTime = new Date(data.forecast?.sunset).toLocaleTimeString("pt-BR", {
        hour: "2-digit",
        minute: "2-digit"
    });

    async function fetchLocationName(cidade) {
        try {
        const response = await fetch("http://localhost:5000/location", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ place: cidade }),
        });
        const data = await response.json();
        return data;
        } catch (error) {
        return null;
        }
    }
    console.log("Dados recebidos:", data);

    const handleConfirm = async (e) => {
        e.preventDefault();

        if (!cidade.trim()) return;
        
        const data = await fetchLocationName(cidade.trim());

        if (data) {
            navigate('/forecast', { state: { forecastData: data } });
        } else {
            alert("Cidade não encontrada.");
        }
    };

    function capitalizeFirstLetter(str) {
        if (!str) return "";
        return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
    }

    const handleNext = () => {
        if (forecastIndex < data.weekly_forecast.length - 1) {
            setForecastIndex(forecastIndex + 1);
            setIndexHour(indexHour + 3);
        }
    };

    const handlePrev = () => {
        if (forecastIndex > 0) {
            setForecastIndex(forecastIndex - 1);
            setIndexHour(indexHour - 3);
        }
    };

    return (
        <>
            <form onSubmit={handleConfirm} className="w-full flex justify-center">
                <input
                    type="text"
                    id="cidadeTxt"
                    placeholder="Digite a sua cidade"
                    onChange={(e) => setCidade(e.target.value)}
                    onKeyPress={(e) => {
                        if (!/[a-zA-ZÀ-ÿ\s]/.test(e.key)) {
                        e.preventDefault();
                        }
                    }}
                    autoComplete="off"
                    className={`border-2 rounded-full p-4 w-[80%] sm:w-[66%] mb-5 text-xl transition-all duration-350 ease-in-out
                        focus:outline-none focus:scale-103 focus:bg-white/10
                        hover:scale-103 hover:bg-white/10 font-extralight`}
                />
            </form>

            <div className="w-[80%] sm:w-[66%] flex flex-col items-center p-4 rounded-lg shadow-lg bg-gradient-to-b from-blue-900 to-blue-500 ">
                <h1 className="font-bold text-center text-3xl sm:text-4xl">{capitalizeFirstLetter(data.location?.place)}</h1>
                <div className="flex justify-between mb-5 w-[100%] text-white text-lg font-semibold">
                    <div className="flex items-center space-x-2">
                        <Icon icon="wi:sunrise" className="w-6 h-6" />
                        <span className="font-light">{sunriseTime}</span>
                    </div>
                    <div className="flex items-center space-x-2">
                        <Icon icon="wi:sunset" className="w-6 h-6" />
                        <span className="font-light">{sunsetTime}</span>
                    </div>
                </div>
                <h1 className="font-bold text-7xl">{Math.round(data.forecast?.temperature) || "--"}°</h1>          
                <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 w-full mt-3 mb-2">
                    {[
                        { icon: "wi:thermometer", label: "Máx", value: `${Math.round(data.forecast?.maxTemperature) || "0"}°` },
                        { icon: "wi:rain", label: "Chuva", value: `${data.forecast?.precipitation || "0"} mm` },
                        { icon: "wi:humidity", label: "Umidade", value: `${data.forecast?.humidity || "0"}%` },
                        { icon: "wi:thermometer-exterior", label: "Mín", value: `${Math.round(data.forecast?.minTemperature) || "0"}°` },
                        { icon: "wi:showers", label: "Prob. Chuva", value: `${data.forecast?.rain_probability || "0"}%` },
                        { icon: "wi:strong-wind", label: "Vento", value: `${Math.round(data.forecast?.wind_speed) || 0} km/h` },
                    ].map((item, index) => (
                        <div
                        key={index}
                        className="p-1 flex flex-col items-center justify-center text-center rounded-lg bg-gradient-to-b from-blue-900 to-blue-800 shadow-md"
                        >
                            <Icon icon={item.icon} className="w-6 h-6 sm:w-10 sm:h-10 text-white " />
                            <span className="text-white text-sm font-semibold">{item.label}</span>
                            <span className="text-white text-sm font-light">{item.value}</span>
                        </div>
                    ))}
                </div>
                <div className="w-full border-t-3 border-white rounded-full" />
            </div>
            <div className="w-[80%] sm:w-[66%] h-[30%] sm:h-[20%] flex justify-between mt-1">
                <div className="w-[60%] flex flex-col items-center p-2 rounded-lg shadow-lg bg-gradient-to-b from-blue-500 to-blue-900 ">
                    <div className="flex w-full">
                        <h1 className="font-bold text-sm sm:text-md"> Previsão para as próximas {indexHour} horas</h1>
                        <div className="flex">
                            <Icon icon="material-symbols:play-arrow-rounded"
                             className="text-white w-6 h-6 rotate-180 cursor-pointer hover:scale-120"
                             onClick={handlePrev}
                            />
                            <Icon icon="material-symbols:play-arrow-rounded" 
                             className="text-white w-6 h-6 cursor-pointer hover:scale-120"
                             onClick={handleNext}
                            />
                        </div>
                    </div>
                    <div className="w-full border-t-3 border-white rounded-full mb-2"/>
                    <div className="w-full text-white">
                        <div className="flex items-center justify-center sm:hidden mb-3">
                            <span className="font-bold text-3xl mr-2">
                                {Math.round(data.weekly_forecast?.[forecastIndex].maxTemperature)}°
                            </span>
                            <span>{Math.round(data.weekly_forecast?.[forecastIndex].minTemperature)}°</span>
                        </div>
                        <div className="grid grid-cols-2 sm:flex sm:justify-around gap-2">
            
                            <div className="hidden sm:flex items-center">
                                <span className="font-bold text-3xl mr-2">
                                    {Math.round(data.weekly_forecast?.[forecastIndex].maxTemperature)}°
                                </span>
                                <span>{Math.round(data.weekly_forecast?.[forecastIndex].minTemperature)}°</span>
                            </div>

                            <div className="flex items-center">
                                <Icon icon="wi:rain" className="w-8 h-8 mr-1" />
                                <span className="font-light">{data.weekly_forecast?.[forecastIndex].precipitation} mm</span>
                            </div>

                            <div className="flex items-center">
                                <Icon icon="wi:showers" className="w-8 h-8 mr-1" />
                                <span className="font-light">{data.weekly_forecast?.[forecastIndex].rain_probability}%</span>
                            </div>

                            <div className="flex items-center">
                                <Icon icon="wi:strong-wind" className="w-8 h-8 mr-1" />
                                <span className="font-light">
                                    {Math.round(data.weekly_forecast?.[forecastIndex].wind_speed)} km/h
                                </span>
                            </div>

                            <div className="flex items-center">
                                <Icon icon="wi:humidity" className="w-8 h-8 mr-1" />
                                <span className="font-light">{data.weekly_forecast?.[forecastIndex].humidity}%</span>
                            </div>
                        </div>
                    </div>
                </div>   
                <div className=" w-[39%] sm:w-[39.5%] flex flex-col items-center p-4 rounded-lg shadow-lg bg-gradient-to-b from-blue-500 to-blue-900  ">
                    
                </div>           
            </div>
        </>
    );
}

export default WeatherPage;
