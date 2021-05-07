from umqtt.robust import MQTTClient
from sht30 import SHT30
from machine import ADC, Pin
import ubinascii
import machine
import upip
import secrets
import json
import time
from boot import connect, sta_if, toggle_led


def get_mac_address():
    return ubinascii.hexlify(machine.unique_id()).decode('utf-8')


mac = get_mac_address()
mqtt_client = MQTTClient(mac, secrets.MQTT_SERVER)

mq2 = ADC(0)            # gas sensor
sht30 = SHT30(i2c_address=0x44)
button = Pin(0, Pin.IN)  # flash button


while button.value():
    if not sta_if.isconnected():
        connect()

    mqtt_client.reconnect()

    gas = mq2.read()              # read value, 0-1024
    temperature, humidity = sht30.measure()

    print('Temperature:', temperature, 'C, RH:', humidity, '%, ', 'Gas:', gas)

    toggle_led()

    msg_json = json.dumps({
        'mac': mac,
        'temperature': temperature,
        'humidity': humidity,
        'gas': gas
    })
    print(msg_json)

    mqtt_client.publish('/sensors/' + mac, msg_json)

    time.sleep_ms(5_000)
