import time
import board
from adafruit_motorkit import MotorKit
import digitalio
import busio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(16, GPIO.IN)

print("hallo motor")

pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

print("done!")


kit = MotorKit()
print(kit.motor3)
# try:
#     while True:
#         print("I2C addresses found:", [hex(device_address)
#                                        for device_address in i2c.scan()])
#         time.sleep(2)
#
# finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
#     i2c.unlock()

def sleighs_forward():
    kit.motor1.throttle = 1
    while True:

        if GPIO.input(24):
            print("Hi")
            break
        else:
            print("low")

    kit.motor1.throttle = 0
    kit.motor3.throttle = 1
    while True:
        if GPIO.input(23):
            print("moin")
            break
        else:
            print("Tschüss")
    kit.motor3.throttle = 0

def sleighs_backward():
    kit.motor1.throttle = -1
    while True:
        if GPIO.input(25):
            print("back")
            break
        else:
            print("stop")
    kit.motor1.throttle = 0
    kit.motor3.throttle = -1
    while True:
        if GPIO.input(16):
            print("back2")
            break
        else:
            print("stop2")
    kit.motor3.throttle = 0

def switch_on():
    print("Im soon going to switch on")