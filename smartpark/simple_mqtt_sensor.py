""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""
import random
import sys

import mqtt_device
from sense_emu import SenseHat

import tomli

from config_parser import parse_config

from sys import argv

CONFIG_FILE = "config.toml"
DEVICE_NUMBER = int(argv[1]) - 1


class Sensor(mqtt_device.MqttDevice):
    def __init__(self, config):
        super().__init__(config)
        self.temperature_sensor = SenseHat()

    @property
    def temperature(self):
        self.temperature_sensor.clear()
        return self.temperature_sensor.get_temperature()

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish(f'lot/moondalup/{self.name}/{self.topic_qualifier}', message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            print("Press E when 🚗 entered!")
            print("Press X when 🚖 exited!")
            detection = input("E or X> ").upper()
            if detection == 'E':
                self.on_detection(f"entered, {self.temperature}")
            else:
                self.on_detection(f"exited, {self.temperature}")


if __name__ == '__main__':
    # TODO: Read previous config from file instead of embedding
    config = parse_config()
    sensor = Sensor(config['Sensors'][DEVICE_NUMBER])
    print(f"{sensor.name} initialized")

    sensor.start_sensing()
