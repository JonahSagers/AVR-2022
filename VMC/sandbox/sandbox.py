from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import AvrFcmVelocityPayload, AvrPcmSetServoOpenClosePayload
from bell.avr.mqtt.payloads import AvrPcmSetBaseColorPayload
import time

from loguru import logger

class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        logger.debug("Hello world (init)")
        #payload = AvrPcmSetBaseColorPayload((128, 232, 142, 0))
        self.send_message("avr/pcm/set_base_color",{"wrgb": [0, 0, 0, 0]})
        payload = AvrPcmSetServoOpenClosePayload(servo=3, action="open")
        self.send_message("avr/pcm/set_servo_open_close",payload)
        logger.debug("Servo Opened")
        time.sleep(1)
        payloadClose = AvrPcmSetServoOpenClosePayload(servo=3, action="close")
        self.send_message("avr/pcm/set_servo_open_close",payloadClose)
        logger.debug("Servo Closed")
    def autonomous_code(self) -> None:
        #while self.enabled:
        logger.debug("button pressed")
    # Here's an example of a custom message handler here.
    # This is what executes whenever a message is received on the "avr/fcm/velocity"
    # topic. The content of the message is passed to the `payload` argument.
    # The `AvrFcmVelocityMessage` class here is beyond the scope of AVR.
    # def show_velocity(self, payload: AvrFcmVelocityPayload) -> None:
    #     vx = payload["vX"]
    #     vy = payload["vY"]
    #     vz = payload["vZ"]
    #     v_ms = (vx, vy, vz)

    #     # Use methods like `debug`, `info`, `success`, `warning`, `error`, and
    #     # `critical` to log data that you can see while your code runs.

    #     # This is what is known as a "f-string". This allows you to easily inject
    #     # variables into a string without needing to combine lots of strings together.
    #     # https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
    #     logger.debug(f"Velocity information: {v_ms} m/s")

    # Here is an example on how to publish a message to an MQTT topic to
    # perform an action
    def open_servo(self) -> None:
        # It's super easy, use the `self.send_message` method with the first argument
        # as the topic, and the second argument as the payload.
        # Pro-tip, if you set `python.analysis.typeCheckingMode` to `basic` in you
        # VS Code preferences, you'll get a red underline if your payload doesn't
        # match the expected format for the topic.
        logger.debug("Hello world (servo)")
        self.send_message("avr/pcm/set_servo_open_close",{"servo": 3, "action": "open"})


if __name__ == "__main__":
    # This is what actually initializes the Sandbox class, and executes it.
    # This is nested under the above condition, as otherwise, if this file
    # were imported by another file, these lines would execute, as the interpreter
    # reads and executes the file top-down. However, whenever a file is called directly
    # with `python file.py`, the magic `__name__` variable is set to "__main__".
    # Thus, this code will only execute if the file is called directly.
    box = Sandbox()
    # The `run` method is defined by the inherited `MQTTModule` class and is a
    # convience function to start processing incoming MQTT messages infinitely.
    box.run()
