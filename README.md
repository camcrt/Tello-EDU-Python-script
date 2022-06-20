# Drone-Swarming
The goal of this project is to allow the manual control of one or more Tello EDU drone. 

*  The `conf.py` file and a part of the`setup.sh` file come from [this repository](https://github.com/hammoudipro/Drone-Swarming) 

# Installation
The instructions below work on Linux and similar operating systems.

#### Clone this repository
```bash
git clone https://github.com/camcrt/Tello-EDU-Python-script.git
```

#### Install python3 and all needed modules
The file `setup.sh` is responsible for the python setup.
- First we need to give execute permissions to `setup.sh`
```bash
chmod +x setup.sh
```
- Then execute script bash
```bash
./setup.sh
```

## Scripts 
There is four usable script in the the scripts folder : 

### controller_AP_mode.py 
Thanks to this script you can control one Tello EDU on acces point mode.
It is the simplest way to connect the drone. You just have to search the name of the access point in the list of available networks in your wifi setting and connect to it  

Personnaly I use a Sony DualShock for the controller.

### controller_router_mode.py 
Thanks to this script you can control one Tello EDU through a router.

For this you need to connect the drone to it. This is what the `.conf` file is for.  
* if the drone is not connected to the router, uncomment the line below 
```python3
    #ip = conf.run()
```
once the drone is connected you have to comment it again

* We need the **name**, **ssid**, **password** and **netmask** (by default netmask is set to 24) of the router 

### keyboard_controlled_swarm.py
The aim of this script is to control an indefinite number of drone with the keyboard. To connect them to re router, follow the same instruction  as for the `controller_router_mode.py` script.

#### Here the commands : 
| key |      command      |
|:---:|:-----------------:|
|  e  |      takeoff      |
|  p  |        land       |
|  z  |    move forward   |
|  q  |  move to the left |
|  s  |     move back     |
|  d  | move to the right |
|  c  |      move up      |
|  x  |     move down     |
|  f  |     do a flip     |

### two_drone_one_keyboard.py
Thanks to this script you can control two Tello EDU through a router with your keyboard. To connect them to re router, follow the same instruction  as for the `controller_router_mode.py` script.

#### Here the commands : 
|   Drone 1  |                   | Drone 2 |                   |
|:----------:|:-----------------:|:-------:|:-----------------:|
|     key    |      command      |   key   |      command      |
|     TAB    |      takeoff      |    e    |      takeoff      |
|   RETURN   |        land       |    p    |        land       |
|      z     |    move forward   |    i    |    move forward   |
|      q     |  move to the left |    qj   |  move to the left |
|      s     |     move back     |    k    |     move back     |
|      d     | move to the right |    l    | move to the right |
|    space   |      move up      |    b    |      move up      |
| left shift |     move down     |    n    |     move down     |
|      e     |  yaw on the right |    o    |  yaw on the right |
|      a     |  yaw on the left  |    u    |  yaw on the left  |