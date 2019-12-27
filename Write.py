# based on: https://pimylifeup.com/raspberry-pi-rfid-rc522/ 
# writes a text and reads it out again (including card ID)

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('New data:')
    print("Now place your tag to write")
    reader.write(text)
    print("Written")

finally:
    GPIO.cleanup()

reader = SimpleMFRC522()

try:
     id, text = reader.read()
     print("id: "+str(id))
     print("text: "+str(text))

finally:
    GPIO.cleanup()