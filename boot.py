# This file is executed on every boot (including wake-boot from deepsleep)
import network
import machine
from machine import Pin
import uos
import gc
import esp
import secrets
import time
import upip

esp.osdebug(None)

led = Pin(2, Pin.OUT)   # *inversed* onboard led


def toggle_led():
    led.value(not led.value())


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

print('Connecting to ' + secrets.WIFI_SSID)


def connect():
    while not sta_if.isconnected():
        toggle_led()
        print(".")
        time.sleep_ms(500)
        # sta_if.connect()

    print('network config:', sta_if.ifconfig())


connect()

upip.install('micropython-umqtt.robust')
upip.install('micropython-umqtt.simple')

gc.collect()
