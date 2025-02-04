
class Motors_mock:
  def __init__(self):
    print("It seems you try to run the code on a non-Raspberry Pi device. Motors are disabled.")
    self._left_speed = 0
    self._right_speed = 0

  @property
  def left_speed(self):
    return self._left_speed
  
  @left_speed.setter
  def left_speed(self, speed):
    print(f"Left speed: {speed}")
    self._left_speed = speed

  @property
  def right_speed(self):
    return self._right_speed
  
  @right_speed.setter
  def right_speed(self, speed):
    print(f"Right speed: {speed}")
    self._right_speed = speed

  def control_motor(self, motor_index, speed):
    print(f"Motor {motor_index} speed: {speed}")

