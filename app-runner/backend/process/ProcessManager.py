from .Process import Process
import shlex
import os
from fastapi import HTTPException

class ProcessManager:
    
    def __init__(self):
        self.processes = []

    def execute(self, path: str, args: str):
        print(f"Executing {path} with args {args}")

        # get current working directory and command from path
        cwd = "/".join(path.split("/")[:-1])

        workspace_path = os.path.abspath(os.path.join(os.getcwd(), "..", "..", "workspace"))
        cwd = os.path.abspath(os.path.join(workspace_path, cwd))
        full_path = os.path.abspath(os.path.join(workspace_path, path))
    
        if not os.path.exists(full_path):
          raise HTTPException(status_code=404, detail="Folder not found")
        
        # check if file at full_path has execute permissions. 
        # if not add them leaving the rest of the permissions as they are
        if not os.access(full_path, os.X_OK):
          os.chmod(full_path, os.stat(full_path).st_mode | 0o111)

        p = Process(workspace_path + "/" + path + " " + args, cwd, name=path.split("/")[-1])
        self.processes.append(p)
        p.start()

    def get_processes(self):
        return self.processes
      
    def get_process_by_uid(self, uid):
        for process in self.processes:
            if process.uid == uid:
                return process
        return None