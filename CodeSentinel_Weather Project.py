import requests
import json

# Replace with your own API key (get it free at https://openweathermap.org/api)
API_KEY = "0354dc151dbe917f7dbd62d08a5612a6"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Build request URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    # Send GET request
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # parse JSON response
        
        # Extract needed fields
        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        
        print(f"\n🌍 Weather in {city_name}:")
        print(f"🌡 Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Condition: {condition.capitalize()}\n")
        
    else:
        print("❌ City not found or error fetching data.")

def main():
    city = input("Enter city name: ").strip()
    get_weather(city)

if __name__ == "__main__":
    main()
