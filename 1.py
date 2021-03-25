import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [24, 25, 8, 7, 12, 16, 20, 21]

def lightUp(ledNumber, period):
    n = leds[ledNumber]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 1)
    time.sleep(period)
    GPIO.output(n, 0)
    #GPIO.output(leds, 0)

lightUp(6,0)



def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (0, blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
        
#blink(5, 1, 1)


def runningLight(count, period):
    for i in range(0, count):
        for j in range(0, 8):
            lightUp(j, period)

#runningLight(1, 1)

def lightDark(ledNumber, period): #turn on all lump without one
    n = leds[ledNumber]


    #GPIO.output(n, 1)
    #time.sleep(period)
    #GPIO.output(n, 0)
    for i in range(0, 8):
        GPIO.setup(leds[i], GPIO.OUT)
        GPIO.output(leds[i], 1)
        #GPIO.output(leds[i], 0)   


    #GPIO.setup(leds[ledNumber], GPIO.IN)
    GPIO.output(n, 0)
    time.sleep(period)
    GPIO.output(n, 0)   
    GPIO.output(leds, 0)
    

def runningDark(count, period):
    for i in range(0, count):
        for j in range(0, 8):
            lightDark(j, period)

#runningDark(2, 1)

def lightNumber(n):
    n = bin(n)
    n = n*2
    print(n)
    #for i in range(0, 5):

#lightNumber(3)
#GPIO.output(leds, 0)
GPIO.cleanup()