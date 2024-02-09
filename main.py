
import time
from servo import Servo
from picozero import Pot

# Create our Servo object, assigning the
# GPIO pin connected the PWM wire of the servo
my_servo = Servo(pin_id=16)
potentiometer = Pot(0)


def mapPotToAngle():
    return potentiometer.value * 180

while True:
    print("potentionmeter", potentiometer.value)
    my_servo.write(mapPotToAngle())
