#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

print repr(sys.argv)
if len(sys.argv) < 4:
    sys.exit("Require two image arguments")
else:
    image_file = sys.argv[1]
    image_file2 = sys.argv[2]
    image_file3 = sys.argv[3]

image = Image.open(image_file)
image2 = Image.open(image_file2)
image3 = Image.open(image_file3)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
 
matrix = RGBMatrix(options = options)

# Make image fit our screen.
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
image2.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(image.convert('RGB'))

try:
    print("Press CTRL-C to stop.")
    while True:
        matrix.Clear()
        matrix.SetImage(image.convert('RGB'))
        time.sleep(1)
        matrix.Clear()
        matrix.SetImage(image2.convert('RGB'))
        time.sleep(1)
        matrix.Clear()
        matrix.SetImage(image3.convert('RGB'))
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(0)
    
