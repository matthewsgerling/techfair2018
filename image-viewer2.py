#!/usr/bin/env python
import time
import sys
import curses

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

#print repr(sys.argv)
#if len(sys.argv) < 2:
#    sys.exit("Require image arguments")
#else:
#    image_file = sys.argv[1]

imageRight = Image.open("/home/pi/Pictures/Link3.png")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.brightness = 100
x = 18
y = 18

matrix = RGBMatrix(options = options)

# Make image fit our screen.
imageRight.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

matrix.SetImage(imageRight.convert('RGB'), x, y)

try:
    print("Press CTRL-C to stop.")
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(0, 0, 'right')
            x = x + 1
            matrix.Clear()
            matrix.SetImage(imageRight.convert('RGB'), x, y)
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
            x = x - 1
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up   ')
            y = y - 1
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
            y = y + 1

except KeyboardInterrupt:
    sys.exit(0)

finally:
    corses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
