import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Index from "./pages/Index";
import Header from "./components/Header";
import WeatherPage from "./pages/WeatherPage";

function App() {
  return (
    <BrowserRouter>
      <div className="w-full h-screen overflow-hidden flex flex-col items-center bg-gradient-to-b from-blue-900 to-blue-400 pb-5">
        <Header />
        <Routes>
          <Route path="/" element={<Index />} /> {/* Rota padrao do site */}
          <Route path="/forecast" element={<WeatherPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

