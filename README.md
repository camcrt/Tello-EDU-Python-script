# Drone-Swarming
The goal of this project is to allow the manual control of one or more Tello EDU drone. 

*  The `conf.py` file and the `setup.sh`come from [this repository](https://github.com/hammoudipro/Drone-Swarming) 

# Installation
The instructions below work on Linux and similar operating systems.

#### Clone this repository
```bash
git clone https://github.com/hammoudipro/Drone-Swarming.git
```

#### Change directory
```bash
cd Drone-Swarming
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
There is three usable script in the the example folder : 

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


### two_drone_one_keyboard.py
Thanks to this script you can control two Tello EDU through a router with your keyboard. To connect them to re router, follow the same instruction  as for the `controller_router_mode.py` script.

