document.getElementById("searchBtn").addEventListener("click", () => {
    const city = document.getElementById("cityInput").value;
    if (city) {
        fetchWeather(city);
    }
});

async function fetchWeather(city) {
    const apiKey = "";
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;
    document.getElementById("weatherInfo").innerHTML = "<p>Loading...</p>"; 

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("City not found");
    
        const data = await response.json();
        document.getElementById("location").textContent = `${data.name}, ${data.sys.country}`;
        document.getElementById("temperature").textContent = `${Math.round(data.main.temp)}°C`;
        document.getElementById("description").textContent = data.weather[0].description;
        document.getElementById("weatherIcon").src = `https://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
    } catch (error) {
        alert(error.message);  // error message if something goes wrong
    } finally {
        document.getElementById("weatherInfo").innerHTML = "";  // Clear loading text when done
    }
    
}
