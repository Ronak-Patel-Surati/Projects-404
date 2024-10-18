import React, { useState, useEffect } from "react";

const Weather = () => {
  const [weatherData, setWeatherData] = useState(null);
  const [city, setCity] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false); 

  // Function to fetch weather data based on city name or coordinates
  const fetchWeather = async (lat = null, lon = null, city = null) => {
    const apiKey = 'f07cdf6080ee17b38fd72a5a1c6d3862'; 
    let url;
  
    if (lat && lon) {
      url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
    } else if (city) {
      url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;
    } else {
      throw new Error('Please provide either latitude/longitude or a city name');
    }
  
    try {
      setLoading(true); // Start loading before fetching
      const response = await fetch(url);
      console.log(response)
      if (!response.ok) {
        throw new Error('Unable to Fetch Weather Data');
      }
      const data = await response.json();
      setWeatherData(data);
    } catch (error) {
      console.error('There has been a problem with your fetch operation:', error);
      setError(error.message);
    } finally {
      setLoading(false); // Stop loading after the fetch completes
    }
  };
  

  useEffect(() => {
    const getLocationAndFetchWeather = () => {
        setError(null);
      if (navigator.geolocation && !city) { // Only use location if no city is provided
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const { latitude, longitude } = position.coords;
            fetchWeather(latitude, longitude);
          },
          (error) => {
            setError('Failed to retrieve location');
            setLoading(false);
          }
        );
      } else if (city) { // Fetch weather if city is set
        fetchWeather(null, null, city);
      }
    };

    getLocationAndFetchWeather();
  }, [city]);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSearch = () => {
    if (!inputValue) {
      setError("Please enter a city name");
      return;
    }
    setCity(inputValue); // This will trigger useEffect to fetch weather for the new city
    setLoading(true); // Set loading to true while fetching new data
  };

  // Convert Unix timestamp to a formatted time string
  const convertUnixToTime = (timestamp) => {
    const date = new Date(timestamp * 1000); // Convert seconds to milliseconds
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className="weather-container p-4">
      <div className="enterCity flex items-center mb-4">
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Search"
          className="outline-blue-500 w-full mx-auto my-2 bg-blue-200 rounded-md px-4 py-2"
        />
        <button
          onClick={handleSearch}
          className="ml-2 px-4 py-2 bg-blue-500 text-white rounded-md"
        >
          Search
        </button>
      </div>
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      {weatherData && (
        <div className="flex items-start font-mono">
          <img
            src={`http://openweathermap.org/img/wn/${weatherData.weather[0].icon}.png`}
            alt={weatherData.weather[0].description}
            className="h-16 mr-2"
          />
          <div>
            <h1 className="text-2xl font-bold">{weatherData.main.temp}°C</h1>
            <div className="my-2"></div>
            <p className="text-2xl font-semibold">{weatherData.name}, {weatherData.sys.country}</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">{weatherData.weather[0].description}</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Humidity: {weatherData.main.humidity}%</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Wind Speed: {weatherData.wind.speed} m/s</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Wind Direction: {weatherData.wind.deg}°N </p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Feels Like: {weatherData.main.feels_like}°C</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Temp Min: {weatherData.main.temp_min}°C</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Temp Max: {weatherData.main.temp_max}°C</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Cloudiness: {weatherData.clouds.all}%</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Sunrise: {convertUnixToTime(weatherData.sys.sunrise)}</p>
            <div className="my-2"></div>
            <p className="text-xl font-semibold">Sunset: {convertUnixToTime(weatherData.sys.sunset)}</p>
            <div className="my-2"></div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Weather;
