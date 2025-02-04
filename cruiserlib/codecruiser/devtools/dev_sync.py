import os
import time
import paramiko
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SyncHandler(FileSystemEventHandler):
  def __init__(self, local_folder, remote_folder, ssh_client):
    self.local_folder = local_folder
    self.remote_folder = remote_folder
    self.ssh_client = ssh_client

  def sync_file(self, src_path):
    """ Upload the modified file to the Raspberry Pi """
    try:
      relative_path = os.path.relpath(src_path, self.local_folder)
      remote_path = os.path.join(self.remote_folder, relative_path).replace("\\", "/")
  
      sftp = self.ssh_client.open_sftp()
      remote_dir = os.path.dirname(remote_path)
      try:
        sftp.chdir(remote_dir)
      except IOError:
        sftp.mkdir(remote_dir)
        sftp.chdir(remote_dir)


      sftp.put(src_path, remote_path)
      sftp.close()
      print(f"Synced: {src_path} -> {remote_path}")

    except Exception as e:
      print(f"Error syncing {src_path}: {e}")

  def delete_remote(self, src_path):
    try:
      relative_path = os.path.relpath(src_path, self.local_folder)
      remote_path = os.path.join(self.remote_folder, relative_path).replace("\\", "/")

      sftp = self.ssh_client.open_sftp()
      try:
        sftp.remove(remote_path)
        print(f"Deleted: {remote_path}")
      except IOError:
        print(f"Failed to delete: {remote_path}")
      sftp.close()

    except Exception as e:
      print(f"Error deleting {src_path}: {e}")

  def sync_all_files(self):
    for root, _, files in os.walk(self.local_folder):
      for file in files:
        self.sync_file(os.path.join(root, file))

  def on_modified(self, event):
    if not event.is_directory:
      self.sync_file(event.src_path)

  def on_created(self, event):
    if not event.is_directory:
      self.sync_file(event.src_path)
      
  def on_deleted(self, event):
    self.delete_remote(event.src_path)
    
def dev_sync(file, host="codecruiser.local", username="pi", workspace_dir="/home/pi/workspace"):

  app_dir = os.path.dirname(os.path.realpath(file))
  app_name = os.path.basename(app_dir)

  print("App name: " + app_name)

  LOCAL_FOLDER = app_dir
  REMOTE_FOLDER = os.path.join(workspace_dir, app_name)

  # Connect to the Raspberry Pi
  print(f"Connecting to {host}...")
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(host, username=username)
  print("Connected!")

  print(f"Syncing {LOCAL_FOLDER} -> {REMOTE_FOLDER}")
  event_handler = SyncHandler(LOCAL_FOLDER, REMOTE_FOLDER, ssh_client)
  event_handler.sync_all_files()
  observer = Observer()
  observer.schedule(event_handler, LOCAL_FOLDER, recursive=True)
  observer.start()

  try:
    while True:
      time.sleep(0.5)
  except KeyboardInterrupt:
    observer.stop()
    ssh_client.close()

  observer.join()

