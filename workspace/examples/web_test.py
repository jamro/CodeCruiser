#!/usr/bin/env python3
from codecruiser import WebApp, Motors
from fastapi import FastAPI
from fastapi.responses import FileResponse
from time import sleep

app = WebApp()
motors = Motors()

@app.get("/")
def read_root():
    return FileResponse("web_test.html")

@app.get("/api/forward")
def go_forward():
    motors.left_speed = 1
    motors.right_speed = 1
    sleep(0.5)
    motors.left_speed = 0
    motors.right_speed = 0
    return {"status": "ok"}

@app.get("/api/backward")
def go_backward():
    motors.left_speed = -1
    motors.right_speed = -1
    sleep(0.5)
    motors.left_speed = 0
    motors.right_speed = 0
    return {"status": "ok"}

@app.get("/api/left")
def go_left():
    motors.left_speed = -1
    motors.right_speed = 1
    sleep(0.5)
    motors.left_speed = 0
    motors.right_speed = 0
    return {"status": "ok"}

@app.get("/api/right")
def go_right():
    motors.left_speed = 1
    motors.right_speed = -1
    sleep(0.5)
    motors.left_speed = 0
    motors.right_speed = 0
    return {"status": "ok"}

app.start_server()