#############################
## Name: read-real.py
## Author: Aditya Sakhuja
## Date: Monday, 20 June 2016
## Description: 
##
#############################


import sys
from time import sleep

## For Image Capture
from picamera import PiCamera

## For Optical Character Recognition
from ocr import read

## For Translation
from translation import translate



## Camera Setup and Capture
camera = PiCamera()
camera.start_preview()
sleep(10)
camera.capture('image.jpg')

## Optical Character Recognition
text = read()
for letter in text:
	braille = translate(letter)
	print letter + braille

## Translation



