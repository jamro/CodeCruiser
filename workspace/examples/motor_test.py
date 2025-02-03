#!/usr/bin/env python3

from codecruiser import Motors
from time import sleep
import sys

# parse four input arguments. each float value is a speed for each motor index (0 - 3)
args = sys.argv[1:]
if len(args) != 4:
  print("Usage: motor_test.py <motor1_speed> <motor2_speed> <motor3_speed> <motor4_speed>")
  sys.exit(1)

try:
  args = [float(arg) for arg in args]
  for arg in args:
    if arg < -1 or arg > 1:
      raise ValueError("Speed must be between -1 and 1")
except ValueError:
  raise ValueError("All arguments must be valid float numbers between -1 and 1")


motors = Motors()

print("Setting motor1 speed to", args[0])
print("Setting motor2 speed to", args[1])
print("Setting motor3 speed to", args[2])
print("Setting motor4 speed to", args[3])
motors.control_motor(0, args[0])
motors.control_motor(1, args[1])
motors.control_motor(2, args[2])
motors.control_motor(3, args[3])

sleep(2)

print("Stopping all motors")

motors.control_motor(0, 0)
motors.control_motor(1, 0)
motors.control_motor(2, 0)
motors.control_motor(3, 0)

print("Done")