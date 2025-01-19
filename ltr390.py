import adafruit_ltr390
import board
import busio

def read_uv(i2c, sensor):
    return sensor.uvs
