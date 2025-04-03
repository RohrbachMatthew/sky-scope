import requests

# API KEY
# BASE_URL

def get_weather(city):
    """fetch weather from API"""
    
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric" # metric gives the temp in Celsisus

    try:
        response = requests.get(url)
        response.raise_for_status()  # raises exception errors
        
        return response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None