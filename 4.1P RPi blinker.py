import RPi.GPIO as GPIO
import time
#setup GPIO
GPIO.setmode(GPIO.BOARD)
#setup pin 10 as output
GPIO.setup(10, GPIO.OUT)
try:
	while 1:
		#pin 10 set to high LED flash on
		GPIO.output(10, GPIO.HIGH)
		time.sleep(0.25)
		#LED off
		GPIO.output(10, GPIO.LOW)
		time.sleep(0.25)
except KeyboardInterrupt:
	GPIO.cleanup()
	
