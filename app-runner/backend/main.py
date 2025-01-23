from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
from api import get_folder
from process import ProcessManager

process_manager = ProcessManager()
app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to specific domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred."},
    )

class ExecuteRequest(BaseModel):
    path: str
    args: str

# API endpoints
@app.get("/api/status")
def get_status():
    return {"status": "Running"}

@app.get("/api/files/{path:path}")
def get_workspace(path: str):
    return get_folder(path)

@app.get("/api/files")
def get_workspace_root():
    return get_workspace("")

@app.get("/api/processes")
@app.get("/api/processes/")
def get_process():
    result = []
    for p in process_manager.get_processes():
        result.append({
            "pid": p.pid,
            "uid": p.uid,
            "name": p.name,
            "command": p.command,
            "working_directory": p.working_directory,
            "is_running": p.is_running,
            "start_timestamp": p.start_timestamp,
            "stop_timestamp": p.stop_timestamp,
        })
    return result

@app.post("/api/processes")
def create_process(request: ExecuteRequest):
    process_id = process_manager.execute(request.path, request.args)
    return {
        "path": request.path,
        "args": request.args
    }

@app.get("/api/processes/{uid}/logs")
def get_process_logs(uid: str):
    process = process_manager.get_process_by_uid(uid)
    if process is None:
        raise HTTPException(status_code=404, detail="Process not found")
    return process.logs

# Serve the React build directory as static files
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend/build")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")