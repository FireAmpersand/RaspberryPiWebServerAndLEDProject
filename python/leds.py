import time
from neopixel import *
import argparse
import random

#LED Strip One Setup
STRIP_LEDS = 756 #Total LEDS For Strip
STRIP_LEDS_PER_STRAND = 108 #LEDS PER BEAM
STRIP_PIN = 18 #LED Pin For Strip 
STRIP_FREQ = 800000
STRIP_DMA = 10
STRIP_BRIGHTNESS = 127
STRIP_INVERT = False
STRIP_CHANNEL = 0
STRIP = Adafruit_NeoPixel(STRIP_LEDS, STRIP_PIN, STRIP_FREQ, STRIP_DMA, STRIP_INVERT, STRIP_BRIGHTNESS, STRIP_CHANNEL)
STRIP.begin()

MASTER_LOOP = False

def newBrightness():
    STRIP.setBrightness(STRIP_BRIGHTNESS)

def colorwipe(color, wait_ms=1):
    for i in range(STRIP.numPixels()):
        STRIP.setPixelColor(i, color)
        STRIP.show()
        time.sleep(wait_ms/1000.0)

def pulseColor(color, wait_ms=100):
    for i in range(STRIP.numPixels()):
        STRIP.setPixelColor(i, color)
    STRIP.show()
    time.sleep(wait_ms/1000.0)
    for t in range(STRIP.numPixels()):
        STRIP.setPixelColor(t, Color(0,0,0))
    STRIP.show()
    time.sleep(wait_ms/1000.0)

def runRave():
    while MASTER_LOOP == True:
        pulseColor(Color(0,255,0))

def theaterChase(color,wait_ms=50, times=10):
    for j in range(times):
        for q in range(3):
            for i in range(0, STRIP.numPixels(), 3):
                STRIP.setPixelColor(i+q, color)
            STRIP.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, STRIP.numPixels(), 3):
                STRIP.setPixelColor(i+q, 0)

def colorWipeBeam(color, wait_ms = 20):
    for q in range(STRIP_LEDS_PER_STRAND):
        for i in range(0, STRIP.numPixels(), STRIP_LEDS_PER_STRAND):
            STRIP.setPixelColor(i+q, color)
        STRIP.show()
        time.sleep(wait_ms/1000.0)

def staticColor(red,green,blue):
    for i in range(STRIP.numPixels()):
        STRIP.setPixelColor(i, Color(red,green,blue))
    STRIP.show()


def runColorCycle():
    while MASTER_LOOP:
        type = random.randint(0,1)
        if type == 0:
            colorWipeBeam(Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        if type == 1:
            theaterChase(Color(random.randint(0,255), random.randint(0,255),random.randint(0,255)))
        #colorWipeBeam(Color(255,0,0))
        #colorWipeBeam(Color(0,255,0))
        #colorWipeBeam(Color(0,0,255))
        #colorWipeBeam(Color(114,228,52))
        #colorWipeBeam(Color(52,52,52))
        #colorWipeBeam(Color(255,0,128))
        

def startUp(): 
    colorWipeBeam(Color(255,0,0))
    colorWipeBeam(Color(0,255,0))
    colorWipeBeam(Color(0,0,255))
    colorWipeBeam(Color(0,0,0))
    pulseColor(Color(0,255,0))
    pulseColor(Color(0,255,0))
    pulseColor(Color(0,255,0))
    pulseColor(Color(0,255,0))


def turnOff():
    colorWipeBeam(Color(0,0,0))


def runTheater():
    while MASTER_LOOP:
        theaterChase(Color(255,255,255))


def pong():
    for i in range(34):
        STRIP.setPixelColor(i+36, Color(255,255,255))
        STRIP.setPixelColor(648 + 36 + i, Color(255,255,255))
        STRIP.show()
    for t in range(3):
        STRIP.setPixelColor(162 , Color(255,255,255))
        STRIP.show()
        time.sleep(1)
        STRIP.setPixelColor(162, Color(0,0,0))
        STRIP.show()
        time.sleep(1)
    STRIP.setPixelColor(162, Color (255,255,255))
    STRIP.show()
    while MASTER_LOOP:
        oldLocation = 162
        for q in range(4):
            STRIP.setPixelColor(oldLocation, Color(0,0,0))
            STRIP.setPixelColor(oldLocation + 108, Color(255,255,255))
            oldLocation = oldLocation + 108
            STRIP.show()
            time.sleep(.7)
        for w in range(4):
            STRIP.setPixelColor(oldLocation, Color(0,0,0))
            STRIP.setPixelColor(oldLocation - 108, Color(255,255,255))
            oldLocation = oldLocation - 108
            STRIP.show()
            time.sleep(0.7)
