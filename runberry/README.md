# RunBerry

**RunBerry** is a web interface for running executables on your Raspberry Pi. It allows you to browse your filesystem, select an executable, and run it. The output of the executable will be displayed in the browser. You can also manage the running processes and stop them if needed. The user interface is optimized for mobile devices, so you can control your Raspberry Pi from your phone or tablet.

![RunBerry Screenshot](docs/runberry_ui.png)

## Key Features
- Browse your filesystem
- Run executables (with custom arguments)
- View logs and output
- Manage running processes
- Download files

## Workspace

All files available through the web interface are located in the `/home/pi/CodeCruiser/workspace` directory. You can upload your own executables to this directory and run them using **RunBerry**. The workspace contains `examples` directory with some example executables that you can try.

All the commands are execured as root user. The web interface is running on port 80, so you don't need to specify the port in the URL.

## System Tools

**RunBerry** comes with a set of system tools located in the `/home/pi/CodeCruiser/workspace/system` directory. These tools allow you to perform various tasks on your Raspberry Pi:

- `sys_update.sh` - Update the system and install the latest version of **RunBerry**.
- `bash.sh` - Run any bash command on your Raspberry Pi. Provide the command as an argument.

## Development

**RunBerry** is built using Python and React. The backend is a FastAPI server that runs on the Raspberry Pi (see `backend` directory). The frontend is a React app that is served by the backend (see `frontend` directory). The communication between the frontend and the backend is done using API calls.

To make development easier, you can run the frontend and the backend on your local machine. The frontend will be available at `http://localhost:3000` and the backend at `http://localhost:8000`. To start the development server, run the following commands:

```bash
./scripts/dev.sh
```

This will start the backend and the frontend in development mode. The frontend will automatically reload when you make changes to the source code.

### Building

Frontend build is stored in the `frontend/build` directory and committed to the repository. It makes installation process faster and easier. Remember to rebuild the frontend after making changes to the source code before committing them. To build the frontend, run the following command:

```bash
./scripts/build.sh
```
