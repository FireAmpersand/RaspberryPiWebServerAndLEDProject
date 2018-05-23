import time
from neopixel import *
import argparse
import random

#LED Strip One Setup
STRIP_ONE_LEDS = 432 #Total LEDS
STRIP_ONE_LEDS_PER_STRAND = 108 #LEDS PER BEAM
STRIP_ONE_PIN = 18 #LED PIN OUT
STRIP_ONE_FREQ = 1000000
STRIP_ONE_DMA = 10
STRIP_ONE_BRIGHTNESS = 255
STRIP_ONE_INVERT = False
STRIP_ONE_CHANNEL = 0
STRIP = Adafruit_NeoPixel(STRIP_ONE_LEDS, STRIP_ONE_PIN, STRIP_ONE_FREQ, STRIP_ONE_DMA, STRIP_ONE_INVERT, STRIP_ONE_BRIGHTNESS, STRIP_ONE_CHANNEL)
STRIP.begin()

MASTER_LOOP = False

def newBrightness():
    STRIP.setBrightness( STRIP_ONE_BRIGHTNESS)

def colorwipe(color, wait_ms=1):
    for i in range(STRIP.numPixels()):
        STRIP.setPixelColor(i, color)
        STRIP.show()
        time.sleep(wait_ms/1000.0)

def revColorWipe(color, wait_ms=1):
    for i in range(STRIP.numPixels()):
        STRIP.setPixelColor(stripOne.numPixels()-1-i, color)
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
    for q in range(STRIP_ONE_LEDS_PER_STRAND):
        for i in range(0, STRIP.numPixels(), STRIP_ONE_LEDS_PER_STRAND):
            STRIP.setPixelColor(i+q, color)
        STRIP.show()
        time.sleep(wait_ms/1000.0)

def staticColor(red,green,blue):
    for i in range(STRIP.numPixels()):
        STRIP.setPixelColor(i, Color(red,green,blue))
    STRIP.show()


def runColorCycle():
    while MASTER_LOOP:
        colorWipeBeam(Color(255,0,0))
        colorWipeBeam(Color(0,255,0))
        colorWipeBeam(Color(0,0,255))
        colorWipeBeam(Color(114,228,52))
        colorWipeBeam(Color(0,0,0))
        colorWipeBeam(Color(255,0,128))

def startUp(): 
    colorWipeBeam(Color(255,0,0))
    colorWipeBeam(Color(0,255,0))
    colorWipeBeam(Color(0,0,255))
    colorWipeBeam(Color(0,0,0))
    #pulseColor(Color(255,0,0))
    #pulseColor(Color(255,0,0))
    #pulseColor(Color(255,0,0))
    #pulseColor(Color(255,0,0))


def turnOff():
    colorwipe(Color(0,0,0))


def runTheater():
    while MASTER_LOOP:
        print('Looping theater chase')
        theaterChase(Color(255,255,255))
