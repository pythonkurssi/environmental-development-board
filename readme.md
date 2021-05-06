# AZ-Envy - environmental development board demo

## Details

Sensor          | Pin / Address
----------------|--------------
MQ2 gas sensor  | ADC 0
SHT30 temperature and humidity sensor | I2C address 0x44
Onboard led     | Pin 2 (inversed: 1=off, 0=on)
Flash button    | Pin 0 (HIGH Run, LOW Flash)


## Getting started

> *"The micro-USB jack of the AZ-Envy is used for power supply. To program the microcontroller chip, you need a separately available USB to serial adapter like our FT232RL module."*
>
> https://www.az-delivery.de/en/products/az-envy

Connect your FT232RL module to the headers of your AZ-Envy development board, and the FT232RL to your computer's USB port. You will also need to power the board with a separate USB cable, which can be connected to either a power supply or your PC.


## Erasing flash

When erasing the flash, first type in the command `py -m esptool --port COM3 erase_flash`. When esptool starts connecting, hold the flash button and click the reset button. When connection is established, you can release the flash button.

```
> py -m esptool --port COM3 erase_flash
esptool.py v3.0
Serial port COM3
Connecting........_
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
Crystal is 26MHz
MAC: e8:db:84:94:2a:fe
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 15.9s
Hard resetting via RTS pin...
```


## Installing MicroPython

When installing MicroPython, repeat the flash and reset button procedure required when erasing the flash: hold the flash button and click the reset button.

```
> py -m esptool --port COM3 --baud 460800 write_flash --flash_size=detect 0 .\esp8266-20210418-v1.15.bin
esptool.py v3.0
Serial port COM3
Connecting......
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
Crystal is 26MHz
MAC: e8:db:84:94:2a:fe
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 460800
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Flash params set to 0x0040
Compressed 632632 bytes to 415633...
Wrote 632632 bytes (415633 compressed) at 0x00000000 in 9.4 seconds (effective 537.5 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```


## Credits

SHT30 library https://github.com/rsc1975/micropython-sht30 is created by Roberto Sánchez and licensed with Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0.