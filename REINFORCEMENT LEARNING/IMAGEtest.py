import pygame
import sys
import pymunk
from random import randint
pygame.init()

screen=pygame.display.set_mode((640,480))

image=pygame.image.load(r"ball.png")


object_surface=pygame.Surface((100,100))
object_surface.blit(image,(0,0))
screen.fill("white")
pygame.display.update()
pygame.display.update()
from typing import Optional, Tuple
import pygame
import pymunk
from pymunk.body import Body
import pymunk.pygame_util
import math
from random import randint
pygame.init()

WIDTH = 800
HEIGHT = 800
window=pygame.display.set_mode((WIDTH,HEIGHT))






def draw(space,window,draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()
    
def create_boundries(space,width,height):
    rects=[  
           [(width/2,height-10),(width,20)],
            [(width/2,10),(width,20)],
            [(10,height/2),(20,height)],
             [(width-10,height/2),(20,height)], 
           
           
    ]
    
    for pos,size in rects:
        body=pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position=pos
        shape=pymunk.Poly.create_box(body,size)
        shape.elasticity=1
        shape.friction=0.5
        space.add(body,shape)


class Ball():
    
    def __init__(self,body=pymunk.Body(body_type=pymunk.Body.DYNAMIC),radius=10,color=(255,0,0,100)):
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.radius = radius
        self.color = color

        
    def create_ball(self,space,mass=100,elst=1,fric=0):
        self.body.position=(randint(100,700),(randint(100,700)))
        self.shape=pymunk.Circle(self.body,radius=self.radius)
        self.shape.mass=mass
        self.shape.elasticity=elst
        self.shape.friction=fric
        body=pymunk.Body()
        body.position=(randint(100,700),(randint(100,700)))
        space.add(self.body,self.shape)
        return self.shape
        
    
    
# def create_ball(space,radius,mass,number=1):
#     body=pymunk.Body()
#     body.position=(randint(100,700),(randint(100,700)))
#     if body.position>(800,800) or body.position<(0,0):
#         body.position=(randint(100,700),(randint(100,700)))

#     shape=pymunk.Circle(body,radius=radius)
#     shape.mass=mass    
#     shape.color=(255,0,0,100)
    
#      #   bod=body.copy()
#      #   shape
     
#     shape.elasticity=1
#     shape.friction=.1
#     space.add(body,shape)
#     return shape
    
    
def run(window,width,height):
    run = True
    clock = pygame.time.Clock()
    fps=60
    
    space=pymunk.Space()
    space.gravity=(0,98)
    
   
   # bal=create_ball(space,30,10,number=10)
    newb=[]
    #f#or ball in newb:
    #ball.create_ball(space)
    #ball=Ball(radius=30)
    #ball.create_ball(space)
    
    
    boundri=create_boundries(space,width,height)
    draw_options=pymunk.pygame_util.DrawOptions(window)
    
    
    
    

# Load an image from a file and convert it to a pygame surface
    image = pygame.image.load("ball.png").convert_alpha()

# Create a DrawOptions object to draw the space
    draw_options = pymunk.pygame_util.DrawOptions(window)
           
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False 
                break
        if event.type==pygame.MOUSEBUTTONDOWN:
            #ball.body.position=pygame.mouse.get_pos()
            x=Ball(radius=30)
            x.body.position=pygame.mouse.get_pos()
            x.create_ball(space)
            newb.append(x)
            
        #for ball in newb:
        #    ball.body.position=pygame.mouse.get_pos()

         
         
            #ball.create_ball(space)

            
    # Convert the body position to pygame coordinates and blit the image
        pos = pymunk.pygame_util.to_pygame((100,100), window)
        
        window.blit(image,(0,0))
        
 
        space.step(1/fps )
       
    

        draw(space,window,draw_options)
        clock.tick(fps)

    pygame.quit()

    
if __name__=="__main__":
    run(window,WIDTH,HEIGHT)
    
    