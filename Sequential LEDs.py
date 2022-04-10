import time #load time library
import RPi.GPIO as GPIO #load GPIO Library

btns = [17, 27, 22]
leds = [5, 6, 13, 19, 26]

GPIO.setwarnings(False) # supress warnings
GPIO.setmode(GPIO.BCM) # USE GPIO pin numbering

for btn in btns:
    GPIO.setup(btn, GPIO.IN)

for led in leds:
    GPIO.setup(led, GPIO.OUT)

while True:
    if  GPIO.input(btns[0]) == False:
        for led in leds:
            GPIO.output(led, GPIO.HIGH)
            time.sleep(.250)
            GPIO.output(led, GPIO.LOW)
    
    elif  GPIO.input(btns[1]) == False:
        leds.reverse()
        
        for led in leds:
            GPIO.output(led, GPIO.HIGH)
            time.sleep(.250)
        for led in leds:
            GPIO.output(led, GPIO.LOW)
            time.sleep(.250)
        
        leds.reverse()
            
    elif GPIO.input(btns[2]) == False:
        last = 4
        first = 0
        
        while last >= 0:
            GPIO.output(leds[first], GPIO.HIGH)
            GPIO.output(leds[last], GPIO.HIGH)
            time.sleep(.250)
            GPIO.output(leds[first], GPIO.LOW)
            GPIO.output(leds[last], GPIO.LOW)
            last -= 1
            first += 1
            
    else: 
        for led in leds:
            GPIO.output(led, GPIO.LOW)
    
GPIO.cleanup() #reset pin status to their default state