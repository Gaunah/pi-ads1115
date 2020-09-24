#!/usr/bin/python3

import time

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

chanA0 = AnalogIn(ads, ADS.P0)

while True:
    time.sleep(1)
    # Voltage times 5 because we use a voltage divider to limit the input voltage to the ADS1115
    voltageA0 = chanA0.voltage * 5
    print("A0 = {} V".format(round(voltageA0, 2)))
