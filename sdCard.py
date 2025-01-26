# https://www.raspberrypi.com/documentation/computers/remote-access.html
# https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial/circuitpython
import board
import busio
import sdcardio
import storage
import csv
from pathlib import Path

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
def cardWrite(filepath, count, temp, pressure, uv, signal):
    """ Writes to a new csv file everytime the program is restarted """
    if Path(filepath):
        exist = True
    else:
        exist = False
    
    with open(filepath, "w") as file:
        # creates writer object allowing you to write to csv
        writer = csv.writer(file)
        
        if not exist:
            writer.writerow(["Packet Count", "RSSI", "Temperature", "Pressure", "UV"])
            
        writer.writerow([count, signal, temp, pressure, uv])
        
        
