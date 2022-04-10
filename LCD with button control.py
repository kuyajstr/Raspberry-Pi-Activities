import I2C_LCD_driver  #Load I2C_LCD Library
import time             #load time library
import RPi.GPIO as GPIO #load GPIO Library

btns = [26, 19, 13, 6]

GPIO.setwarnings(False) # supress warnings
GPIO.setmode(GPIO.BCM) # USE GPIO pin numbering

#initialize components
for btn in btns:
    GPIO.setup(btn, GPIO.IN)

lcd = I2C_LCD_driver.lcd()

def display1():
    lcd.lcd_display_string("Study",1,0) 
    time.sleep(2)
    lcd.lcd_clear()

def display2():
    lcd.lcd_display_string("Sleep",1,7) 
    time.sleep(2)
    lcd.lcd_clear()

def display3():
    lcd.lcd_display_string("Eat",2,0) 
    time.sleep(2)
    lcd.lcd_clear()
def display4():
    lcd.lcd_display_string("Code",2,7) 
    time.sleep(2)
    lcd.lcd_clear()

while True:
    if  GPIO.input(btns[0]) == False:
        display1()
    elif GPIO.input(btns[1]) == False:
        display2()
    elif GPIO.input(btns[2]) == False:
        display3()
    elif GPIO.input(btns[3]) == False:
        display4()
    
GPIO.cleanup() 