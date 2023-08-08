import pygame
import pymunk

screen = pygame.display.set_mode((800, 800))
space = pymunk.Space()
space.gravity = (0,90)  # Adjusted gravity value
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



static_lines = [
        pymunk.Segment(space.static_body, (0, 780.0), (780, 780), 0.0),
        pymunk.Segment(space.static_body, (780, 780), (780, 0), 0.0),
        pymunk.Segment(space.static_body, (780, 0), (0, 0), 0.0),
        pymunk.Segment(space.static_body, (0, 0), (0, 780), 0.0)
    ]
for l in static_lines:
        l.friction = 0.5
        l.color = pygame.color.THECOLORS['blue']
        
space.add(*static_lines)

    

    





# Dictionary to keep track of key states
keys_pressed = {}




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
    vx = ((keys_pressed.get(pygame.K_d, False) - keys_pressed.get(pygame.K_a, False)))*100 
    vy = (keys_pressed.get(pygame.K_s, False) - keys_pressed.get(pygame.K_w, False))*100
    box.velocity = (vx, vy)

    # Clear the screen
    screen.fill((0, 0, 0))
    #screen.blit(pygame.image.load('background.png'),(0,0))

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