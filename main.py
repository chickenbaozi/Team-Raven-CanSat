# Code for the CanSat, written by the software designer / programmer of Team Raven
import adafruit_bmp280, adafruit_ltr390, adafruit_ccs811
import bmp280,ltr390, ccs811
import sdCard
import radio
import digitalio
import board
import busio
import time
import random
import storage

# the black one is scl, the brown one is sda
def scan_i2c_devices(i2c):
    print("Scanning I2C bus for devices...")
    while not i2c.try_lock():
        pass
    try:
        devices = i2c.scan()
        print(f"Found {len(devices)} device(s):")
        for device in devices:
            print(f" - I2C address: 0x{device:02X}")
    finally:
        i2c.unlock()

i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
scan_i2c_devices(i2c)
time.sleep(0.5)
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)
ltr390_sensor = adafruit_ltr390.LTR390(i2c)
ccs811_sensor = adafruit_ccs811.CCS811(i2c)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

packetCount = 0
session = False

while True:
    led.value = not led.value
    radioMessage = radio.tryRead()

    if radioMessage is not None:
        print("Radio RX {:d} {:s}".format(packetCount, str(radioMessage, "ascii")))
        rssi = radio.rssi()
        print("RSSI: {:3d}db".format(rssi))
        packetCount += 1
    else:
        rssi = 0

    temp = bmp280.read_temperature(bmp280_sensor)
    pressure = bmp280.read_pressure(bmp280_sensor)
    uv = ltr390.read_uv(ltr390_sensor)
    gas = ccs811.read_gas(ccs811_sensor)

    # def cardWrite(filepath, count, temp, pressure, uv, signal):

    filePath = sdCard.cardWrite(session, packetCount, temp, pressure, uv, rssi)
    sdCard.cardRead(filePath)

    session = True

    print("\n--------------------------------\n")
    print(f"Cansat Temperature: {temp}")
    print(f"Cansat Pressure:    {pressure}")
    print(f"UV levels:          {uv}")
    print(f"Gas levels:         {gas}")

    radio.send(f"------------------\nTeam Raven\n Temperature: {temp}\nPressure:    {pressure}\nUV levels:          {uv}\n------------------")
    print("--- Radio Message sent ---")
