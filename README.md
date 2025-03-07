## IoT Weather Station - Marius-Augustin Niţu

The project is a weather monitoring system built using a Raspberry Pi and programmed in Python. It utilizes a AHT10 and MPL3115A2 sensor, communicating over the I2C protocol, to acquire temperature, humidity, and atmospheric pressure data. The collected data is sent to the IoT platform ThingSpeak using HTTP requests. On the ThingSpeak platform, the data is stored, analyzed, and visualized through real-time graphs and charts.

### Installation

The project can launched as a simple Python script.

1. Clone the repository.
	```
	git clone git@github.com:Marius-Augustin/WeatherStation.git
	```
2. Run the Python script.
	```
	python3 main.py
	```

### Hardware

* Raspberry Pi 3B
* AHT10 Sensor
* MPL3115A2 Sensor

### Further Notes

* API Keys are visible in this repository. This project is for educational purposes, so this is not a security concern.
* The Keys are not used for sensitive operations.
