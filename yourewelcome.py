## Credit:
## Midi to Raspberry Pi Converter
##     - Andy Tran (extramaster), 2015
## https://www.extramaster.net/tools/midiToArduino/
##
## Process:
## Midi -> Midi tracks -> Note mappings -> Frequency
##
## CC0

import RPi.GPIO as GPIO
import time

# Set this to be the pin that your buzzer resides in. (Note that you can only have one buzzer actively using the PWM signal at a time).

# GD = GND = Ground
 
# RPI v1 GPIO Layout BCM
# 5V 5V GD 14 15 18 GD 23 24 GD 25 08 07
# 3V 02 03 04 GD 17 27 22 3V 10 09 11 GD

# RPI v2 GPIO Layout BCM
# 5V 5V GD 14 15 18 GD 23 24 GD 25 08 07 SC GD 12 GD 16 20 21
# 3V 02 03 04 GD 17 27 22 3V 10 09 11 GD SD 05 06 13 19 26 GD 

# Note: Raspberry Pi 2 seems to handle software-PWM a lot better then the original Raspberry Pis.
tonePin = 13;

GPIO.setmode(GPIO.BCM)  
GPIO.setup(tonePin, GPIO.IN)
GPIO.setup(tonePin, GPIO.OUT)

# High-level abstraction of the Arduino's Delay function
def delay(times):
    time.sleep(times/1000.0)
    
# High-level abstraction of the Arduino's Tone function, though this version is blocking
def tone(pin, pitch, duration):
    if pitch == 0:
        delay(duration)
        return
    p = GPIO.PWM(tonePin, pitch)
    
    # Change the duty-cycle to 50 if you wish
    p.start(30)
    delay(duration)
    p.stop()
    
    # Delay used to discourage overlap of PWM cycles
    delay(2)
    
def midi():
    tone(tonePin, 391, 111.111)
    tone(tonePin, 220, 222.222)
    tone(tonePin, 261, 111.111)
    tone(tonePin, 220, 222.222)
    tone(tonePin, 329, 444.444)
    tone(tonePin, 293, 222.222)
    tone(tonePin, 261, 444.444)
    tone(tonePin, 391, 222.222)
    tone(tonePin, 659, 333.333)
    tone(tonePin, 523, 333.333)
    delay(370.37)
    tone(tonePin, 391, 111.111)
    tone(tonePin, 523, 222.222)
    tone(tonePin, 493, 333.333)
    tone(tonePin, 493, 111.111)
    tone(tonePin, 493, 222.222)
    tone(tonePin, 493, 333.333)
    delay(30.8641666667)
    tone(tonePin, 293, 83.33325)
    tone(tonePin, 391, 222.222)
    delay(30.8641666667)
    tone(tonePin, 220, 83.33325)
    tone(tonePin, 440, 166.6665)
    delay(432.098333333)
    tone(tonePin, 391, 111.111)
    tone(tonePin, 220, 222.222)
    tone(tonePin, 261, 111.111)
    tone(tonePin, 220, 222.222)
    delay(30.8641666667)
    tone(tonePin, 329, 416.66625)
    tone(tonePin, 587, 222.222)
    tone(tonePin, 293, 27.77775)
    tone(tonePin, 261, 208.333125)
    tone(tonePin, 523, 208.333125)
    tone(tonePin, 391, 222.222)
    tone(tonePin, 659, 333.333)
    tone(tonePin, 523, 333.333)
    delay(370.37)
    tone(tonePin, 195, 222.222)
    delay(123.456666667)
    tone(tonePin, 391, 111.111)
    tone(tonePin, 207, 111.111)
    tone(tonePin, 493, 111.111)
    tone(tonePin, 493, 111.111)
    tone(tonePin, 493, 222.222)
    tone(tonePin, 493, 111.111)
    tone(tonePin, 493, 222.222)
    tone(tonePin, 493, 111.111)
    tone(tonePin, 440, 111.111)
    tone(tonePin, 493, 111.111)
    tone(tonePin, 659, 444.444)
    delay(370.37)
    tone(tonePin, 220, 222.222)
    tone(tonePin, 261, 111.111)
    tone(tonePin, 220, 222.222)
    tone(tonePin, 783, 333.333)
    tone(tonePin, 329, 111.111)
    tone(tonePin, 659, 111.111)
    tone(tonePin, 293, 111.111)
    tone(tonePin, 261, 444.444)
    tone(tonePin, 391, 222.222)
    tone(tonePin, 659, 333.333)
    tone(tonePin, 523, 222.222)
    delay(987.653333333)
    tone(tonePin, 493, 666.666)
    tone(tonePin, 329, 111.111)
    tone(tonePin, 349, 111.111)
    tone(tonePin, 329, 111.111)
    tone(tonePin, 261, 111.111)
    tone(tonePin, 220, 111.111)
    tone(tonePin, 195, 111.111)
    tone(tonePin, 220, 111.111)
    tone(tonePin, 440, 444.444)
    delay(123.456666667)
    tone(tonePin, 220, 222.222)
    tone(tonePin, 261, 111.111)
    tone(tonePin, 220, 222.222)
    delay(30.8641666667)
    tone(tonePin, 783, 305.55525)
    tone(tonePin, 329, 111.111)
    tone(tonePin, 659, 111.111)
    tone(tonePin, 293, 138.88875)
    tone(tonePin, 261, 208.333125)
    delay(231.48125)
    tone(tonePin, 391, 222.222)
    tone(tonePin, 659, 333.333)
    tone(tonePin, 523, 222.222)
    delay(493.826666667)
    tone(tonePin, 195, 222.222)
    delay(123.456666667)
    delay(123.456666667)
    tone(tonePin, 207, 111.111)
    tone(tonePin, 493, 555.555)
    tone(tonePin, 523, 555.555)
    tone(tonePin, 440, 666.666)


while 1:
    midi()
    # GPIO.cleanup()