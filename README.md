# Pyramid-Pi

Pyramid Pi is a project developed in Python with the aim of automating and speeding up the construction of pyramids and towers within Minecraft Pi, being of great help when you want to build large structures.

## PREREQUISITES

- A Raspberry Pi (2GB is enough).
- A Raspberry Pi Power Supply.
![image](https://user-images.githubusercontent.com/85902337/130700135-7602561a-4ccd-4993-9dfa-3af0a76fca44.png)

- A microSD card (at least 8GB).
![image](https://user-images.githubusercontent.com/85902337/130700204-dae26a1b-9c4e-4fd4-92a1-4a5eb7640f3c.png)

- A keyboard.
- A mouse.
- A TV or computer monitor.
- Depending on the port of your TV / monitor, you will need one of the following cables:

  HDMI-HDMI cable
  
![image](https://user-images.githubusercontent.com/85902337/130700347-26edd0f8-ec2d-4dad-bd9a-97d624265c7b.png)

  HDMI-VGA cable
  
![image](https://user-images.githubusercontent.com/85902337/130700485-35c3f8fc-2e3c-4270-912b-ac8084a3c9b1.png)

  HDMI-DVI cable
  
![image](https://user-images.githubusercontent.com/85902337/130700535-f8656c96-e84e-43da-8110-f52f87232db5.png)

Prepare the Raspberry Pi to start following the instructions.
- Minecraft Pi installed.
- Python IDE (installed by default at your Raspberry Pi).

### To start the Raspberry Pi

Follow the instructions, which you can consult in more detail in the following link on the official Raspberry Pi page:

https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up


### To install and get started to Minecraft Pi

I highly recommend to follow the guide of Getting started with Minecraft Pi by the official Raspberry Pi website, it explains step by step how to install Minecraft Pi, how to use the game and manipulate it via python IDE:

https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi

## QUICKSTART

Clone this repository:
```
git clone https://github.com/davidd-eng/pyramid-pi
```
To use this program you must open the document pyramid-pi.py and manipulate it.

### To change the type of block to build go to the line 198 and undo the following comment:
```
#pyramid_pi_object = Pyramid_pi(block.STONE.id)
```
If you want to change the block to build, you can do it with the ID that corresponds to each type of block, the IDs of the blocks can be found in the “API Block List” of Minecraft Pi in the following link:

https://www.raspberrypi-spy.co.uk/2014/09/raspberry-pi-minecraft-block-id-number-reference/

You can select the blocks in the “API Block List” using the following syntax :

block.GRASS.id

### To make a pyramid go to the line 201 and undo the following comment:
```
#pyramid_pi_object.build_pyramid(5)
```
With this, if the code is run, a pyramid will be built automatically, the number that appears in parentheses can be changed according to the height of the pyramid that is desired. In this case, with the number 5, the pyramid will be 5 blocks high.

### To make an empty pyramid go to the line 204 and undo the following comment:
```
#pyramid_pi_object.build_empty_pyramid(5)
```
Running this code will make a pyramid appear that will be empty inside and will have an entrance if the height of the pyramid is greater than 4. In this case, we have that our pyramid will be 5 blocks high, therefore it will have an entrance.

### To make a tower go to the line 207 and undo the following comment:
```
#pyramid_pi_object.build_tower(mc,6,4,5)
```
If this function is run, it will make a tower appear, it will include a door if all its measurements (width, length and height) are greater than 2 blocks, the door will be on one of the longest sides of the tower, either the width or the length. In the part of the parentheses it is important to keep mc where it is, since without this nothing will be built, where 6 is located is the place to choose the width you want, where 4 is the place to choose the length and the last number, which is where 5 is, is the place to choose the height of the tower.
