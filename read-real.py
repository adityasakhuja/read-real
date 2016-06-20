#####################################################################
## Name: read-real.py						   ##
## Author: Aditya Sakhuja					   ##
## Date: Monday, 20 June 2016					   ##
## Description: This program combines all the functionalities	   ##
## of the Read Real pen. It uses the PiCamera library to  	   ##
## capture an image and store it in the working directory. 	   ##
## The OCR function is then called to read the text from 	   ##
## the image and store it in a string. The translation function	   ##
## then takes as input each character from this string and 	   ##
## finds its corresponding 6-bit braille code in the lookup table. ##
## This code is then transmitted to the Arduino board via a Serial ##
## connection and printed in the console for easy debugging.	   ##
#####################################################################

import os
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
#camera.start_preview()
#sleep(10)
camera.capture('image.jpg')

## Optical Character Recognition
text = read()

## Translation
for letter in text:
	braille = translate(letter)
	print letter + " " + braille


## Delete image file captured
os.remove("/home/pi/Desktop/read-real/image.jpg")

