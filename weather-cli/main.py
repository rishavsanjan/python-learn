import requests
import os
from dotenv import load_dotenv

def start_app():
    url = "https://api.openweathermap.org/data/2.5/weather"

    load_dotenv()

    api_key = os.getenv("API_KEY")

    if len(api_key) == 0:
        print("No api key found!")
        return

    while True: 
        try:
            lat = float(input("Enter your latitude : "))
        except ValueError:
            print("Invalid input!")
            continue
        break

    while True: 
            try:
                long = float(input("Enter your longitude : "))
            except ValueError:
                print("Invalid input!")
                continue
            break
    
    params = {
        "appid" : api_key,
        "lat": lat,
        "lon": long,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        return
         

    
    print("Staus code :", response.status_code)

    try:
        response_data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON response from the server.")
        return

    print(response_data)
    print(f"Location: {response_data['name']}")
    print(f"Temperature: {response_data['main']['temp']:.1f}°C")
    print(f"Wind speed :, {response_data["wind"]["speed"]}m/s")
    print(f"Feels like: {response_data["main"]["feels_like"]}°C")
    print("Condition :", response_data["weather"][0]["description"])

    print(f"Humidity:, {response_data["main"]["humidity"]}%")


start_app()


