import pygame
import pymunk
import pymunk.pygame_util
import math
from random import randint
pygame.init()

WIDTH = 800
HEIGHT = 800
window=pygame.display.set_mode((WIDTH,HEIGHT))

def calculate_distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def calculate_angle(p1,p2):
    return math.atan2(p1[1]-p2[1],p1[0]-p2[0])



def draw(space,window,draw_options,line,ball):
    window.fill("white")
    if ball:
        print(line[0])
        pygame.draw.line(window,color=(255,0,0,100),start_pos=line[0],end_pos=line[1],width=3)
    #try:
    #    pass
    #except:pass   
    print(line)
    space.debug_draw(draw_options)
  #  if 1==1:
  #          pygame.draw.line(window,color=(255,0,0,100),start_pos=pressed_pos,end_pos=(200,100),width=3)


    
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
        shape.elasticity=0.5
        shape.friction=0.5
        space.add(body,shape)

def create_ball(space,radius,mass,number=1,pos=(0,0)):
    body=pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position=pos
    if body.position>(800,800) or body.position<(0,0):
        body.position=(randint(100,700),(randint(100,700)))

    shape=pymunk.Circle(body,radius=radius)
    shape.mass=mass
    shape.color=(255,0,0,100)

     #   bod=body.copy()
     #   shape

    shape.elasticity=2
    shape.friction=.1
    space.add(body,shape)
    return shape


def run(window,width,height):
    run = True
    clock = pygame.time.Clock()
    fps=60

    space=pymunk.Space()
    space.gravity=(0,98)


   # ball=create_ball(space,30,10,number=10)
   # boundri=create_boundries(space,width,height)

    draw_options=pymunk.pygame_util.DrawOptions(window)


    pressed_pos=None
    ball=None




# Load an image from a file and convert it to a pygame surface
    image = pygame.image.load("ball.png").convert_alpha()
    create_boundries(space,width,height)
# Create a DrawOptions object to draw the space
    draw_options = pymunk.pygame_util.DrawOptions(window)
    line=[]
    while run: 
        
        
        if ball:line=[ball.body.position,pygame.mouse.get_pos()]

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            if not ball:
                pressed_pos=pygame.mouse.get_pos()
                ball=create_ball(space,30,10,number=10,pos=pressed_pos)
                
            elif pressed_pos:
                ball.body.body_type=pymunk.Body.DYNAMIC
                ball.body.apply_impulse_at_local_point((100,0),(0,0))
                pressed_pos=None
        
        if ball:line=[ball.body.position,pygame.mouse.get_pos()]
                
        print(line,len(line))
    # Convert the body position to pygame coordinates and blit the image
        pos = pymunk.pygame_util.to_pygame((100,100), window)
        window.blit(image, image.get_rect(center=pos))



        space.step(1/fps )
        draw(space,window,draw_options,line,ball)
        clock.tick(fps)

    pygame.quit()


if __name__=="__main__":
    run(window,WIDTH,HEIGHT)

