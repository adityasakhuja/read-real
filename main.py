import sys
from time import sleep
from picamera import PiCamera
try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract


camera = PiCamera()
camera.resolution = (1024, 768)
camera.capture('test.jpg')

