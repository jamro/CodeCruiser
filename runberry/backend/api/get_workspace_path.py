import os
import json

def get_workspace_path():

  config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "config.json"))
  with open(config_path, "r") as file:
    config = json.load(file)

  workspace_dir = config["workspace_dir"]
  # if workspace_dir is not starting with /, it is a relative path
  if not workspace_dir.startswith("/"):
    workspace_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", workspace_dir))
  
  return workspace_dir

# main
if __name__ == "__main__":
  get_workspace_path()