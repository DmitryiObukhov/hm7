import requests


def get_weather(city_name, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city_name
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if "current" in data:
            current_data = data["current"]
            temperature = current_data["temp_c"]
            condition = current_data["condition"]["text"]
            print(f"City: {city_name}")
            print(f"Temperature: {temperature}°C")
            print(f"Weather: {condition}")
        else:
            print("Weather information not available.")
    except requests.exceptions.RequestException:
        print("Error when making an API request")
