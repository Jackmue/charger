# With this file you are able to controle the drone "Tello by Edu"

from time import sleep
from easytello import Tello
import time

print("Welcome here write the code now to control the Drone")

#from tello import Tello

def convert_to_go_code(x, y, z, speed, pad):
    command_str = "go " + str(x) + " " + str(y) + " " + str(z) + " " + str(speed) + " m" + str(pad)
    return command_str

def angle_maker(angle):
    command_str = "ccw " + str(angle)
    return command_str

def two_pads(distance_of_pads):
    x1 = 0
    y1 = 0
    z1 = 150
    speed1 = 20
    x2 = distance_of_pads
    y2 = 0
    z2 = 150
    speed2 = 50
    angle = 180

    tello = Tello()

    tello.send_command("command")
    tello.send_command("takeoff")
    tello.send_command("mon")
    tello.send_command(convert_to_go_code(x1, y1, z1, speed1, 1))
    tello.send_command(convert_to_go_code(x2, y2, z2, speed2, 1))
    tello.send_command(angle_maker(angle))
    tello.send_command(convert_to_go_code(x1, y1, z1, speed1, 2))
    tello.send_command(convert_to_go_code(x2, y2, z2, speed2, 2))
    tello.send_command(angle_maker(angle))
    tello.send_command(convert_to_go_code(x1, y1, z1, speed1, 1))
    tello.send_command(convert_to_go_code(0, 0, 40, speed2, 1))
    time.sleep(3)
    tello.send_command(convert_to_go_code(0, 5, 35, 10, 1))
    time.sleep(2)
    tello.send_command("land")
    return None

def four_pads(distance_of_pads):
    x1 = 0
    y1 = 0
    z1 = 150
    speed1 = 20
    x2 = distance_of_pads
    y2 = 0
    z2 = 150
    speed2 = 100
    angle = 90

    tello = Tello()

    tello.send_command("command")
    tello.streamon()
    tello.send_command("takeoff")
    tello.send_command("mon")
    tello.send_command(convert_to_go_code(x1, y1, z1, speed1, 1))
    tello.send_command(convert_to_go_code(x2, y2, z2, speed2, 1))
    tello.send_command(angle_maker(angle))
    tello.send_command(convert_to_go_code(x1, y1, z1, speed1, 2))
    tello.send_command(convert_to_go_code(x2, y2, z2, speed2, 2))
    tello.send_command(angle_maker(angle))
    tello.send_command(convert_to_go_code(x1, y1, z1, speed1, 3))
    tello.send_command(convert_to_go_code(x2, y2, z2, speed2, 3))
    tello.send_command(angle_maker(angle))
    tello.send_command(convert_to_go_code(x1, y1, z1, speed1, 4))
    tello.send_command(convert_to_go_code(x2, y2, z2, speed2, 4))
    tello.send_command(angle_maker(angle))
    tello.send_command(convert_to_go_code(x1, y1, z1, speed1, 1))
    tello.send_command(convert_to_go_code(0, 0, 40, speed2, 1))
    tello.send_command("land")
    return None

"""exit(0)

for i in range(4):
    tello.send_command("forward 30")
    tello.send_command("cw 90")
tello.send_command("land")
exit(0)
from easytello import tello
drone = tello.Tello()

drone.takeoff()
for i in range(4):
    drone.forward(20)
    drone.ccw(90)
drone.land()"""