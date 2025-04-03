from flask import Flask, jsonify, request
from services import get_weather  # Import the weather service function

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    weather_data = get_weather(city)
    
    if weather_data:
       
        result = {
            "city": weather_data["name"],
            "temperature": weather_data["main"]["temp"], 
            "condition": weather_data["weather"][0]["description"], 
            "icon": weather_data["weather"][0]["icon"]  
        }
        return jsonify(result)  
    else:
        return jsonify({"error": "Could not retrieve weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
