import os
from fastapi import HTTPException
from .get_mime_type import get_mime_type

def looks_executable(file_path):
  # ends with .sh
  if file_path.endswith(".sh"):
    return True


def get_folder(path):
  workspace_path = os.path.abspath(os.path.join(os.getcwd(), "..", "..", "workspace"))
  folder_path = os.path.abspath(os.path.join(workspace_path, path))

  if not folder_path.startswith(workspace_path):
    path = workspace_path

  if not os.path.isdir(folder_path):
    raise HTTPException(status_code=404, detail="Folder not found")
  
  files = os.listdir(folder_path)

  result = {
    "path": path,
    "files": []
  }

  for file in files:
    file_path = os.path.join(folder_path, file)
    is_directory = os.path.isdir(file_path)
    result["files"].append({
      "name": file,
      "is_directory": is_directory,
      "is_executable": not is_directory and os.access(file_path, os.X_OK),
      "looks_executable": not is_directory and looks_executable(file_path),
      "is_downloadable": not is_directory and get_mime_type(file_path) is not None,
      "path": path + "/" + file if path else file
    })

  # sort result alphabetically by name but with directories first
  result["files"] = sorted(result["files"], key=lambda x: (not x["is_directory"], x["name"]))

  return result

