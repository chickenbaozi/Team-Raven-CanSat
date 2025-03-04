# https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor
import adafruit_ccs811
import board
import busio

# This part will measure eCO2 (equivalent calculated carbon-dioxide) concentration within a
# range of 400 to 8192 parts per million (ppm), and TVOC (Total Volatile Organic Compound)
# concentration within a range of 0 to 1187 parts per billion (ppb). According to the fact sheet it
# can detect Alcohols, Aldehydes, Ketones, Organic Acids, Amines, Aliphatic and Aromatic Hydrocarbons.

#Please note, this sensor, like all VOC/gas sensors, has variability and to get precise measurements
# you will want to calibrate it against known sources! That said, for general environmental sensors,
# it will give you a good idea of trends and comparisons.

def read_gas(sensor):
    try:
        eco2 = sensor.eco2
        tvoc = sensor.tvoc
    except:
        return False
    return eco2, tvoc
