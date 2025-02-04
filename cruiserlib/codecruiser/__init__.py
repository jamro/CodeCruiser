try:
  from .Motors import Motors
except ImportError:
  print("ImportError: Motors not available. Using mock implementation.")
  from .Motors_mock import Motors_mock as Motors
  pass

try:
  from .WebApp import WebApp
except ImportError:
  print("ImportError: WebApp not available fully. Using mock implementation.")
  from .WebApp_mock import WebApp_mock as WebApp
  pass