from typing import Optional, Tuple
import pygame
import pymunk
from pymunk.body import Body
import pymunk.pygame_util
import math
from random import randint
from objects import Ball
from objects import meteotite
from objects import spaceship

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










sp=spaceship()
    
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
    
    
    sp.create_ball(space)
    

# Load an image from a file and convert it to a pygame surface
    #image = pygame.image.load("ball.png").convert_alpha()

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
            newb.append(x)
            x.create_ball(space)
        #for ball in newb:
        #    ball.body.position=pygame.mouse.get_pos()

         
         
            #ball.create_ball(space)
        #for i in range(len(newb)):
        #newb[0].create_ball(space)
            
    # Convert the body position to pygame coordinates and blit the image
        pos = pymunk.pygame_util.to_pygame((100,100), window)
        #window.blit(image, image.get_rect(center=pos))
        
 
        space.step(1/fps )
       
    

        draw(space,window,draw_options)
        clock.tick(fps)

    pygame.quit()

    
if __name__=="__main__":
    run(window,WIDTH,HEIGHT)
    