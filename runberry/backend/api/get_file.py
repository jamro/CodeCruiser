from .get_mime_type import get_mime_type
from fastapi import HTTPException
import os
from fastapi.responses import FileResponse
from .get_workspace_path import get_workspace_path

def get_file(path):
  mimetype = get_mime_type(path)

  if mimetype is None:
    raise HTTPException(status_code=404, detail="File not found")
  
  workspace_path = get_workspace_path()
  file_path = os.path.abspath(os.path.join(workspace_path, path))

  if not file_path.startswith(workspace_path):
    raise HTTPException(status_code=404, detail="File not found")

  if not os.path.isfile(file_path):
    raise HTTPException(status_code=404, detail="File not found")
  
  return FileResponse(file_path, media_type=mimetype)
