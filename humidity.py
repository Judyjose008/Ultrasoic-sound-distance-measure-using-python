import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
	humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
		print("Temp:{}c Humidity : {}%".format(temperature, humidity));
	else:
		print("Sensor failed")
	time.sleep(3)
