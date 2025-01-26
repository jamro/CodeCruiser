#!/usr/bin/env python3

from flask import Flask, Response
from picamera2 import Picamera2
import io
import time

app = Flask(__name__)

# Global variable for the camera
picam2 = None

def initialize_camera():
  global picam2
  picam2 = Picamera2()
  camera_config = picam2.create_video_configuration(main={"size": (640, 480)})
  picam2.configure(camera_config)
  picam2.start()

  # Test camera readiness by capturing a single frame
  for _ in range(5):  # Retry up to 5 times
    try:
      stream = io.BytesIO()
      picam2.capture_file(stream, format="jpeg")
      print("Camera is ready!")
      return
    except Exception as e:
      print(f"Camera not ready, retrying: {e}")
      time.sleep(2)

  raise RuntimeError("Camera failed to initialize after multiple attempts.")

@app.route('/')
def video_feed():
  if not picam2:
    return "Camera not initialized. Please restart the server."

  def generate():
    while True:
      stream = io.BytesIO()
      try:
        picam2.capture_file(stream, format="jpeg")
        stream.seek(0)
        frame = stream.read()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        stream.seek(0)
        stream.truncate()
        time.sleep(0.1)  # Adjust frame rate
      except Exception as e:
        print(f"Error capturing frame: {e}")
        break

  return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  try:
    initialize_camera()  # Ensure the camera is ready before starting the server
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=False)
    print(f"Starting server on http://0.0.0.0:{port}")
  finally:
    if picam2:
      picam2.stop()