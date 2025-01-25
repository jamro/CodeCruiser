#!/usr/bin/env python3

from codecruiser import Motors
from time import sleep

motors = Motors()

print("Moving forward...")
motors.left_speed = 1
motors.right_speed = 1
sleep(1)

print("Stopping...")
motors.left_speed = 0
motors.right_speed = 0
sleep(0.5)

print("Turning...")
motors.left_speed = 1
motors.right_speed = -1
sleep(0.5)

print("Done!")
motors.left_speed = 0
motors.right_speed = 0