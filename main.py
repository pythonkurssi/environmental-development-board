from sht30 import SHT30
from machine import ADC, Pin
import machine

mq2 = ADC(0)            # gas sensor
sht30 = SHT30(i2c_address=0x44)
led = Pin(2, Pin.OUT)   # *inversed* onboard led
button = Pin(0, Pin.IN)  # flash button


def toggle_led():
    led.value(not led.value())


while button.value():
    gas = mq2.read()              # read value, 0-1024
    temperature, humidity = sht30.measure()

    print('Temperature:', temperature, 'C, RH:', humidity, '%, ', 'Gas:', gas)

    toggle_led()

    machine.sleep(1_000)
