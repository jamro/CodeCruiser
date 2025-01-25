from fastapi import FastAPI
import socket
import uvicorn

class WebApp(FastAPI):
  def __init__(self):
    super().__init__()

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