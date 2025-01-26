#!/usr/bin/env python3
from codecruiser import WebApp

app = WebApp()

@app.get("/")
def stream_video():
  return app.stream_video()

app.start_server()