from typing import Dict
import board
import adafruit_sht31d

class TemperatureSensor:
    def __init__(self) -> None:
        i2c = board.I2C()
        self.sensor = adafruit_sht31d.SHT31D(i2c)

    def read(self) -> Dict:
        return {
            'hum': self.sensor.relative_humidity,
            'temp': self.sensor.temperature
        }
