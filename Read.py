# based on: https://pimylifeup.com/raspberry-pi-rfid-rc522/ 
# reads card ID + text (data) from card or transponder

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from os import system, name
from time import sleep

# Function to clear screen
# based on: https://www.geeksforgeeks.org/clear-screen-python/

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

reader = SimpleMFRC522()

# Loop to keep reader active
# can be cancelled with Ctrl+C

try:
    while (True):
        id, text = reader.read()
        print("ID is:"+str(id))
        print("Text is:"+str(text))
        sleep(5)
        clear()

finally:
        GPIO.cleanup()