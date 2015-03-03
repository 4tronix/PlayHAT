#!/usr/bin/python
# servoTest.py

import time, random
from neopixel import *

# LED strip configuration:
LED_COUNT      = 9       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 40     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Define list of Dice configurations
digits = [[0,0,0,0,0,0,0,0,0],  # 0
          [0,0,0,0,1,0,0,0,0],  # 1
          [1,0,0,0,0,0,0,0,1],  # 2
          [1,0,0,0,1,0,0,0,1],  # 3
          [1,0,1,0,0,0,1,0,1],  # 4
          [1,0,1,0,1,0,1,0,1],  # 5
          [1,1,1,0,0,0,1,1,1]]  # 6
           

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

def clearStrip(strip):
    for i in range(0, strip.numPixels()):
        strip.setPixelColor(i, 0)
    strip.show()

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
    strip.show()
    time.sleep(wait_ms/1000.0)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def doDigit(digit, colour):
    for i in range(9):
        if digits[digit][i] > 0:
            strip.setPixelColor(i, colour)
        else:
            strip.setPixelColor(i, 0)
    strip.show()
                                

    
try:
    while True:
        num = 0
#        colorWipe(strip, Color(255, 0, 0))  # Red wipe
#        colorWipe(strip, Color(0, 255, 0))  # Blue wipe
#        colorWipe(strip, Color(0, 0, 255))  # Green wipe
#        rainbowCycle(strip)
        for i in range(1, 30):
            num = random.randrange(1, 7)
            doDigit(num, Color(255,0,0))
            time.sleep(0.1)
        doDigit(num, Color(0,255,0))
        time.sleep(3)

except KeyboardInterrupt:
    print

finally:
    clearStrip(strip)
