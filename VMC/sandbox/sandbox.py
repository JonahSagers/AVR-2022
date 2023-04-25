from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import AvrFcmVelocityPayload, AvrPcmSetServoOpenClosePayload
from bell.avr.mqtt.payloads import AvrPcmSetBaseColorPayload
import time

from loguru import logger

class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        logger.debug("Hello world (init)")
        self.send_message("avr/pcm/set_base_color",{"wrgb": [0, 100, 0, 0]})
        logger.debug("Servo Opened")
if __name__ == "__main__":
    box = Sandbox()
    box.run()
