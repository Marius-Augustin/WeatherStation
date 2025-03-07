import smbus
import time
import requests

# Open Weather 
API_KEY = '2410cf2a5e619984faa1ee748e8c4d27'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
CITY = 'Bucharest'

def readOpenWeather():
    params = {
        'q': CITY,
        'units': 'metric',
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
    if response.status_code == 200:
        print(f"Succesful Open Weather read.")
				return [temperature, pressure, humidity]
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# AHT10 - Humidity
def readAHT10():
	bus = smbus.SMBus(1)

	config = [0x08, 0x00]
	bus.write_i2c_block_data(0x38, 0xE1, config)
	time.sleep(0.5)
	byt = bus.read_byte(0x38)
	
	MeasureCmd = [0x33, 0x00]
	bus.write_i2c_block_data(0x38, 0xAC, MeasureCmd)
	time.sleep(0.5)
	data = bus.read_i2c_block_data(0x38,0x00)

	tmp = ((data[1] << 16) | (data[2] << 8) | data[3]) >> 4
	humidity = int(tmp * 100 / 1048576)
	print(u'Humidity: {0}%'.format(humidity))

	return humidity

# MPL3115A2 - Temperature, Pressure
def readMPL3115A2():
	bus = smbus.SMBus(1)

	bus.write_byte_data(0x60, 0x26, 0xB9)
	bus.write_byte_data(0x60, 0x13, 0x07)
	bus.write_byte_data(0x60, 0x26, 0xB9)
	time.sleep(1)

	data = bus.read_i2c_block_data(0x60, 0x00, 6)

	# Convert the data to 20-bits.
	temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16
	cTemp = temp / 16.0
	
	bus.write_byte_data(0x60, 0x26, 0x39)
	time.sleep(1)
	data = bus.read_i2c_block_data(0x60, 0x00, 4)

	# Convert the data to 20-bits.
	pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
	pressure = (pres / 4.0) / 1000.0

	# Output data to screen.
	print("Pressure : %.2f kPa" % pressure)
	print("Temperature in Celsius: %.2f C" % cTemp)

	return [cTemp, pressure]

def readOpenWeather():
    params = {
				'lot': 44.436152,
				'lat': 26.044443,
        'q': city_name,
        'units': 'metric',
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        print(f"Temperatura: {temperature}°C, Umiditate: {humidity}%, Presiune: {pressure} hPa, Descriere: {description}")
        return [temperature, pressure, humidity]
    else:
        return None