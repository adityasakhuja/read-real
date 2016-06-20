##########################################################
## Name: ocr.py						##
## Author: Aditya Sakhuja				##
## Date: Monday, 20 June 2016				##
## Description: Performs Optical Character Recognition	##
## using the pytesseract library - a Python wrapper for ##
## Google's Tesseract-OCR.				##
##########################################################


try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract


## Function used by main function to initiate OCR
def read():
	text = pytesseract.image_to_string(Image.open('TestImages/test.jpg'))
	return text

