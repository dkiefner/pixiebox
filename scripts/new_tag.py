#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pathlib
import os

reader = SimpleMFRC522()
uploadDir = "~pixiebox/audio/upload/"

try:
    print(f"Move all audio files you want to associate with a RFID tag into the folder {uploadDir}")
    print("Scan you RFID tag now...")

    chip_id, _ = reader.read()
    print(f"chip_id={chip_id}")
    rfidDir = f"~pixiebox/audio/rfid/{chip_id}"

    print("Checking if directory already exists...")
    newDir = pathlib.Path(rfidDir)
    if newDir.exists():
        print(f"{rfidDir} already exists. Please delete directory manually and retry!")
    else:
        print(f"Creating dir {rfidDir}")
        newDir.mkdir(755)
        
        print(f"Moving files from {uploadDir} to {rfidDir}")
        allfiles = os.listdir(uploadDir)
        for f in allfiles:
            os.rename(uploadDir + f, rfidDir + f)

finally:
    GPIO.cleanup()