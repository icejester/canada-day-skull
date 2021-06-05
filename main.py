# Trinket IO demo
# Welcome to CircuitPython :)

from touchio import *
from digitalio import *
from analogio import *
from board import *
import time
import neopixel

# Capacitive touch on D3
touch = TouchIn(D1)

# NeoPixel strip (of 16 LEDs) connected on D4
NUMPIXELS = 18
neopixels = neopixel.NeoPixel(D3, NUMPIXELS, brightness=.1, auto_write=True)

######################### HELPERS ##############################

# Helper to convert analog input to voltage
# def getVoltage(pin):
#     return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return (0, 0, 0)
    if (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

######################### MAIN LOOP ##############################

i = 0;
while True:

  # also make the neopixels swirl around
  for p in range(NUMPIXELS):
      idx = int ((p * 256 / NUMPIXELS) + i)
      neopixels[p] = wheel(idx & 255)
  neopixels.show()

  if touch.value:
      print("D3 touched!")

  i = (i+20) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down
