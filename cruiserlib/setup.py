from setuptools import setup, find_packages

setup(
  name='codecruiser',
  version='0.1.1',
  packages=find_packages(),
  install_requires=[
    "gpiozero",
    "watchdog",
    "paramiko",
    "fastapi"
  ],
  include_package_data=True,
  description='CodeCruiser library',
  author='Krzysztof Jamroz',
  author_email='kjamroz83@gmail.com',
  python_requires='>=3.6',
)