#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        print("Waiting for RFID chip...")
        id, text = reader.read()
        print(id)
finally:
        GPIO.cleanup()
