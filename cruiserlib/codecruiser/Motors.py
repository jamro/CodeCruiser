from gpiozero import PWMOutputDevice
from time import sleep

class Motors:
  def __init__(self):
    self._motors = [
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
    self._sides = {
      "left": [0, 1],
      "right": [2, 3]
    }
    self._left_speed = 0
    self._right_speed = 0

  @property
  def left_speed(self):
    return self._left_speed
  
  @left_speed.setter
  def left_speed(self, speed):
    self._left_speed = speed
    for motor_index in self._sides["left"]:
      self.control_motor(motor_index, speed)

  @property
  def right_speed(self):
    return self._right_speed
  
  @right_speed.setter
  def right_speed(self, speed):
    self._right_speed = speed
    for motor_index in self._sides["right"]:
      self.control_motor(motor_index, speed)

  def control_motor(self, motor_index, speed):
    motor = self._motors[motor_index]
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
