#!/usr/bin/env python3

from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from picamera2 import Picamera2
import io
import time
import asyncio

# Global variable for the camera
picam2 = None

def initialize_camera():
    """Initialize the Picamera2 camera."""
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


async def lifespan(app: FastAPI):
    """Lifespan context manager for FastAPI."""
    try:
        initialize_camera()
        yield
    finally:
        if picam2:
            picam2.stop()


app = FastAPI(lifespan=lifespan)


async def video_stream_generator():
    """Asynchronous generator to stream video frames."""
    while True:
        stream = io.BytesIO()
        try:
            picam2.capture_file(stream, format="jpeg")
            stream.seek(0)
            frame = stream.read()
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
            await asyncio.sleep(0.1)  # Limit to ~10 FPS
        except Exception as e:
            print(f"Error capturing frame: {e}")
            break


@app.get("/")
async def root():
    """Root endpoint to serve the video stream."""
    if not picam2:
        return Response("Camera not initialized. Please restart the server.", status_code=500)

    return StreamingResponse(video_stream_generator(), media_type="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    import uvicorn
    port = 5000
    print(f"Starting server on http://0.0.0.0:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)