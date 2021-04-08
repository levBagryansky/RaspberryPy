import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [24, 25, 8, 7, 12, 16, 20, 21]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup (dac[0], GPIO.OUT)
GPIO.setup (dac[1], GPIO.OUT)
GPIO.setup (dac[2], GPIO.OUT)
GPIO.setup (dac[3], GPIO.OUT)
GPIO.setup (dac[4], GPIO.OUT)
GPIO.setup (dac[5], GPIO.OUT)
GPIO.setup (dac[6], GPIO.OUT)
GPIO.setup (dac[7], GPIO.OUT)

def lightUp(ledNumber, period):
    n = leds[ledNumber]
    GPIO.setup(n, GPIO.OUT)
    GPIO.output(n, 1)
    time.sleep(period)
    GPIO.output(n, 0)
    #GPIO.output(leds, 0)

#lightUp(6,0)

#GPIO.cleanup()

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (0, blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
        
#blink(5, 5, 1)


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

#runningDark(1, 1)

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
#arr = decToBinList(254)


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
#shift(arr, 1)
#print(arr)

#arr = decToBinList(214)





def lightNumber(arr):
    
    for i in range(0, 8):
        if(arr[i] == '1'):
            GPIO.setup(leds[7-i], GPIO.OUT)
            GPIO.output(leds[7-i], 1)

    #GPIO.output(n, 0)
    time.sleep(1)
    #GPIO.output(n, 0)
    for i in range(0, 8):
        if(True):
            GPIO.setup(leds[i], GPIO.OUT)
            GPIO.output(leds[i], 1)

    GPIO.output(leds[1], 0)
    GPIO.output(leds[2], 0)
    GPIO.output(leds[3], 0)
    GPIO.output(leds[4], 0)
    GPIO.output(leds[5], 0)
    GPIO.output(leds[6], 0)
    GPIO.output(leds[7], 0)
    GPIO.output(leds[0], 0)
    

#arr = decToBinList(255)
#lightNumber(arr)

def runningPattern(pattern, direcrion):
    i = 0
    k = 1
    if(direcrion == "left"):
        k = -1
    arr = decToBinList(pattern)
    while(True):
        shift(arr, k)
        lightNumber(arr)

#runningPattern(3, "left")

leds = dac

def num2dac(value):
    #value = 255
    arr1 = decToBinList(value)
    print(arr1)
    n = 0
    for byte in arr1:
        GPIO.output (dac[n], int(byte))
        n+=1
    time.sleep(1)

#num2dac(255)



#arr = decToBinList(3)
def script1():
    while(True):
        print("Введите число:")
        x = int(input())
        if(x == -1):
            print("Выхожу..")
            break
        else:
            num2dac(x)
script1()

def script2(n):
    for

GPIO.cleanup()