# https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial/circuitpython
import board
import busio
import sdcardio
import storage

# SPI0 TX, SPI0 RX
# creating spi object - SCK, MOSI, MISO
spi = busio.SPI(clock = board.GP2, MOSI = board.GP3, MISO = board.GP4)
cs = board.GP5

# microSD card object and filesystem object
sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)

# mount the microSD card's filesystem into the CircuitPython filesystem
storage.mount(vfs, "/sd")
