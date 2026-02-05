import RPi.GPIO as GPIO
import time

LED_ROUGE = 17
LED_VERTE = 27
LED_JAUNE = 22

# Configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup([LED_ROUGE, LED_VERTE, LED_JAUNE], GPIO.OUT)

# Allumer la LED rouge
GPIO.output(LED_ROUGE, GPIO.HIGH)
time.sleep(1)
GPIO.output(LED_ROUGE, GPIO.LOW)

# Allumer la LED verte
GPIO.output(LED_VERTE, GPIO.HIGH)
time.sleep(1)
GPIO.output(LED_VERTE, GPIO.LOW)

# Allumer la LED jaune
GPIO.output(LED_JAUNE, GPIO.HIGH)
time.sleep(1)
GPIO.output(LED_JAUNE, GPIO.LOW)

GPIO.cleanup()

GPIO.cleanup()