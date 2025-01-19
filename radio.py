import digitalio
import board
import busio
import adafruit_rfm9x
import bmp280

spi = busio.SPI(clock = board.GP2, MOSI = board.GP3, MISO = board.GP4)

cs = digitalio.DigitalInOut(board.GP6)
reset = digitalio.DigitalInOut(board.GP7)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 433.0)

# a bunch of functions
def send(message):
    rfm9x.send(message)

def tryRead():
    return rfm9x.receive(timeout = 5.0)

def rssi():
    return rfm9x.rssi


print("----- RFM9x radio started successfully ------")
