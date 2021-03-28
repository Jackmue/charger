from motor_control import *
from drone_control import *

if __name__ == '__main__':
    print('Hi this is start')
    init_motors()
    init_sleighs()
    two_pads(100)
    print("drone landed")

    init_motors()
    init_sleighs()
    #exit(0)

    sleighs_forward()
    print("sleighs kissed the Drone")
    charge()
    switch()
    sleighs_backward()
    #Drone getting charged
    print("drone ready to fly")


    print("hello_Charger_its_me")
    exit(0)