import Adafruit_DHT
from sys import exit
from time import sleep

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 27

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
        sleep(2)
    except KeyboardInterrupt:
        print("Quit")
        exit()

		
