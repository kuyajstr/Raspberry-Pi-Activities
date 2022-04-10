#number guessing game
import I2C_LCD_driver 
import time             #load time library
import RPi.GPIO as GPIO #load GPIO Library

cols = [5, 0, 11, 9]
rows = [6, 13, 19, 26]

numToGuess = "9"
inputNum = ""
counter = 0

GPIO.setwarnings(False) # supress warnings
GPIO.setmode(GPIO.BCM)  # USE GPIO pin numbering

#initialize components
for c in cols:
    GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
for r in rows:
    GPIO.setup(r, GPIO.OUT)

lcd = I2C_LCD_driver.lcd()

#Read the input button
def readLine(line, characters):
    global inputNum
    
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(cols[0]) == 1):
        inputNum = characters[0]
    if(GPIO.input(cols[1]) == 1):
        inputNum = characters[1]
    if(GPIO.input(cols[2]) == 1):
        inputNum = characters[2]
    if(GPIO.input(cols[3]) == 1):
        inputNum = characters[3]
    GPIO.output(line, GPIO.LOW)
    
def numComparator():
    global inputNum
    
    if int(inputNum) < int(numToGuess):
        return "HIGHER"
    elif int(inputNum) == int(numToGuess):
        return "CONGRATULATION!!"
    else:
        return "LOWER"

    
def checkInput():
    global inputNum
    global counter
    
    if not inputNum == "" :
        
        lcd.lcd_clear()
        
        if inputNum == numToGuess: #Prompt Correct answer
            lcd.lcd_display_string(numComparator(),1,0)
            lcd.lcd_display_string(inputNum + " CORRECT!!",2,0)
            counter = 0
        else: #Prompt incorrect number
            lcd.lcd_display_string(numComparator(),1,0)
            lcd.lcd_display_string(inputNum + " Try Again",2,0)
            
            counter += 1
            
        if counter > 5 :
            lcd.lcd_display_string("GAME OVER!!!",2,0)
            counter = 0
            
        inputNum = ""
            
        time.sleep(0.5)
        lcd.lcd_clear()
    
try: 
    while True:
        lcd.lcd_display_string("Guess a number",1,0)
        
        readLine(rows[0], ["1","2","3","4"])
        readLine(rows[1], ["5","6","7","8"])
        readLine(rows[2], ["9","10","11","12"])
        readLine(rows[3], ["13","14","15","16"])
        time.sleep(0.1)
        
        checkInput()
        
except KeyboardInterrupt:
    print("\nApplication stopped!")