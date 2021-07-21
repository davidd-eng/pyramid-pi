from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

class Pyramid_pi:
    def __init__(self, block):
        self.block = block
        
    def build_square(self,mc,x,y,z,s,h):
        for j in range(s):
            for i in range(s):
                mc.setBlock(x+i,y+h,z+j,self.block)

    def build_pyramid(self,h):
        x, y, z = mc.player.getPos()
        new_x, new_y, new_z = mc.player.getPos()
        square_size = h*2-1
        new_size = square_size
        for i in range(h):
            new_x= x+i
            new_z= z+i
            new_size= square_size-2*i
            self.build_square(mc,new_x,new_y,new_z,new_size,i)

    def build_empty_pyramid(self,h):
        x, y, z = mc.player.getPos()
        new_x, new_y, new_z = mc.player.getPos()
        square_size = h*2-1
        new_size = square_size
        for i in range(h):
            new_x = x+i
            new_z = z+i
            new_size = square_size-2*i
            self.build_frame(mc,new_x,new_y+i,new_z,new_size,i)
            
        # build entrance
        self.build_entrance(mc,x,y,z,square_size,h)
    
    def build_entrance(self,mc,x,y,z,s,h):
        #find the middle
        middle = (s-1)/2
        #verifying the height to be able to have an entrance
        if h>4:
            #break the blocks for the entrance
            new_x = x + middle
            new_y = y + 1
            new_z = z + 1
            mc.setBlock(new_x,y,z,block.AIR.id)
            
            mc.setBlock(new_x,new_y,new_z,block.AIR.id)
            #build the door
            mc.setBlock(new_x,y,z+2,block.DOOR_WOOD.id,0)
            mc.setBlock(new_x,y+1,z+2,block.DOOR_WOOD.id,8)
            
        
    def build_frame(self,mc,x,y,z,s,h):
        
        if s == 1:
            mc.setBlock(x,y,z,self.block)
        
        for i in range(s-1):
            new_x = x + i
            new_y = y
            new_z = z
            mc.setBlock(new_x, new_y, new_z, self.block)
     
        for j in range(s-1):
            new_x = x + (s-1)
            new_y = y  
            new_z = z + j
            mc.setBlock(new_x, new_y, new_z, self.block)
            
        for k in range(s-1):
            new_x = x + (s-1) - k
            new_y = y
            new_z = z + (s-1)
            mc.setBlock(new_x, new_y, new_z, self.block)
            
        for l in range(s-1):
            new_x = x 
            new_y = y
            new_z = z + (s-1) - l
            mc.setBlock(new_x, new_y, new_z, self.block)
        
    x, y, z = mc.player.getPos()
    
    def build_tower(self,mc,width,length,height):
        x, y, z = mc.player.getPos()
        for i in range(height):
            self.build_tower_frame(mc,width,length,i)
        
        #build the roof
        self.build_roof(mc,width,length,height)
        
        #build the entrance
        self.build_tower_entrance(mc,x,y,z,width,length,height)
            
    def build_tower_frame(self,mc,width,length,height):
        
        x, y, z = mc.player.getPos()
        
        for i in range(width):
            new_x = x+i 
            new_y = y+height
            new_z = z
            mc.setBlock(new_x,new_y,new_z,self.block)
            
        for i in range(length):
            new_x = new_x
            new_y = y+height
            new_z = z+i
            mc.setBlock(new_x,new_y,new_z,self.block)
            
        for i in range(width):
            new_x = x+i
            new_y = y+height
            new_z = new_z
            mc.setBlock(new_x,new_y,new_z,self.block)
            
        for i in range(length):
            new_x = x
            new_y = y+height
            new_z = z+i
            mc.setBlock(new_x,new_y,new_z,self.block)
    
    def build_roof(self,mc,width,length,height):
        x, y, z = mc.player.getPos()
        new_x = x
        new_y = y+height
        new_z = z
        for j in range(length):
            for i in range(width):
                mc.setBlock(new_x+i,new_y,new_z+j,self.block)
                
    def build_tower_entrance(self,mc,x,y,z,width,length,height):
        #verifying the measurements to be able to have an entrance
        if width>2 and length>2 and height>2:
            
            if width>=length:
                
                if width % 2 == 0:
                    #find the middle
                    middle = width/2
                    #find the space for the entrance
                    new_x = x + middle
                    new_y = y 
                    new_z = z
                    #build the doors
                    mc.setBlock(new_x,new_y,new_z,block.DOOR_WOOD.id,0)
                    mc.setBlock(new_x,new_y+1,new_z,block.DOOR_WOOD.id,8)
                    mc.setBlock(new_x-1,new_y,new_z,block.DOOR_WOOD.id,0)
                    mc.setBlock(new_x-1,new_y+1,new_z,block.DOOR_WOOD.id,8)
                    
                    
                else:
                    #find the middle
                    middle = (width-1)/2
                    #find the space for the entrance
                    new_x = x + middle
                    new_y = y 
                    new_z = z
                    #build the door
                    mc.setBlock(new_x,new_y,new_z,block.DOOR_WOOD.id,0)
                    mc.setBlock(new_x,new_y+1,new_z,block.DOOR_WOOD.id,8)
                
            else:
                
                if length % 2 == 0:
                    #find the middle
                    middle = length/2
                    #find the space for the entrance
                    new_x = x 
                    new_y = y 
                    new_z = z + middle
                    #build the doors
                    mc.setBlock(new_x,new_y,new_z,block.DOOR_WOOD.id,0)
                    mc.setBlock(new_x,new_y+1,new_z,block.DOOR_WOOD.id,8)
                    mc.setBlock(new_x,new_y,new_z-1,block.DOOR_WOOD.id,0)
                    mc.setBlock(new_x,new_y+1,new_z-1,block.DOOR_WOOD.id,8)
                    
                    
                else:
                    #find the middle
                    middle = (length-1)/2
                    #find the space for the entrance
                    new_x = x 
                    new_y = y 
                    new_z = z + middle
                    #build the door
                    mc.setBlock(new_x,new_y,new_z,block.DOOR_WOOD.id,0)
                    mc.setBlock(new_x,new_y+1,new_z,block.DOOR_WOOD.id,8)
        
        else:
            print('To build the door width,length and height must be more than 2 blocks')

pyramid_pi_object = Pyramid_pi(block.STONE.id)

#precolumbian_builder_object.build_empty_pyramid(5)
#precolumbian_builder_object.build_roof(mc,5,3,4)
pyramid_pi_object.build_tower(mc,6,4,5)
