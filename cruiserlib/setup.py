from setuptools import setup, find_packages

setup(
  name='codecruiser',
  version='0.1.0',
  packages=find_packages(),
  install_requires=[
    "gpiozero",
  ],
  include_package_data=True,
  description='CodeCruiser library',
  author='Krzysztof Jamroz',
  author_email='kjamroz83@gmail.com',
  python_requires='>=3.6',
)