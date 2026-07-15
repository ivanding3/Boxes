import pygame
import vars


def center(size,pos):
    width = size[0]
    height = size[1]
    left = pos[0]
    top = pos[1]
    return (width/2+left,height/2+top)

def sign(num):
    if num > 0 :return 1
    if num < 0 :return-1
    if num == 0:return 0

class sprite:
    def __init__(self,pos,size,texture_name,vel = (0,0), accel = (0,0)):
        self.pos = pos
        self.vel = vel
        self.accel = accel
        self.size = size
        self.surface = pygame.transform.scale(pygame.image.load(texture_name),size)
        self.rect = pygame.Rect(pos,size)

    @property
    def pos(self):
        return (self.x,self.y)
    @pos.setter
    def pos(self,tuple):
        (self.x,self.y) = tuple
    @property
    def vel(self):
        return (self.velx,self.vely)
    @vel.setter
    def vel(self,vel):
        (self.velx,self.vely) = vel
    @property
    def accel(self):
        return (self.accelx,self.accely)
    @accel.setter
    def accel(self,accel):
        (self.accelx,self.accely) = accel
    @property
    def input_direction(self):
        return (self.input_directionx,self.input_directiony)
    @input_direction.setter
    def input_direction(self,tuple):
        (self.input_directionx,self.input_directiony) = tuple  
    @property
    def vel_direction(self):
        return (self.vel_directionx,self.vel_directiony)
    @vel_direction.setter
    def vel_direction(self,tuple):
        (self.vel_directionx,self.vel_directiony) = tuple  
    @property
    def size(self):
        return (self.width,self.height)
    @size.setter
    def size(self, tuple):
        (self.width,self.height) = tuple
    @property
    def left(self):
        return self.x
    @left.setter
    def left(self,val):   
        self.x = val
    @property
    def right(self):
        return self.x + self.width
    @right.setter
    def right(self,val):
        self.x = val - self.width
    @property
    def top(self):
        return self.y
    @top.setter
    def top(self,val):
        self.y = val
    @property
    def bottom(self):
        return self.y + self.height
    @bottom.setter
    def bottom(self,val):
        self.y = val - self.height
    @property
    def center(self):
        return (self.centerx,self.centery)
    @center.setter
    def center(self,tuple):
        (self.centerx,self.centery) = tuple
    @property
    def centerx(self):
        return self.width/2+self.left
    @centerx.setter
    def centerx(self,val):
        self.x = val-self.width/2
    @property
    def centery(self):
        return self.height/2+self.top
    @centery.setter
    def centery(self,val):
        self.y = val-self.height/2



class Player(sprite):
    def __init__(self, pos, size, texture_name, vel=(0, 0), accel=(0, 0)):
        super().__init__(pos, size, texture_name, vel, accel)
        self.colliding_left_wall = False
        self.colliding_right_wall = False
        self.colliding_ceiling = False
        self.colliding_floor = False
        self.collided_floor = False
    def movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and keys_pressed[pygame.K_s]:
            self.input_direction
        if keys_pressed[pygame.K_w] and not self.colliding_ceiling:
            self.jump()

        elif keys_pressed[pygame.K_s]and not self.colliding_floor: 
            self.accely = 500 
            self.input_directiony = 1

        else:
            self.accely = 0
            self.input_directiony = 0


        #movement y
        if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_d]:
            self.accelx = 0
        elif keys_pressed[pygame.K_a] and not self.colliding_right_wall:
            self.accelx = -500
            self.input_directionx = 1

        elif keys_pressed[pygame.K_d] and not self.colliding_left_wall:
            self.accelx = 500    
            self.input_directionx = -1

        else:
            self.accelx = 0
            self.input_directionx = 0
   
    
    def on_floor(self):
        pass
    
    def on_wall(self): 
        pass


    def air_res(self):
        self.vel = [vel-vel*vars.dt*0.5 for vel in self.vel]

    def gravity(self):
        self.vely += 1000*vars.dt     

    def update_movement(self):
        self.velx += self.accelx*vars.dt
        self.vely += self.accely*vars.dt
        self.x += self.velx*vars.dt
        self.y += self.vely*vars.dt
        self.vel_direction = tuple(map(sign,self.vel))
    
    def jump(self):
        if self.collided_floor:
            self.vely = -500
            self.vel_directiony = -1
            self.collided_floor = False
        else: 
            self.accely = -400

           

    def dash(self):
        pass

    def create_crumble(self):
        pass




player = Player((800,500),(100,100),'boxplayer.webp')

    







#create player









