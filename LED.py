import RPi.GPIO as GPIO
import time

greenLed = 11 #pin 11

yellowLed = 13 #pin 13

redLed = 15 #pin 15

greenLed2 = 18 #pin 18

yellowLed2 = 16 #pin 16

redLed2 = 12 #pin 12

button = 38 #pin 38

crossLED = 40 #pin 38

def setup():
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(greenLed, GPIO.OUT)
    GPIO.output(greenLed, GPIO.HIGH)
    
    GPIO.setup(yellowLed, GPIO.OUT)
    GPIO.output(yellowLed, GPIO.HIGH)
    
    GPIO.setup(redLed, GPIO.OUT)
    GPIO.output(redLed, GPIO.HIGH)
    
    ## Oppsosite intersection
    GPIO.setup(greenLed2, GPIO.OUT)
    GPIO.output(greenLed2, GPIO.HIGH)
    
    GPIO.setup(yellowLed2, GPIO.OUT)
    GPIO.output(yellowLed2, GPIO.HIGH)
    
    GPIO.setup(redLed2, GPIO.OUT)
    GPIO.output(redLed2, GPIO.HIGH)
    
    # Button setup
    GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(button, GPIO.FALLING, callback=pressed)
    
    #LED Crossing
    GPIO.setup(crossLED, GPIO.OUT)
    GPIO.output(crossLED, GPIO.HIGH)
    
ispressed = 0
def loop():
    while True:
        print ('Red2 LED On')
        GPIO.output(redLed2, GPIO.HIGH)
        time.sleep(1)
        print ('Green LED On')
        GPIO.output(greenLed, GPIO.HIGH)
        time.sleep(5)
        print('Green LED Off')
        GPIO.output(greenLed, GPIO.LOW)
        
        print ('Yellow LED On')
        GPIO.output(yellowLed, GPIO.HIGH)
        time.sleep(3)
        print('Yellow LED Off')
        GPIO.output(yellowLed, GPIO.LOW)
        
        print ('Red LED On')
        GPIO.output(redLed, GPIO.HIGH)
        time.sleep(1)
        ## Change to opposite intersection
        print('Red LED Off')
        GPIO.output(redLed2, GPIO.LOW)
        
        print ('Green2 LED On')
        GPIO.output(greenLed2, GPIO.HIGH)
        time.sleep(5)
        print('Green2 LED Off')
        GPIO.output(greenLed2, GPIO.LOW)
        
        print ('Yellow2 LED On')
        GPIO.output(yellowLed2, GPIO.HIGH)
        time.sleep(3)
        print('Yellow2 LED Off')
        GPIO.output(yellowLed2, GPIO.LOW)
        
        print('Red LED Off')
        GPIO.output(redLed, GPIO.LOW)
        global ispressed

        if ispressed > 0:
            print ('Red2 LED On')
            GPIO.output(redLed2, GPIO.HIGH)
            print ('Red1 LED On')
            GPIO.output(redLed, GPIO.HIGH)
            print ('Yellow2 LED On')
            GPIO.output(crossLED, GPIO.HIGH)
            time.sleep(2)
            print('Yellow2 LED Off')
            GPIO.output(crossLED, GPIO.LOW)
            print ('Yellow2 LED On')
            GPIO.output(crossLED, GPIO.HIGH)
            time.sleep(3)
            print('Yellow2 LED Off')
            GPIO.output(crossLED, GPIO.LOW)
            GPIO.output(redLed, GPIO.LOW)
            GPIO.output(redLed2, GPIO.LOW)
            ispressed = 0
            
def pressed(channel):
    global ispressed
    print('PRESSED')
    ispressed = 1
    
    
def destroy():
    GPIO.output(greenLed, GPIO.HIGH)
    GPIO.output(yellowLed, GPIO.HIGH)
    GPIO.output(redLed, GPIO.HIGH)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
