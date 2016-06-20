## Name: read-real.py
## Author: Aditya Sakhuja
## Date: Monday, 20 June 2016
## Description: 
##


#############################
import sys
from time import sleep
from picamera import PiCamera
try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract

from ocr import read
############################


## Camera Setup and Capture
camera = PiCamera()
camera.start_preview()
sleep(10)
camera.capture('image.jpg')

## Optical Character Recognition
read()

## Translation



