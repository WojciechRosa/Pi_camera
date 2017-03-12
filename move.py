#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
pwm=GPIO.PWM(12,50)
pwm.start(7)
#to jest komentarz
for i in range (30,110):
        DC=1./18.*(i)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(.05)
pwm.stop()
GPIO.cleanup()
