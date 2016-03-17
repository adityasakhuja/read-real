import sys
try: 
	import Image
except ImportError:
	from PIL import Image
import pytesseract

output = open('output.txt', 'w')

output.write(pytesseract.image_to_string(Image.open(sys.argv[1])))

output.close()
