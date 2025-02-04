from fastapi import FastAPI, Response
import socket
import uvicorn

class WebApp_mock(FastAPI):
  def __init__(self, *args, enable_camera=False, **kwargs):
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
    pass

  def stream_video(self):
    return Response(content="Camera not available", status_code=503)