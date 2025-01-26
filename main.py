# Code for the CanSat, written by the software designer / programmer of Team Raven
import adafruit_bmp280, adafruit_ltr390
import bmp280,ltr390
import sdCard
import radio
import digitalio
import board
import busio
import time
import random
import datetime

# the black one is scl, the brown one is sda
i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)
ltr390_sensor = adafruit_ltr390.LTR390(i2c)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

packetCount = 0

while True:
    led.value = not led.value
    radioMessage = radio.tryRead()

    if radioMessage is not None:
        print("Radio RX {:d} {:s}".format(packet_count, str(radioMessage, "ascii")))
        rssi = radio.rssi()
        print("RSSI: {:3d}db".format(rssi))
        packetCount += 1
    else:
        rssi = 0

    temp = bmp280.read_temperature(i2c, bmp280_sensor)
    pressure = bmp280.read_pressure(i2c, bmp280_sensor)
    uv = ltr390.read_uv(i2c, ltr390_sensor)
    
    # def cardWrite(filepath, count, temp, pressure, uv, signal):
    path = datetime.datetime.now().strftime("d") + "_" + datetime.datetime.now().strftime("m") + "_" + datetime.datetime.now().strftime("Y") + "_" + datetime.datetime.now().strftime("H") + "_" + datetime.datetime.now().strftime("M") + "_" + datetime.datetime.now().strftime("S") + ".csv"
    sdCard.cardWrite(path, packetCount, temp, pressure, uv, rssi)
    
    print("\n--------------------------------\n")
    print(f"Cansat Temperature: {temp}")
    print(f"Cansat Pressure:    {pressure}")
    print(f"UV levels:          {uv}")

    radio.send(f"------------------\nTeam Raven\n Temperature: {temp}\nPressure:    {pressure}\nUV levels:          {uv}\n------------------")
    print("--- Radio Message sent ---")
