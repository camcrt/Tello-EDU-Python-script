# The purpose of this program is to control a drone via a controller 

from conf import *
from djitellopy import TelloSwarm
import pygame

def controleManette(tello):
    LEFT, RIGHT, UP, DOWN, FORE, BACK, YAW_G, YAW_D = False, False, False, False, False, False, False, False
    pygame.init()

    #initialize window
    window = pygame.display.set_mode((400, 400))
    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()

    running = True

    #Initialize controller
    joysticks = []
    for i in range(pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
    for joystick in joysticks:
        joystick.init()

    # 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
    # 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
    analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }
   

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # HANDLES BUTTON PRESSES
            
    
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(0): # x
                    print("x pressed")
                    tello.flip_back()

                if pygame.joystick.Joystick(0).get_button(1): # circle
                    print("circle pressed")
                    tello.flip_right()
                

                if pygame.joystick.Joystick(0).get_button(2): # triangle
                    print("triangle pressed")
                    tello.flip_foreward()
                
                
                if pygame.joystick.Joystick(0).get_button(3): # square
                    print("triangle pressed")
                    tello.flip_left()
                
                if pygame.joystick.Joystick(0).get_button(4): # L1
                    print("L1 pressed")
                    tello.land()
                
                if pygame.joystick.Joystick(0).get_button(5): # R1
                    print("R1 pressed")
                    tello.takeoff()

                if pygame.joystick.Joystick(0).get_button(6): # L2
                    print("L2 pressed")
                    

                if pygame.joystick.Joystick(0).get_button(7): # R2 
                    print("R2 pressed")
                    #UP = True
                
                if pygame.joystick.Joystick(0).get_button(8): # share
                    print("right stick pressed")

                if pygame.joystick.Joystick(0).get_button(9): # option
                    print("L1 pressed")
                
                if pygame.joystick.Joystick(0).get_button(10): # PS
                    print("PS pressed")
                    tello.takeoff()

                if pygame.joystick.Joystick(0).get_button(11): # L3
                    print("up arrow pressed")
                
                if pygame.joystick.Joystick(0).get_button(12): # R3
                    print("down arrow pressed")
                
                elif event.type == pygame.JOYBUTTONUP:
                    print("released")

            if event.type == pygame.JOYAXISMOTION:
                analog_keys[event.axis] = event.value
                # print(analog_keys)
                # Horizontal Analog
                if abs(analog_keys[0]) > .4:
                    if analog_keys[0] < -.7:
                        LEFT = True
                    else:
                        LEFT = False
                    if analog_keys[0] > .7:
                        RIGHT = True
                    else:
                        RIGHT = False
                # Vertical Analog
                if abs(analog_keys[1]) > 0.4:
                    if analog_keys[1] < -0.7:
                        FORE = True
                    else:
                        FORE = False
                    if analog_keys[1] > .7:
                        BACK = True
                    else:
                        BACK = False
                
                
                if analog_keys[2] > 0.7:  # Left trigger
                    DOWN = True
                else: 
                    DOWN = False

                
                if analog_keys[5] > 0.7:  # Right Trigger
                    UP = True
                else : 
                    UP = False
                
                if abs(analog_keys[3]) > 0.4:# right vertical analog 
                    if analog_keys[3] < -0.7:
                        YAW_G = True 
                    else:
                        YAW_G = False
                    
                    if analog_keys[3] > .7:
                        YAW_D = True
                    else:
                        YAW_D = False
                

        if YAW_D == False and YAW_G == False:
            yaw = 0

        if UP == False and DOWN == False:
            high_low = 0

        if FORE == False and DOWN == False:
            fore_back = 0
        
        if RIGHT == False and LEFT == False:
            left_right = 0 

        if YAW_D:
            yaw = 90
        if YAW_G:
            yaw = -90

        if UP : 
            high_low = 100
            print("up")
        
        if DOWN :
            high_low = -100
            print("down")
            
        if FORE : 
            fore_back = 90

        if BACK : 
            fore_back = -90
        if LEFT : 
            left_right = -90
        if RIGHT : 
            left_right = 90   

        tello.send_rc_control(left_right,fore_back,high_low,yaw)
                

            
               

    pygame.quit()
 
def swarm_example():

    # create, initialize a configuration and save it in a variable for later
    # change the parameter with your router's parameter
    conf = Configuration('router name', 'SSID', 'password', 24)

    # run tello configuration script
    #ip = conf.run()
    
    ip = conf.getTelloIp()

    # create swarm  drone with available tello ip that we recover from conf variable
    swarm = TelloSwarm.fromIps(ip)
    swarm.connect()
    
    controleManette(swarm.tellos[0])
    

if __name__ == '__main__':
    swarm_example()