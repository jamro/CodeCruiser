#!/usr/bin/python3
import smbus
import time

# I2C Address of ADXL345
ADXL345_I2C_ADDR = 0x53

# ADXL345 Registers
POWER_CTL = 0x2D   # Power control register
DATA_FORMAT = 0x31 # Data format register
DATAX0 = 0x32      # X-axis data 0
DATAX1 = 0x33      # X-axis data 1
DATAY0 = 0x34      # Y-axis data 0
DATAY1 = 0x35      # Y-axis data 1
DATAZ0 = 0x36      # Z-axis data 0
DATAZ1 = 0x37      # Z-axis data 1

# Initialize I2C bus
bus = smbus.SMBus(1)  # Use I2C bus 1

# Initialize ADXL345
def initialize_adxl345():
  bus.write_byte_data(ADXL345_I2C_ADDR, POWER_CTL, 0x08)  # Set to measurement mode
  bus.write_byte_data(ADXL345_I2C_ADDR, DATA_FORMAT, 0x08)  # Set full resolution mode (±2g)

# Read raw data from ADXL345
def read_raw_data(addr):
  low = bus.read_byte_data(ADXL345_I2C_ADDR, addr)
  high = bus.read_byte_data(ADXL345_I2C_ADDR, addr + 1)
  value = (high << 8) | low  # Combine high and low byte
  if value > 32767:  # Convert to signed value
    value -= 65536
  return value

# Read accelerometer data
def read_acceleration():
  x = read_raw_data(DATAX0)
  y = read_raw_data(DATAY0)
  z = read_raw_data(DATAZ0)
  return x, y, z

initialize_adxl345()
print("Reading ADXL345 accelerometer data...")

while True:
  x, y, z = read_acceleration()
  print(f"X: {x}, Y: {y}, Z: {z}")
  time.sleep(0.5)  # Read every 500ms