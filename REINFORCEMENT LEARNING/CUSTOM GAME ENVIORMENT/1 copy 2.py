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




# class Ball(pygame.sprite.Sprite):
#     def __init__(self, space, x, y, radius, image):
#         super().__init__()
#         self.space = space # pymunk.Space
#         self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, radius)) # pymunk.Body
#         self.body.position = x, y # initial position
#         self.shape = pymunk.Circle(self.body, radius) # pymunk.Shape
#         self.shape.elasticity = 0.9 # bounce factor
#         self.space.add(self.body, self.shape) # add body and shape to space
#         self.original_image = image # load image from file
#         self.original_image = pygame.transform.smoothscale(self.original_image, (radius * 2, radius * 2)) # scale image to match shape size
#         self.image = self.original_image # current image
#         self.rect = self.image.get_rect(center=self.body.position) # current rect

#     def update(self):
#         # update image and rect according to body position and angle
#         self.image = pygame.transform.rotate(self.original_image, -self.body.angle * 180 / 3.14)
#         self.rect = self.image.get_rect(center=self.body.position)
        

class Ball(pygame.sprite.Sprite):
    def __init__(self, space, x, y, radius, image):
        super().__init__()
        self.space = space # pymunk.Space
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, radius)) # pymunk.Body
        self.body.position = x, y # initial position
        self.shape = pymunk.Circle(self.body, radius) # pymunk.Shape
        self.shape.elasticity = 0.9 # bounce factor
        self.space.add(self.body, self.shape) # add body and shape to space
        self.original_image = image # load image from file
        self.original_image = pygame.transform.smoothscale(self.original_image, (radius * 2, radius * 2)) # scale image to match shape size
        self.image = self.original_image # current image
        self.rect = self.image.get_rect(center=self.body.position) # current rect

    def update(self):
        # update image and rect according to body position and angle
        self.image = pygame.transform.rotate(self.original_image, -self.body.angle * 180 / 3.14)
        self.rect = self.image.get_rect(center=self.body.position)
        window.blit(self.image, self.rect)

    
    
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
    
    
    
    image=pygame.image.load("ball.png").convert_alpha()
    ball = Ball(space, 100, 200, 50, image) # create ball sprite with image "ball.png"
    sprites = pygame.sprite.Group() # create sprite group


   
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False 
                break
                
    # Convert the body position to pygame coordinates and blit the image
        
 
        space.step(1/fps )
       
    
        sprites.update()
        ball.update()
        draw(space,window,draw_options)
        sprites.add(ball) # add ball sprite to group
        sprites.draw(window) # draw sprites on screen
        clock.tick(fps)

    pygame.quit()

    
if __name__=="__main__":
    run(window,WIDTH,HEIGHT)
    
    