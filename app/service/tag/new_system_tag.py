#!/usr/bin/env python

from lib.command import SystemCommand
from lib.di import ServiceLocatorFactory, ServiceName
from lib.rfid_reader import MFRC522Reader

service_locator = ServiceLocatorFactory.create()
system_tag_store = service_locator.get(ServiceName.SystemTagStore)

print("Which system action do you want to record?:")
print("1) Stop playing music")
print("2) Volume up")
print("3) Volume down")
print("\nUse 'q' to exit this script.")

keyToCommandDict = {
    "1": SystemCommand.STOP.name,
    "2": SystemCommand.VOLUME_UP.name,
    "3": SystemCommand.VOLUME_DOWN.name
}

while True:
    input_key = input()

    if "q" == input_key.rstrip():
        break

    if input_key in keyToCommandDict:
        print(f"Please use the RFID tag you want to link to the action '{keyToCommandDict[input_key]}'")
        rfidReader = MFRC522Reader()
        rfid_tag = rfidReader.read()
        system_tag_store.save(rfid_tag, keyToCommandDict[input_key])
        rfidReader.cleanup()
        break
    else:
        print(f"Sorry, {input_key} is not a valid option.")

print("Done.")
