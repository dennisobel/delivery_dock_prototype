import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ROW_PINS = [6, 13, 19, 26]
COL_PINS = [16, 20, 21]
DOCS_LOCK=4
HOT_LOCK=17
COLD_LOCK=27
REFILLABLES_LOCK=22