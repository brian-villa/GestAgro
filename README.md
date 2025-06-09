
[English Version](#weatherforecast-web-app-(english))

# WeatherForecast Web App

Este projeto é uma aplicação web interativa de previsão do tempo, desenvolvida com foco na experiência do utilizador, simplicidade e comunicação em tempo real. A aplicação permite ao utilizador obter informações meteorológicas atuais, previsões para as próximas horas e sugestões a partir do nome de uma cidade ou da seleção de uma localização em um mapa interativo.

## Funcionalidades

- Busca de localizações via campo de texto
- Seleção interativa da localização em mapa
- Comunicação em tempo real com backend
- Atualizações automáticas dos dados meteorológicos a cada 30 segundos
- Visualização clara das condições atuais
- Previsão das próximas horas do dia
- Alertas dinâmicos personalizados baseados nas condições climáticas

## Tecnologias Utilizadas

### Frontend

- React.js
- Tailwind CSS
- React Router DOM
- Leaflet.js (para mapa interativo)

### Backend

- Flask
- Flask-CORS
- Websockets
- Requests
- python-dotenv

### API de Dados Meteorológicos

- OpenWeatherMap (ou outra API externa configurada no backend)

## Instalação e Execução

### Frontend
cd frontend
npm install
npm run dev

### Backend
cd backend
pip install -r requirements.txt
python app.py


# WeatherForecast Web App (English)

This project is an interactive weather forecast web application, developed with a focus on user experience, simplicity, and real-time communication. The app allows users to obtain current weather information, forecasts for the next hours, and suggestions by entering a city name or selecting a location on an interactive map.

## Features

- Location search via text input
- Interactive location selection on map
- Real-time communication with backend
- Automatic weather data updates every 30 seconds
- Clear display of current conditions
- Hourly weather forecast for the upcoming hours
- Dynamic personalized alerts based on weather conditions

## Technologies Used

### Frontend

- React.js
- Tailwind CSS
- React Router DOM
- Leaflet.js (for interactive map)

### Backend

- Flask
- Flask-CORS
- Websockets
- Requests
- python-dotenv

### Weather Data API

- OpenWeatherMap (or another external API configured in the backend)

## Installation and Running

### Frontend

cd frontend
npm install
npm run dev

### Backend

cd backend
pip install -r requirements.txt
python app.py
