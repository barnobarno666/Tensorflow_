import pygame
import pymunk
import math

screen = pygame.display.set_mode((800, 800))
space = pymunk.Space()
space.gravity = (0,0)  # Adjusted gravity value
#space.damping = 0.9
box = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
box_shape = pymunk.Circle(box, radius=30)  # Reduced radius value for better visualization
box_shape.friction = 0.5  # Adjusted friction value
box_shape.elasticity = 0.95  # Adjusted elasticity value
box.position = 400, 400
box_shape.body = box
space.add(box, box_shape)

new= pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
new_shape = pymunk.Circle(new, radius=30)  # Reduced radius value for better visualization
space.add(new, new_shape)


class spaceship:
    def __init__(self,power=1,screen=screen,space=space) -> None:
        self.body=pymunk.Body(mass=10,body_type=pymunk.Body.DYNAMIC)
        self.shape=pymunk.Poly(self.body, vertices=[(0,0),(50,50),(25,25),(0,0)], radius=3)
        self.shape.friction = 0.5  # Adjusted friction value
        self.shape.mass=1000
        self.shape.elasticity = 0.05  # Adjusted elasticity value
        self.intertia=self.shape.moment
        self.body.position = (400, 400)
        self.power=power
        self.shape.body = self.body

        space.add(self.body, self.shape)
        
    # def moving(self,keys_pressed,keystroke):
        
    #     forcebam = ((keys_pressed.get(pygame.K_d, False) - keys_pressed.get(pygame.K_a, False)))*self.power
    #     forcedan = (keys_pressed.get(pygame.K_s, False) - keys_pressed.get(pygame.K_w, False))*self.power
        
        
    #     self.body.apply_force_at_local_point((forcedan,0),(   50    ,50 ))
    #     self.body.apply_force_at_local_point((forcebam,0),(   0  ,0 ))
        
        
    #     #find a way to make it so that the force is applied to the center of mass
    #     angle=self.body.angle
    #     angle=math.degrees(angle)
        
       # return angle
      
        
static_lines = [
        pymunk.Segment(space.static_body, (0, 780.0), (780, 780), 10.0),
        pymunk.Segment(space.static_body, (780, 780), (780, 0), 10.0),
        pymunk.Segment(space.static_body, (780, 0), (0, 0), 10.0),
        pymunk.Segment(space.static_body, (0, 0), (0, 780), 10.0)
    ]
for l in static_lines:
        l.friction = 0.5
        l.color = pygame.color.THECOLORS['blue']
        
space.add(*static_lines)

    

    





# Dictionary to keep track of key states
keys_pressed = {}


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
        screen.blit(self.image, self.rect)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            keys_pressed[event.key] = False

    # Update the body's velocity based on the keys pressed
    vx = ((keys_pressed.get(pygame.K_d, False) - keys_pressed.get(pygame.K_a, False)))*1000
    vy = (keys_pressed.get(pygame.K_s, False) - keys_pressed.get(pygame.K_w, False))*1000
    box.velocity = (vx, vy)

    # Clear the screen
    screen.fill((0, 0, 0))
    #screen.blit(pygame.image.load('background.png'),(0,0))

        
    ship=spaceship(space=space,screen=  screen)
    #ship.moving(keys_pressed,pygame.KEYDOWN)
    screen.blit(pygame.image.load('player.png'), (400,400))
    print(ship.body.position)
    
        
    # Draw the circle at the current body position
    #pygame.draw.circle(screen, (255, 255, 255), (int(box.position.x), int(box.position.y)), 30)
    screen.blit(pygame.image.load('enemy.png'), (int(box.position.x), int(box.position.y)))

    for line in static_lines:
            body = line.body

            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = round(pv1.x), round((pv1.y))
            p2 = round(pv2.x), round((pv2.y))
            pygame.draw.lines(screen, pygame.Color("lightgray"), False, [p1, p2], 2)


    s=Ball(space,400,400,30,pygame.image.load('background.png'))
    
        

    # Step the physics simulation
    dt = 1.0 / 60.0
    space.step(dt)

    

    # Update the display
    pygame.display.update()



    """
    def convert_vertices(shape):
    # convert local vertices to world vertices
    verts = []
    for v in shape.get_vertices():
        x = v.rotated(shape.body.angle).x + shape.body.position.x
        y = v.rotated(shape.body.angle).y + shape.body.position.y
        verts.append((x, y))
    return verts
Copy
And then use it in your drawing function like this:

def draw_poly(shape):
    pygame.draw.polygon(screen, [255, 255, 255], convert_vertices(shape))

    """