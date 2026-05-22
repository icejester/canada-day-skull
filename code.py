# Trinket IO demo
# Welcome to CircuitPython :)

from touchio import *
from digitalio import *
from analogio import *
from board import *
import time
import neopixel
import random

# Capacitive touch on D3
touch = TouchIn(D1)

# NeoPixel strip (of 16 LEDs) connected on D4
NUMPIXELS = 50
MAXLITBLINKPIXELS = 30
CURLITBLINKPIXELS = 0
neopixels = neopixel.NeoPixel(D3, NUMPIXELS, brightness=1, auto_write=True)
DIRECTION = 1 # 1 == "up"
COLOR = 1 # 1 == "red"

# COLORS
RED = (0, 255, 0)
ORANGE = (255,165,0)
WHITE = (125, 125, 125)
BLUE = (0,0,255)
PURPLE = (0, 255, 255)
GREEN = (255, 0, 0)
CYAN = (255, 0, 255)
PINK = (255, 192, 200)

## COLORPALETTE = [CYAN, BLUE, PURPLE, GREEN, RED, ORANGE]
COLORPALETTE = [GREEN, CYAN, GREEN, BLUE, CYAN, GREEN]

######################### HELPERS ##############################

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

def flicker(idx, rgbVal):
    neopixels[idx] = rgbVal
    if idx > 2 and idx < NUMPIXELS -2:
        neopixels[idx -2] = rgbVal
        neopixels[idx -1] = rgbVal
    time.sleep(0.0125)
    neopixels[idx] = (0, 0, 0)

def rainbowPulse(i):
    for p in range(NUMPIXELS):
        idx = int ((p * 256 / NUMPIXELS) + i)
        neopixels[p] = wheel(idx & 255)

def pulse(mask):
    aPixel = neopixels[0]
    rCur = aPixel[0]
    gCur = aPixel[1]
    bCur = aPixel[2]

    if DIRECTION == 1:
        neopixels.fill((rCur + 10 * mask[0], gCur + 10 * mask[1], bCur + 10 * mask[2]))
    if DIRECTION == 2:
        neopixels.fill((rCur - 10 * mask[0], gCur - 10 * mask[1], bCur - 10 * mask[2]))

def blinkFade(blinkColor):
    currentLitPixels = 0
    # count total lit pixels
    for p in range(NUMPIXELS):
        aPixel = neopixels[p]
        if (aPixel[0] > 10 or aPixel[1] > 10 or aPixel[2] > 10):
            rCur = aPixel[0]
            gCur = aPixel[1]
            bCur = aPixel[2]

            neopixels[p] = (max(0, rCur - 10), max(0, gCur - 10), max(0, bCur - 10))
            currentLitPixels += 1

        elif (aPixel[0] < 10 and aPixel[1] < 10 and aPixel[2] < 10):
            neopixels[p] = ((0,0,0))
            currentLitPixels -= 1

    # if the number of lit pixels is less than max lit pixels
    if currentLitPixels < MAXLITBLINKPIXELS:
        neopixels[random.randint(0, NUMPIXELS - 1)] = blinkColor

######################### MAIN LOOP ##############################

i = 0
colorChange = 0

while True:

    if touch.value:
        neopixels.brightness = 1
        neopixels.fill((0, 0, 0))
        flicker(random.randint(0, (NUMPIXELS-1)),(255, 255, 255))
        colorChange = 1
    else:
        if colorChange:
            if COLOR == 1:
                COLOR = 2
            elif COLOR == 2:
                COLOR = 3
            elif COLOR == 3:
                COLOR = 4
            elif COLOR == 4:
                COLOR = 1

            colorChange = 0

        aPixel = neopixels[0]
        rCur = aPixel[0]
        if rCur >= 244:
            DIRECTION = 2

        elif rCur <= 15:
            DIRECTION = 1

        if COLOR == 1:
            blinkFade((255, 255, 255))
        elif COLOR == 2:
            pulse((1, 1, 1))
        elif COLOR == 3:
            rainbowPulse(i)
        elif COLOR == 4:
            blinkFade(COLORPALETTE[random.randint(0, len(COLORPALETTE) - 1)])

    i = (i+30) % 256  # run from 0 to 255
    neopixels.brightness = .5
    time.sleep(.05) # make bigger to slow down
