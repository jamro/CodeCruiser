from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from picamera2 import Picamera2
import socket
import uvicorn
import io
import asyncio
from time import sleep

class WebApp(FastAPI):
  def __init__(self, *args, enable_camera=False, **kwargs):

    async def lifespan(app: FastAPI):
      """Lifespan context manager for FastAPI."""
      try:
          self.initialize_camera()
          yield
      finally:
          if self.picam2:
              self.picam2.stop()

    if enable_camera:
      kwargs['lifespan'] = lifespan

    super().__init__(*args, **kwargs)
    self.picam2 = None
    self.picam2_ready = False
    self.picam2_config = {
      "width": 640,
      "height": 480,
      "fps": 60
    }

  def find_available_port(self, start_port=9000, end_port=9100):
    for port in range(start_port, end_port + 1):
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
          s.bind(("0.0.0.0", port))
          return port
        except OSError:
          continue
    raise RuntimeError(f"No available ports in range {start_port}-{end_port}")
  
  def start_server(self):
    try:
      port = self.find_available_port()
      print(f"Starting server on http://0.0.0.0:{port}")
      uvicorn.run(self, host="0.0.0.0", port=port)
    except RuntimeError as e:
      print(str(e))

  def initialize_camera(self):
    self.picam2 = Picamera2()
    camera_config = self.picam2.create_video_configuration(main={"size": (self.picam2_config["width"], self.picam2_config["height"])})
    self.picam2.configure(camera_config)
    self.picam2.start()

    # Test camera readiness by capturing a single frame
    for _ in range(5):  # Retry up to 5 times
      try:
        stream = io.BytesIO()
        self.picam2.capture_file(stream, format="jpeg")
        print("Camera is ready!")
        return
      except Exception as e:
        print(f"Camera not ready, retrying: {e}")
        sleep(2)

    raise RuntimeError("Camera failed to initialize after multiple attempts.")

  def stream_video(self):
    async def video_stream_generator():
      while True:
        stream = io.BytesIO()
        try:
          self.picam2.capture_file(stream, format="jpeg")
          stream.seek(0)
          frame = stream.read()
          yield (b"--frame\r\n"
              b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
          await asyncio.sleep(0.1)  # Limit to ~10 FPS
        except Exception as e:
          print(f"Error capturing frame: {e}")
          break

    if not self.picam2:
      return Response("Camera not initialized. Please restart the server.", status_code=500)

    return StreamingResponse(video_stream_generator(), media_type="multipart/x-mixed-replace; boundary=frame")