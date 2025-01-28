# CodeCruiser

**CodeCruiser** is an educational robotics platform for Raspberry Pi. It is targeted at students and hobbyists who want to learn programming of robots and automation systems. **CodeCruiser** provide instructions for building the robot, programming it, and controlling it using a web interface. All construction elements are 3D-printable, and the software is open-source. The platform is based on Raspberry Pi and Python which gives you a lot of flexibility and possibilities for customization and running your own code.


![CodeCruiser Screenshot](docs/render.png)


## Installation

To install **CodeCruiser**, access your Raspberry Pi via SSH and run the following command:

```bash
curl -fsSL https://raw.githubusercontent.com/jamro/CodeCruiser/refs/heads/main/installer.sh | bash
```

This will download and install **CodeCruiser** on your Raspberry Pi. Once the installation is complete, you can access the web interface by navigating to `http://<your_raspberry_pi_ip>` in your browser. To learn more more about Web Interface (aka **RunBerry**), see [RunBerry README](runberry/README.md).

![RunBerry Screenshot](runberry/docs/runberry_ui.png)
