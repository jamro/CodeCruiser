#!/usr/bin/env python3
from codecruiser import WebApp

app = WebApp(enable_camera=True)

@app.get("/")
async def root():
  return app.stream_video()

if __name__ == "__main__":
  import uvicorn
  port = 5000
  print(f"Starting server on http://0.0.0.0:{port}")
  uvicorn.run(app, host="0.0.0.0", port=port)
