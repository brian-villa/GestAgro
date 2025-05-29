import React, { useState } from "react";
import Logo from "../assets/WeatherWatcherLogo.png"
import LogoHover from "../assets/WeatherWatcherLogoHover.png"

function Header(){

    const [isHovered, setIsHovered] = useState(false);

    return(
        <div className="flex w-full p-5">
            <img 
                src={isHovered ? LogoHover : Logo}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
                alt="Logo do WeatherWatcher"
                className="h-20 transition-all ease-in-out hover:scale-105"   
            />
        </div>
    )

}
export default Header