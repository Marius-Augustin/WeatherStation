import requests
import time

# Weather Underground
STATION_ID = 'IBUCHA399'
STATION_KEY = 'YwZmWpSf'
WU_URL = 'https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php'

# Things Speak
TS_API_KEY = '3HVO36BRSPCE9HYO'
TS_URL = 'https://api.thingspeak.com/update'

def sendWeatherUnderground(cTemperature, humidity):
    fTemperature = (cTemperature * 9/5) + 32 # Fahrenheit

    params = {
        'ID': STATION_ID,
        'PASSWORD': STATION_KEY,
        'dateutc': 'now',
        'tempf': round(fTemperature, 1),
        'humidity': humidity,
        'action': 'updateraw'
    }

    response = requests.get(WU_URL, params=params)

    if response.status_code == 200:
        print(f"Succesful Weather Underground Upload: {response.text}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

def sendThingsSpeak(temperature, pressure, humidity):
    payload = {
        'api_key': TS_API_KEY,
        'field1': temperature,
				'field2': pressure,        
				'field3': humidity
    }
    response = requests.post(TS_URL, data=payload)
    if response.status_code == 200:
        print(f"Succesful Things Speak Upload: {response.text}")
    else:
        print(f"Error: {response.status_code}, {response.text}")