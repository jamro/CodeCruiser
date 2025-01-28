from fastapi.testclient import TestClient
from main import app
from time import sleep

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "<html" in response.text

    
def test_read_files():
    response = client.get("/api/files")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    json = response.json()
    assert "files" in json
    files = json["files"]
    assert len(files) > 0

    # find examples folder
    example_folder = None
    for f in files:
        if f["name"] == "examples":
            example_folder = f
            break
        
    assert example_folder is not None
    assert example_folder["is_directory"] == True
    assert example_folder["name"] == "examples"

def test_read_files_example():
    response = client.get("/api/files/examples")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    json = response.json()
    assert "files" in json
    files = json["files"]
    assert len(files) > 0

    # find example file
    example_file = None
    for f in files:
        if f["name"] == "hello_world.sh":
            example_file = f
            break
    assert example_file is not None
    assert example_file["is_directory"] == False
    assert example_file["is_executable"] == True
    assert example_file["name"] == "hello_world.sh"

def test_file_location_not_found():
    response = client.get("/api/files/not_found")
    assert response.status_code == 404
    assert response.headers["content-type"] == "application/json"
    json = response.json()
    assert "detail" in json
    assert json["detail"] == "Folder not found"

def test_process_empty():
    response = client.get("/api/processes")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    processes = response.json()
    assert len(processes) == 0

def test_process_create():
    response = client.post("/api/processes", json={"path": "examples/hello_world.sh", "args": ""})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    process = response.json()
    assert "uid" in process
    uid = process["uid"]

    response = client.get(f"/api/processes")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    processes = response.json()
    assert len(processes) >= 1

    # find the process
    process = None
    for p in processes:
        if p["uid"] == uid:
            process = p
            break

    assert process["uid"] == uid
    assert process["name"] == "hello_world.sh"
    

def test_process_kill():
    response = client.post("/api/processes", json={"path": "examples/ping.sh", "args": ""})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    process = response.json()
    assert "uid" in process
    uid = process["uid"]

    response = client.get(f"/api/processes")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    processes = response.json()
    assert len(processes) >= 1
    process = None
    for p in processes:
        if p["uid"] == uid:
            process = p
            break
        
    assert process is not None
    assert process["uid"] == uid
    assert process["is_running"] == True

    response = client.delete(f"/api/processes/{uid}")
    assert response.status_code == 200

    response = client.get(f"/api/processes")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    processes = response.json()
    assert len(processes) >= 1
    process = None
    for p in processes:
        if p["uid"] == uid:
            process = p
            break
        
    assert process is not None
    assert process["uid"] == uid
    assert process["is_running"] == False

def test_process_logs():
    response = client.post("/api/processes", json={"path": "examples/hello_world.sh", "args": ""})
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    process = response.json()
    assert "uid" in process
    uid = process["uid"]

    sleep(0.1)

    response = client.get(f"/api/processes/{uid}/logs")
    assert response.status_code == 200
    logs = response.content
    assert logs is not None
    assert len(logs) > 0

    assert b"Hello, my beautiful world!" in logs

    
def test_process_logs_not_found():
    response = client.get(f"/api/processes/not_found/logs")
    assert response.status_code == 404
    json = response.json()
    assert "detail" in json
    assert json["detail"] == "Process not found"