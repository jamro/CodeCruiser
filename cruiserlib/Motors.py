from gpiozero import PWMOutputDevice
from time import sleep

class Motors:
  def __init__(self):
    self.motors = [
      {
        "enable": PWMOutputDevice(17),
        "forward": PWMOutputDevice(22),
        "backward": PWMOutputDevice(27),
        "reverse": True
      },
      {
        "enable": PWMOutputDevice(25),
        "forward": PWMOutputDevice(23),
        "backward": PWMOutputDevice(24),
        "reverse": True
      },
      {
        "enable": PWMOutputDevice(10),
        "forward": PWMOutputDevice(9),
        "backward": PWMOutputDevice(11),
        "reverse": False
      },
     {
        "enable": PWMOutputDevice(12),
        "forward": PWMOutputDevice(8),
        "backward": PWMOutputDevice(7),
        "reverse": True
      },
    ]

  def control_motor(self, motor_index, speed):
    motor = self.motors[motor_index]
    if motor["reverse"]:
      speed = -speed

    if speed > 0:
      motor["forward"].value = speed
      motor["backward"].value = 0
    elif speed < 0:
      motor["forward"].value = 0
      motor["backward"].value = -speed
    else:
      motor["forward"].value = 0
      motor["backward"].value = 0
    motor["enable"].value = abs(speed)

    


motors = Motors()
motors.control_motor(0, 1)
motors.control_motor(1, 1)
motors.control_motor(2, 1)
motors.control_motor(3, 1)

sleep(1)

motors.control_motor(0, 0)
motors.control_motor(1, 0)
motors.control_motor(2, 0)
motors.control_motor(3, 0)
