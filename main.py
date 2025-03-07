from readData import *
from sendData import *

if __name__ == "__main__":
    
    [temperature, pressure] = readMPL3115A2()
    humidity = readAHT10()
    sendThingsSpeak(temperature, pressure, humidity) 