
from typing import Dict
import Adafruit_DHT


class TemperatureSensor:
    def __init__(self, pin) -> None:
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin

    def read(self) -> Dict:
        humidity, temperature = Adafruit_DHT.read_retry(
            self.sensor,
            self.pin,
            delay_seconds=1
        )
        return {
            'humidity': humidity,
            'temperature': temperature
        }
