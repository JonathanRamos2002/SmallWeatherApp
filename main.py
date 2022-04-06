import requests

API_KEY = "3199fe3603a2c22050017054721fbcf6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    country = data['sys']['country']
    city_name = data['name']
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    temperatureF = round((data['main']['temp'] - 273.15) * (9/5) + 32, 2)
    humidity = data['main']['humidity']
    feels_like_c = round(data['main']['feels_like'] - 273.15, 2)
    feels_like_f = round((data['main']['feels_like'] - 273.15) * (9/5) + 32, 2)

    # Choose Temperature Scale
    temp_scale = input("Choose a temperature scale; 'celsius', 'fahrenheit', 'both': ")

    print("\nChosen Location:", city_name, ",", country)
    print("Weather:", weather)
    if temp_scale == "celsius":
        print("Temperature:", temperature, "celsius")
        print("Feels like:", feels_like_c, "celsius")
    elif temp_scale == "fahrenheit":
        print("Temperature:", temperatureF, "fahrenheit")
        print("Feels like:", feels_like_f, "fahrenheit")
    elif temp_scale == "both":
        print("Temperature:", temperatureF, "fahrenheit,", temperature, "celsius")
        print("Feels like:", feels_like_f, "fahrenheit,", feels_like_c, "celsius")
    else:
        print("Temperature:", temperatureF, "fahrenheit")
        print("Feels like:", feels_like_f, "fahrenheit")
    print("Humidity:", humidity)
else:
    print("An error occurred.")
