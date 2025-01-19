# Write your code here :-)
import board
import busio
import adafruit_bmp280

def read_temperature(i2c, sensor):
    return sensor.temperature


def read_pressure(i2c, sensor):
    return sensor.pressure
