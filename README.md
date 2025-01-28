# CodeCruiser

**CodeCruiser** is an educational robotics platform for Raspberry Pi. It is targeted at students and hobbyists who want to learn programming of robots and automation systems. **CodeCruiser** provide instructions for building the robot, programming it, and controlling it using a web interface. All construction elements are 3D-printable, and the software is open-source. The platform is based on Raspberry Pi and Python which gives you a lot of flexibility and possibilities for customization and running your own code.


![CodeCruiser Screenshot](docs/render.png)

## Key Features

- **Based on Raspberry Pi** - a powerful and versatile platform giving you a lot of possibilities for software development
- **Wi-Fi connectivity** - control the robot wirelessly
- **Four-wheel drive** - for better traction and stability. The robot can move in any direction and rotate in place. Steering is done by changing the speed of the wheels on each side.
- **Front camera** - capable of 4608x2592 pixel images and 4608x2592@14FPS / 2304x1296@56FPS / 1536x864@120FPS video.
- **Powered by 2x 18650 batteries** - easy to replace and recharge. Built-in voltage meter for monitoring the battery level.
- **RunBerry web interface** - control the robot from your phone or tablet using a web browser
- **CodeCruise Library** - a set of Python modules to streamline the development of robot applications
- **Example applications** - included to get you started
- **3D-printable construction elements** - easy to modify and customize. All files are available in the `hardware` directory.

## Installation

To install **CodeCruiser**, access your Raspberry Pi via SSH and run the following command:

```bash
curl -fsSL https://raw.githubusercontent.com/jamro/CodeCruiser/refs/heads/main/installer.sh | bash
```

This will download and install **CodeCruiser** on your Raspberry Pi. Once the installation is complete, you can access the web interface by navigating to `http://<your_raspberry_pi_ip>` in your browser. To learn more more about Web Interface (aka **RunBerry**), see [RunBerry README](runberry/README.md).

![RunBerry Screenshot](runberry/docs/runberry_ui.png)
