##########################
## Name: ocr.py
## Author: Aditya Sakhuja
## Date: Monday, 20 June 2016
## Description: Performs Optical Character Recognition
## using the pytesseract library - a Python wrapper for 
## Google's Tesseract-OCR.
##########################


try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('image.jpg')))


#def read():
#	characters = pytesseract.image_to_string(Image.open('image.jpg'))
#	return characters
#
#print read()

