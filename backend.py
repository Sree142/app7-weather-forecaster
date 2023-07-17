import requests

API_KEY = "add6d0e0f26f11c4c11ca940e8fedb5b"

def get_data(place, forecast_days=None):
    place_url = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=1&appid={API_KEY}"
    place_response = requests.get(place_url)
    place_data = place_response.json()
    # print(place_data[0])
    lat = place_data[0]["lat"]
    lon = place_data[0]["lon"]

    weather_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    weather_response = requests.get(weather_url)
    data = weather_response.json()
    filtered_data = data["list"]
    num_values = 8*forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data("Tokyo", 2))