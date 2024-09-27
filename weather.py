import requests  # Import the requests library

# Replace 'your_api_key' with your actual API key from WeatherAPI
API_KEY = '87029d5cf2524294bae91802242709'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

# Specify the city for which you want to get weather information
city = 'Nairobi'

# Construct the API request URL
url = f"{BASE_URL}?key={API_KEY}&q={city}"

# Fetch weather data using requests.get() method
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract relevant weather information
if response.status_code == 200:
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"Current temperature in {city}: {temperature}°C")
    print(f"Weather condition: {condition}")
else:
    print(f"Error: Unable to fetch weather data (status code: {response.status_code})")
