import subprocess
import threading
import datetime
import shlex
import uuid
import os
import signal
import subprocess

class Process:
    def __init__(self, command, working_directory=None, name="Process"):
        if isinstance(command, str):
            self.command = shlex.split(command)
        else:
            self.command = command
        self.uid = str(uuid.uuid4())
        self.name = name
        self.pid = None
        self.is_running = False
        self.exit_code = None
        self.logs = ""
        self.start_timestamp = None
        self.stop_timestamp = None
        self._process = None
        self._lock = threading.Lock()
        self.working_directory = working_directory

    def _read_stream(self, stream, log_type):
        """Helper method to read a stream line-by-line and update logs."""
        while True:
            line = stream.readline()
            if not line:
                break
            with self._lock:
                self.logs += line

    def _monitor_process(self):
        """Monitors the process and updates properties."""
        try:
            stdout_thread = threading.Thread(target=self._read_stream, args=(self._process.stdout, "STDOUT"))
            stderr_thread = threading.Thread(target=self._read_stream, args=(self._process.stderr, "STDERR"))

            stdout_thread.start()
            stderr_thread.start()

            self._process.wait()

            with self._lock:
                self.exit_code = self._process.returncode
                self.stop_timestamp = datetime.datetime.now()
                self.is_running = False

            stdout_thread.join()
            stderr_thread.join()
        except Exception as e:
            with self._lock:
                self.logs += f"\nError while monitoring process: {str(e)}"
                self.exit_code = self._process.returncode
                self.is_running = False

    def start(self):
        """Starts the process in the background."""
        if self.is_running:
            raise RuntimeError("Process is already running.")

        try:
            self._process = subprocess.Popen(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                cwd=self.working_directory
            )
            self.pid = self._process.pid
            self.is_running = True
            self.start_timestamp = datetime.datetime.now()

            # Start a thread to monitor the process
            monitor_thread = threading.Thread(target=self._monitor_process, daemon=True)
            monitor_thread.start()
        except Exception as e:
            with self._lock:
                self.logs += f"\nFailed to start process: {str(e)}"
                self.is_running = False

    def kill(self):
        """Kills the process if it is running."""
        if not self.is_running:
            raise RuntimeError("Process is not running.")

        try:
            subprocess.run(f"kill -9 $(pgrep -P {self.pid})", shell=True, check=True, executable="/bin/bash")

            print(f"Process {self.pid} has been force-killed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to kill process {self.pid}.")
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        try:
            subprocess.run(["kill", "-9", str(self.pid)], check=True)

            print(f"Process {self.pid} has been force-killed.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to kill process {self.pid}.")
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")