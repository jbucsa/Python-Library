import requests

# Replace with the actual API URL (consider using a free weather API)
api_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    city_name = data["name"]
    temperature = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius

    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature:.2f} °C")
else:
    print("Error:", response.status_code)

"""
Explanation of the Example:

    1. We import requests.
    2. We define the API URL for weather data in London (replace with the actual API URL and obtain an API key).
    3. We send a GET request and capture the response.
    4. We check the status code.
    5. If successful (200), we parse the JSON response:
        city_name is extracted from the "name" key.
        temperature is converted from Kelvin to Celsius.
    6. We print the city name and temperature.

This is a basic example. Remember to replace placeholders with your actual API URL and potentially handle different response formats or error scenarios in a production environment.


"""