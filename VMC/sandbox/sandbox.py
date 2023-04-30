import time
import math

from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import AvrPcmSetBaseColorPayload
from loguru import logger

class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        logger.debug("Class initialized")

if __name__ == "__main__":
    box = Sandbox()
    box.run_non_blocking()
    placeholder = 0
    while True:
        placeholder += 0.08
        saturationW = 50 + (math.sin(placeholder) * 50)
        saturationR = 50 + (math.sin(placeholder + 1.57) * 50)
        saturationG = 50 + (math.sin(placeholder + 3.14) * 50)
        saturationB = 50 + (math.sin(placeholder + 4.71) * 50)
        box.send_message("avr/pcm/set_base_color", {"wrgb": [int(saturationW), int(saturationR), int(saturationG), int(saturationB)]})
        #box.send_message("avr/pcm/set_servo_abs", {"servo": 3, "absolute": int(700 + saturationR * 15)})
        logger.debug(saturationR)
        time.sleep(0.0166)