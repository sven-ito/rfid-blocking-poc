RFID Blocking PoC
=================

> How effective are RFID blocking wallets, covers and cards - is there an effordable way to test them?

# Why the PoC?

* In our daily lives, we are using an increasing amount of RFID/NFC enabled cards (banking, credit card, passport, ID, health insurance etc.).
* On the one hand, this is very comfortable when performing e.g. contactless payments.
* On the other hand, one could also become victim to "contactless virtual pitpocketing" or potential data leaks in public space.
* Therefore RFID blocking wallets, covers and cards have been developed - some product examples are:
  * https://www.amazon.de/gp/product/B07RD6RHRD
  * https://www.amazon.de/gp/product/B01NBR9VRD

# An Effordable Way

* While it is possible to purchase card reading devices in the medium-high price range, there are also some rather cheap GPIO boards (type: "RC522") for the RaspberryPi available.
* They also come with RFID cards and transponders in kits.
* This means that for the entire PoC setup, we can stay well below 50 EUR:
  * https://www.amazon.de/gp/product/B00T2U7R7I (RaspberryPi 2, Zero/Zero WH should also suffice)
  * https://www.amazon.de/gp/product/B074S8MRQ (RC522 Kit, including several boards and cards)

# My Working Setup

## Tutorials & GitHub Repos

There are several tutorials/code repos on GitHub out there - a lot of them (including the board distributor's) rather describing how to get the module running with Arduino. The most useful to me were:

**GitHub Repos:**

* https://github.com/mxgxw/MFRC522-python (Raspberry/Python2, first steps, basic examples)
* https://github.com/miguelbalboa/rfid (Arduino/C++, very well documented, many examples)
* https://github.com/pimylifeup/MFRC522-python (Raspberry/Python3, better logging/debugging also ships as pip library)

**Tutorials:**

* https://tutorials-raspberrypi.de/raspberry-pi-rfid-rc522-tueroeffner-nfc/ (German tutorial, use case: door lock, used mainly for wiring)
* https://pimylifeup.com/raspberry-pi-rfid-rc522/ (finally working for me)


## Hardware

### Raspberry

* This setup was tested on the following RaspberryPi models:
  * RaspberryPi2
  * RaspberryPi4

### RFID Module

* The used RC522 RFID module was distributed by AZDelivery (https://www.az-delivery.de/)
  * Amazon Link: https://www.amazon.de/gp/product/B01M28JAAZ
  * ships with an S50 card and transponder
* The board is apparently based on the Philips MF522-AN board ("MIFARE" by NXP Semiconductors)
  * See also: https://en.wikipedia.org/wiki/MIFARE
  * The datasheet of the board can be found here: https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf
  * According to the distributor it is compatible (at least) with the RFID "formats" S50, S70 Ultralight, Pro

### Wiring & Interface

* The board was connected to the Pi via **SPI** (serial peripheral interface):
  * See: https://en.wikipedia.org/wiki/Serial_Peripheral_Interface
  * See also: https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md
* The wiring was done according to this tutorial (https://tutorials-raspberrypi.de/raspberry-pi-rfid-rc522-tueroeffner-nfc/):

RF522 Module | Raspberry Pi
------------ | ------------
SDA	| Pin 24 / GPIO8 (CE0)
SCK	| Pin 23 / GPIO11 (SCKL)
MOSI | Pin 19 / GPIO10 (MOSI)
MISO | Pin 21 / GPIO9 (MISO)
IRQ	| (not connected)
GND | Pin6 (GND)
RST | Pin22 / GPIO25
3.3V | Pin 1 (3V3)

## Software

### Operating System

* Both Raspberries used Raspbian Buster as OS (image: 2019-09-26-raspbian-buster-full).
  * See: http://downloads.raspberrypi.org/raspbian/images/raspbian-2019-09-30/ (not exact image)
* SPI might have to be enabled first. Check if SPI is activated/available:

  ```
  pi@raspberrypi:~ $ lsmod | grep spi
  spidev                 20480  0
  spi_bcm2835            20480  0
  ```

* Alternatively:

  ```
  pi@raspberrypi:~ $ ls /dev/*spi*
  /dev/spidev0.0  /dev/spidev0.1
  ```

### Python

* The setup was tested on **Python 3.7** (as included with Raspbian):

  ```
  pi@raspberrypi:~ $ python3
  Python 3.7.3 (default, Apr  3 2019, 05:39:12)
  [GCC 8.2.0] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  ```

* The pip library **spidev** was already installed:

  ```
  pi@raspberrypi:~ $ sudo pip3 install spidev
  Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
  Requirement already satisfied: spidev in /usr/lib/python3/dist-packages (3.3)
  ```

* The pip library **mfrc522** had to be installed:

  ```
  pi@raspberrypi:~ $ sudo pip3 install mfrc522
  Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
  Collecting mfrc522
    Downloading https://files.pythonhosted.org/packages/d5/b5/d33c0634cece0931c3c4e0978b0db58f248045c3b379ccf2d512b76fe044/  mfrc522-0.0.7-py3-none-any.whl
  Requirement already satisfied: spidev in /usr/lib/python3/dist-packages (from mfrc522) (3.3)
  Requirement already satisfied: RPi.GPIO in /usr/lib/python3/dist-packages (from mfrc522) (0.7.0)
  Installing collected packages: mfrc522
  Successfully installed mfrc522-0.0.7
  ```

# Lesson Learned
