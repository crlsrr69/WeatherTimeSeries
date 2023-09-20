import requests
import matplotlib.pyplot as plt
from datetime import datetime

api_key = 'ac45318b3ed78a56609523496d001c4b'
city = 'Angeles City' 
url = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=ac45318b3ed78a56609523496d001c4b'

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()

    
    dates = [datetime.utcfromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S') for entry in weather_data['list']]
    temperatures = [entry['main']['temp'] - 273.15 for entry in weather_data['list']]  

    
    plt.figure(figsize=(12, 6))
    plt.plot(dates, temperatures, marker='o', linestyle='-')
    
    plt.xlabel('Date')
    plt.ylabel('Temperature (Celsius)')
    plt.title(f'Temperature Time Series in Angeles City')
    
    plt.xticks(rotation=45)  
    
    plt.grid(True)
    plt.tight_layout()
    
    plt.show()
else:
    print('Error fetching weather data.')




