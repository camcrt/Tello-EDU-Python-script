# The purpose of this program is to control more than one drone from the same keyboard

import threading

from conf import *
from djitellopy import TelloSwarm
import pygame

    
def controleClavier1(tello):
    LEFT, RIGHT, UP, DOWN, FORE, BACK, YAW_G, YAW_D = False, False, False, False, False, False, False, False
    
    pygame.init()

    #initialize window
    window = pygame.display.set_mode((400, 400))
    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()

    running = True
    
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    
        userInput = pygame.key.get_pressed()

        if userInput[pygame.K_z]:
            FORE = True
        else : FORE = False
        
        if userInput[pygame.K_s]:
            BACK = True
        else : BACK = False

        if userInput[pygame.K_d]:
            RIGHT = True
        else : RIGHT = False
        
        if userInput[pygame.K_q]:
            LEFT = True
        else : LEFT = False
        
        if userInput[pygame.K_SPACE]:
            UP = True
        else : UP = False

        if userInput[pygame.K_LSHIFT]:
            DOWN = True
        else : DOWN = False

        if userInput[pygame.K_e]:
            YAW_D = True
        else : YAW_D = False

        if userInput[pygame.K_a]:
            YAW_G = True
        else : YAW_G = False
       


        if YAW_D == False and YAW_G == False:
            yaw = 0

        if UP == False and DOWN == False:
            high_low = 0

        if FORE == False and DOWN == False:
            fore_back = 0
        
        if RIGHT == False and LEFT == False:
            left_right = 0 

        if YAW_D:
            yaw = 50

        if YAW_G:
            yaw = -50

        if UP : 
            high_low = 50
            print("up")
        
        if DOWN :
            high_low = -50
            print("down")
            
        if FORE : 
            fore_back = 50

        if BACK : 
            fore_back = -50
            
        if LEFT : 
            left_right = -50
        if RIGHT : 
            left_right = 50   

        if userInput[pygame.K_TAB]:
            tello.takeoff()
        
        if userInput[pygame.K_RETURN]:
            tello.land()
    

        tello.send_rc_control(left_right,fore_back,high_low,yaw)


    pygame.quit()

def controleClavier2(tello):
    LEFT, RIGHT, UP, DOWN, FORE, BACK, YAW_G, YAW_D = False, False, False, False, False, False, False, False
    pygame.init()

    #initialize window
    window = pygame.display.set_mode((400, 400))
    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()

    running = True

    
    while running: #à taffer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # HANDLES BUTTON PRESSES
            
        userInput = pygame.key.get_pressed()

        if userInput[pygame.K_i]:
            FORE = True
        else : FORE = False
        
        if userInput[pygame.K_k]:
            BACK = True
        else : BACK = False

        if userInput[pygame.K_j]:
            RIGHT = True
        else : RIGHT = False
        
        if userInput[pygame.K_l]:
            LEFT = True
        else : LEFT = False
        
        if userInput[pygame.K_b]:
            UP = True
        else : UP = False

        if userInput[pygame.K_n]:
            DOWN = True
        else : DOWN = False

        if userInput[pygame.K_o]:
            YAW_D = True
        else : YAW_D = False

        if userInput[pygame.K_u]:
            YAW_G = True
        else : YAW_G = False
       
                

        if YAW_D == False and YAW_G == False:
            yaw = 0

        if UP == False and DOWN == False:
            high_low = 0

        if FORE == False and DOWN == False:
            fore_back = 0
        
        if RIGHT == False and LEFT == False:
            left_right = 0 

        if YAW_D:
            yaw = 50
        if YAW_G:
            yaw = -50

        if UP : 
            high_low = 50
            print("up")
        
        if DOWN :
            high_low = -50
            print("down")
            
        if FORE : 
            fore_back = 50
            

        if BACK : 
            fore_back = -50
            
        if LEFT : 
            left_right = -50
        if RIGHT : 
            left_right = 50   

        if userInput[pygame.K_p]:
            tello.takeoff()
        
        if userInput[pygame.K_m]:
            tello.land()
    
        tello.send_rc_control(left_right,fore_back,high_low,yaw)
            

    pygame.quit()
    
def launch_swarm():

    conf = Configuration('router name', 'SSID', 'password', 24)

    #ip = conf.run()    
    ip = conf.getTelloIp()

    swarm = TelloSwarm.fromIps(ip)
    swarm.connect()
    
    t1 = threading.Thread(target=controleClavier2, args=[swarm.tellos[0]])
    t2 = threading.Thread(target=controleClavier1, args=[swarm.tellos[1]])    

    t1.start()
    t2.start()

    t1.daemon = True
    t2.daemon = True

    t1.join()
    t2.join()

if __name__ == '__main__':
    launch_swarm()

