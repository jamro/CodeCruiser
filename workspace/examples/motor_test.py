#!/usr/bin/env python3

from codecruiser import Motors
from time import sleep

motors = Motors()

motors.left_speed = 1
motors.right_speed = 1

sleep(1)

motors.left_speed = 1
motors.right_speed = -1

sleep(0.5)

motors.left_speed = 0
motors.right_speed = 0