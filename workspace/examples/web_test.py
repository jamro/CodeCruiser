#!/usr/bin/env python3

from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

def find_available_port(start_port: int, end_port: int) -> int:
    """Find the first available port in the given range."""
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("0.0.0.0", port))
                return port
            except OSError:
                continue
    raise RuntimeError(f"No available ports in range {start_port}-{end_port}")

if __name__ == "__main__":
    import uvicorn
    try:
        port = find_available_port(9000, 9100)
        print(f"Starting server on port {port}")
        uvicorn.run(app, host="0.0.0.0", port=port)
    except RuntimeError as e:
        print(str(e))