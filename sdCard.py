# https://www.raspberrypi.com/documentation/computers/remote-access.html
# https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial/circuitpython
import board
import busio
import sdcardio
import storage
import time
import os

# SPI0 TX, SPI0 RX
# creating spi object - SCK, MOSI, MISO
spi = busio.SPI(clock = board.GP10, MOSI = board.GP11, MISO = board.GP12)
cs = board.GP13

# microSD card object and filesystem object
sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)

# mount the microSD card's filesystem into the CircuitPython filesystem
storage.mount(vfs, "/sd")


# filename = datetime.datetime.now() + ".csv"
def cardWrite(session, count, temp, pressure, uv, signal):
    """ Writes to a new csv file everytime the program is restarted """
    counter = 0

    while True:
        path = "sd/data" + str(counter) + ".csv"
        print(path)
        try:
            with open(path) as tempFile:
                print("file successfully opened, incrementing counter")

        except OSError:
            break

        except:
            print("ERROR IN CARD WRITE FUNCTION LINE 40")
        
        counter += 1
        
    if session:
        counter -= 1
        path = "sd/data" + str(counter) + ".csv"

    with open(path, "a") as file:
        if not session:
            file.write("count,signal,temp,pressure,uv")
        
        string = f"{count},{signal},{temp},{pressure},{uv}\n"
        file.write(string)
        
        print("written to", path)


#def testWrite(data):
#    with open("/sd/test.txt", "w") as file:
#        file.write("hi world")
