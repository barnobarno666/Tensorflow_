import pygame
import pymunk
import pymunk.pygame_util

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pymunk Pygame Example")

# Create a clock to control the framerate
clock = pygame.time.Clock()

# Create a pymunk space and set its gravity
space = pymunk.Space()
space.gravity = (0, -900)

# Create a static ground body and shape
ground = pymunk.Body(body_type=pymunk.Body.STATIC)
ground.position = (400, 50)
ground_shape = pymunk.Segment(ground, (-400, 0), (400, 0), 10)
space.add(ground, ground_shape)

# Create a dynamic body and shape
body = pymunk.Body(10, 100)
body.position = (400, 300)
shape = pymunk.Circle(body, 50)
space.add(body, shape)

# Load an image from a file and convert it to a pygame surface
image = pygame.image.load("ball.png").convert_alpha()

# Create a DrawOptions object to draw the space
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the space using the DrawOptions object
    space.debug_draw(draw_options)

    # Convert the body position to pygame coordinates and blit the image
    pos = pymunk.pygame_util.to_pygame(body.position, screen)
    screen.blit(image, image.get_rect(center=pos))

    # Update the space
    space.step(1/60)

    # Update the display
    pygame.display.flip()

    # Control the framerate
    clock.tick(60)

# Quit pygame
pygame.quit()
