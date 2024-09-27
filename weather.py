import requests  


API_KEY = '87029d5cf2524294bae91802242709'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

city = input("Enter the name of the city: ")


url = f"{BASE_URL}?key={API_KEY}&q={city}"

response = requests.get(url)


data = response.json()


if response.status_code == 200:
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"Current temperature in {city}: {temperature}°C")
    print(f"Weather condition: {condition}")
else:
    print(f"Error: Unable to fetch weather data (status code: {response.status_code})")
