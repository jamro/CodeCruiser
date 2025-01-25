#!/usr/bin/env python3
from codecruiser import WebApp
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = WebApp()

@app.get("/")
def read_root():
    return FileResponse("web_test.html")


@app.get("/api/reverse")
def reverse_string(text):
    return {"reversed": text[::-1]}
    

app.start_server()