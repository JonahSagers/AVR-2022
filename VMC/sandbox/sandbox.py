import time

from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import AvrFcmVelocityPayload, AvrPcmSetBaseColorPayload
from loguru import logger
placeholder = 1

class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        logger.debug("Class initialized")
        self.topic_map = {"avr/fcm/velocity": self.show_velocity}
        if placeholder == 1:
            box.show_velocity()
            placeholder = 0

    def show_velocity(self, payload: AvrFcmVelocityPayload) -> None:
        vx = payload["vX"]
        vy = payload["vY"]
        vz = payload["vZ"]
        v_ms = (vx, vy, vz)
        print(f"Velocity information: {v_ms} m/s")

    def hello_world(self) -> None:
        logger.debug("Hello world")

        payload = AvrPcmSetBaseColorPayload(wrgb=(0, 100, 0, 0))
        self.send_message("avr/pcm/set_base_color", payload)

        logger.debug("Light changed")


if __name__ == "__main__":
    box = Sandbox()
    box.run_non_blocking()
    
    box.hello_world()

    while True:
        time.sleep(0.1)