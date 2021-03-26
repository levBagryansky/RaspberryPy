#import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
leds = [24, 25, 8, 7, 12, 16, 20, 21]

def lightUp(ledNumber, period):
    n = leds[ledNumber]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 1)
    time.sleep(period)
    GPIO.output(n, 0)
    #GPIO.output(leds, 0)

#lightUp(6,0)



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

def decToBinList(n):
    n = bin(n)
    arr = list(n)
    leng = len(arr)
    res = [0, 0, 0, 0, 0, 0, 0, 0]
    leng = leng - 2
    for i in range(8 - leng, 8):
        res[i] = arr[i -6 + leng]
    print(res)
    return res
arr = decToBinList(254)


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
shift(arr, 1)
print(arr)

arr = decToBinList(254)
def lightNumber(arr):
    #arr = decToBinList(pattern);
    for i in range(0, 8):
        if(arr[i] == 1):
            GPIO.setup(leds[i], GPIO.OUT)
            GPIO.output(leds[i], 1)
    #GPIO.output(n, 0)
    time.sleep(2)
    GPIO.output(n, 0)
    GPIO.output(leds, 0)


def runningPattern(pattern, direcrion):
    i = 0
    k = 1
    if(direcrion == "left"):
        k = -1
    arr = decToBinList(pattern)
    while(True):
        shift(arr, k)
        lightNumber(arr)


#def runningPattern(pattern, direction):
    
#GPIO.output(leds, 0)
#GPIO.cleanup()