import RPi.GPIO as GPIO
import time

LED_ROUGE = 17
LED_VERTE = 27
LED_JAUNE = 22

# Liste pour faciliter le chenillard
LEDS = [LED_ROUGE, LED_VERTE, LED_JAUNE]

# Configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDS, GPIO.OUT)

try:
    while True:
        for led in LEDS:
            # Éteindre toutes les LEDs
            GPIO.output(LEDS, GPIO.LOW)

            # Allumer une seule LED
            GPIO.output(led, GPIO.HIGH)

            time.sleep(0.3)  # vitesse du chenillard

except KeyboardInterrupt:
    GPIO.cleanup()
