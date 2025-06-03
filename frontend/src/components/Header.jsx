import React, { useState } from "react";
import Logo from "../assets/WeatherWatcherLogo.png"
import LogoHover from "../assets/WeatherWatcherLogoHover.png"

function Header(){

    const [isHovered, setIsHovered] = useState(false);

    return(
        <div className="flex w-full ">
            <img 
                src={isHovered ? LogoHover : Logo}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
                onClick={() => location.reload()}
                alt="Logo do WeatherWatcher"
                className="h-25 cursor-pointer transition-all ease-in-out hover:scale-105"   
            />
        </div>
    )

}
export default Header