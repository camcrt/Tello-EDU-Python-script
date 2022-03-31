# This is a sample Python script.

import keyboard

from cv2 import CamShift
from conf import *
from djitellopy import TelloSwarm



def keyBoardControl(swarm):
    while keyboard.read_key() != "p":
        
        if keyboard.read_key() == "z":
            swarm.move_forward(50)
        
        if keyboard.read_key() == "s":
            swarm.move_back(50)

        if keyboard.read_key() == "q":
            swarm.move_left(50)

        if keyboard.read_key() == "d":
            swarm.move_right(50)
        
        if keyboard.read_key() == "e":
            swarm.takeoff()

        if keyboard.read_key() == "f":
           swarm.sequentiallyl(lambda i, tello: tello.flip_back())

        if keyboard.read_key() == "c":
            swarm.sequential(lambda i, tello: tello.move_up(i * 10 + 20))


        
                
    
    
    print("\n you left the keyboard control mode")
    swarm.land()

    
    
        

def reboot():
    """not working
    """
    conf = Configuration('redme007', 'redme007', 'motdepasse', 24)
    ip = conf.getTelloIp()
    swarm = TelloSwarm.fromIps(ip)
    swarm.connect()
    for tello in swarm:
        tello.reboot()
    swarm.end()


def swarm_example():
    # create, initialize a configuration and save it in a variable for later
    # change the parameter with your router's parameter
    conf = Configuration('Camille', 'Camille', 'wificamille', 24)
    # run tello configuration script
    #ip = conf.run()
    ip = ['192.168.43.147', '192.168.43.213', '192.168.43.251', '192.168.43.6']

    # create swarm  drone with available tello ip that we recover from conf variable
    swarm = TelloSwarm.fromIps(ip)
    swarm.connect()
    
    

    print("\n you enter in the keyboard control mode")
    keyBoardControl(swarm) 
    
    swarm.end()


if __name__ == '__main__':
    swarm_example()

