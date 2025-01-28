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
def cardWrite(count, temp, pressure, uv, signal):
    """ Writes to a new csv file everytime the program is restarted """
    counter = 0

    while True:
        path = "sd/data" + str(counter) + ".csv"
        print(path)

        try:
            with open(path) as tempFile:
                counter += 1

        except OSError:
            break

        except:
            print("ERROR IN CARD WRITE FUNCTION LINE 40")

        #if not os.path.exists(path):
        #    counter += 1
        #
        # else:
        #     break

    with open(path, "a") as file:
        time.sleep(0.2)
        # creates writer object allowing you to write to csv
        # file.write(["Packet Count", "RSSI", "Temperature", "Pressure", "UV"])
        string = f"{count},{signal},{temp},{pressure},{uv}\n"
        file.write(string)
        print("written to", path)
        time.sleep(0.2)


def testWrite(data):
    with open("/sd/test.txt", "w") as file:
        file.write("hi world")
